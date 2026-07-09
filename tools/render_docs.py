#!/usr/bin/env python3
"""VRIMS Multi-Level Document Renderer.

Reads render settings from render/*.yaml, filters Markdown source content
by document level (executive / business / functional / technical), and
generates .docx output via a node+docx-js generator.

Usage:
  python tools/render_docs.py --document booking_review --level business --format docx
  python tools/render_docs.py --document wellness_centre_review --level executive --format docx

Rules (per render/glm-render-guide.md):
  1. Do not invent business rules.
  2. Do not rewrite business decisions.
  3. Do not change Markdown source.
  4. Use render settings under render/.
  5. If content is missing, report it as missing instead of creating it.
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pyyaml is required: pip3 install pyyaml")

# ── Paths ────────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parent.parent
RENDER_DIR = REPO_ROOT / "render"
TOOLS_DIR = REPO_ROOT / "tools"
DOCX_BUILD = REPO_ROOT / ".docx-build"  # node + docx live here


# ── YAML config loading ──────────────────────────────────────────────────────
def load_yaml(name):
    p = RENDER_DIR / name
    if not p.exists():
        sys.exit(f"Config not found: {p}")
    with open(p) as f:
        return yaml.safe_load(f)


def load_configs():
    return {
        "render_config": load_yaml("render-config.yaml"),
        "levels": load_yaml("document-levels.yaml"),
        "include_rules": load_yaml("include-rules.yaml"),
        "build_order": load_yaml("build-order.yaml"),
    }


# ── Source resolution ────────────────────────────────────────────────────────
def resolve_sources(doc_key, build_order):
    """Return (found_files, missing_files) for a document key."""
    docs = build_order.get("documents", {})
    if doc_key not in docs:
        available = ", ".join(docs.keys())
        sys.exit(f"Document '{doc_key}' not in build-order.yaml. Available: {available}")
    doc = docs[doc_key]
    sources = doc.get("sources", [])
    found, missing = [], []
    for src in sources:
        full = REPO_ROOT / src
        if src.endswith("/"):
            # Directory — collect all .md files inside
            if full.is_dir():
                for md in sorted(full.glob("*.md")):
                    found.append(md)
            else:
                missing.append(src + " (directory not found)")
        else:
            if full.is_file():
                found.append(full)
            else:
                missing.append(src)
    return doc, found, missing


# ── Heading-based content filtering ──────────────────────────────────────────
def parse_headings(md_text):
    """Split markdown into blocks keyed by their heading.
    Returns list of (heading_level, heading_text, block_lines).
    The first block (before any heading) is (0, '', preamble_lines).
    """
    lines = md_text.split("\n")
    blocks = []
    cur_level, cur_heading, cur_lines = 0, "", []

    # Skip YAML front matter
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1

    while i < len(lines):
        line = lines[i]
        hm = None
        if line.strip():
            import re
            hm = re.match(r"^(#{1,6})\s+(.+)$", line)
        if hm:
            # flush previous block
            blocks.append((cur_level, cur_heading, cur_lines))
            cur_level = len(hm.group(1))
            cur_heading = hm.group(2).strip()
            cur_lines = []
        else:
            cur_lines.append(line)
        i += 1
    blocks.append((cur_level, cur_heading, cur_lines))
    return blocks


def should_include_heading(heading_text, level, include_rules):
    """Decide if a heading's content should be included for this level."""
    rules = include_rules.get("rules", {}).get("heading_based", {})
    lr = rules.get(level, {})

    # functional level: include_all_business + extra headings
    if level == "functional":
        return True  # functional includes everything business + more

    # executive and business: use include/exclude lists
    includes = [h.lower() for h in lr.get("include_headings", [])]
    excludes = [h.lower() for h in lr.get("exclude_headings", [])]
    h_lower = heading_text.lower().strip()

    # Strip leading numbering like "1. " or "10. "
    import re
    h_clean = re.sub(r"^\d+\.\s*", "", h_lower).strip()
    # Strip "BS-BKG-001 — " prefix etc.
    h_clean = re.sub(r"^[A-Z]{2}-[A-Z]{3}-\d+\s*[—–-]\s*", "", h_clean).strip()

    if not h_clean:
        return True  # preamble / non-heading block always included

    # Check exclude first (more specific)
    for ex in excludes:
        if ex in h_clean or h_clean in ex:
            return False

    # Check include
    for inc in includes:
        if inc in h_clean or h_clean in inc:
            return True

    # For headings that are document titles (H1), always include
    # For business level, be permissive — include unknown headings
    if level == "business":
        return True

    # For executive, be restrictive — exclude unknown headings
    return False


def filter_markdown(md_text, level, include_rules):
    """Filter markdown content by heading rules for the given level."""
    blocks = parse_headings(md_text)
    filtered = []

    for blk_level, blk_heading, blk_lines in blocks:
        if blk_level == 0:
            # Preamble — keep (usually empty after front matter strip)
            if any(l.strip() for l in blk_lines):
                filtered.extend(blk_lines)
            continue

        if should_include_heading(blk_heading, level, include_rules):
            # Re-emit the heading + its content
            filtered.append("#" * blk_level + " " + blk_heading)
            filtered.extend(blk_lines)

    return "\n".join(filtered)


# ── Orchestrate docx generation ──────────────────────────────────────────────
def generate_docx(doc_meta, level, level_meta, found_files, missing_files, output_path):
    """Filter content, write a JSON payload, call node generator."""
    # Build content sections
    sections = []
    for md_path in found_files:
        md_text = md_path.read_text("utf-8")
        filtered = filter_markdown(md_text, level, load_configs()["include_rules"])
        if filtered.strip():
            sections.append({
                "source": str(md_path.relative_to(REPO_ROOT)),
                "markdown": filtered,
            })

    payload = {
        "document_id": doc_meta.get("document_id", ""),
        "title": doc_meta.get("title", ""),
        "level": level,
        "level_label": level_meta.get("label", level),
        "audience": level_meta.get("audience", []),
        "target_pages": level_meta.get("target_pages", ""),
        "sections": sections,
        "missing_files": missing_files,
        "repo_root": str(REPO_ROOT),
        "output_path": str(output_path),
    }

    # Write payload to temp JSON
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, dir=str(TOOLS_DIR)) as f:
        json.dump(payload, f, ensure_ascii=False)
        payload_path = f.name

    # Call node generator
    gen_script = TOOLS_DIR / "render_docx.js"
    if not gen_script.exists():
        sys.exit(f"Node generator not found: {gen_script}")

    env = os.environ.copy()
    env["NODE_PATH"] = str(DOCX_BUILD / "node_modules")
    result = subprocess.run(
        ["node", str(gen_script), payload_path],
        capture_output=True, text=True, env=env,
    )
    if result.returncode != 0:
        print(result.stdout)
        sys.exit(f"Node generator failed:\n{result.stderr}")
    print(result.stdout)

    # Print missing content report
    if missing_files:
        print("\n⚠️  Missing content report:")
        for m in missing_files:
            print(f"   ✗ {m}")
        print("   (These files are referenced in build-order.yaml but do not exist.)")
        print("   (Per render guide rule 6, missing content is reported, not created.)")

    os.unlink(payload_path)


# ── Main ─────────────────────────────────────────────────────────────────────
def main(argv=None):
    parser = argparse.ArgumentParser(
        description="VRIMS multi-level document renderer.",
        epilog="Example: python tools/render_docs.py --document booking_review --level business --format docx",
    )
    parser.add_argument("--document", required=True,
                        help="Document key from build-order.yaml (e.g. booking_review)")
    parser.add_argument("--level", required=True,
                        choices=["executive", "business", "functional", "technical"],
                        help="Document level/depth")
    parser.add_argument("--format", default="docx", choices=["docx"],
                        help="Output format (currently only docx)")
    args = parser.parse_args(argv)

    configs = load_configs()

    # Resolve document + sources
    doc_meta, found_files, missing_files = resolve_sources(args.document, configs["build_order"])
    print(f"Document : {doc_meta.get('document_id', '?')} — {doc_meta.get('title', '?')}")
    print(f"Level    : {args.level}")
    print(f"Sources  : {len(found_files)} found, {len(missing_files)} missing")

    # Get level metadata
    levels = configs["levels"].get("levels", {})
    level_meta = levels.get(args.level, {})

    # Determine output path
    render_config = configs["render_config"]
    output_paths = render_config.get("output_paths", {})
    out_dir = REPO_ROOT / output_paths.get(args.level, f"exports/{args.level}")
    out_dir.mkdir(parents=True, exist_ok=True)

    naming = render_config.get("naming", {})
    pattern = naming.get("pattern", "{document_id}_{title}_{level}_{version}")
    doc_id = doc_meta.get("document_id", "VRIMS-DOC")
    title = doc_meta.get("title", "Document").replace(" ", "-")
    version = "0.5R"  # from release
    filename = pattern.format(document_id=doc_id, title=title, level=args.level, version=version) + ".docx"
    output_path = out_dir / filename

    print(f"Output   : {output_path}")
    print()

    generate_docx(doc_meta, args.level, level_meta, found_files, missing_files, output_path)

    if output_path.exists():
        size_kb = output_path.stat().st_size / 1024
        print(f"\n✅ Generated: {output_path}")
        print(f"   Size: {size_kb:.1f} KB")
    else:
        sys.exit("❌ Output file was not created.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
