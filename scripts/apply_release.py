#!/usr/bin/env python3
"""Apply a VRIMS documentation release ZIP into the repo, then commit + push.

Codifies the documentation-release workflow so the rules run every time:

  1. Apply release files exactly as provided (no rewriting/summarizing).
  2. Preserve folder structure.
  3. Never `git add -A` — stage only the release paths (keeps .DS_Store etc. out).
  4. Use commit-message.txt (if present) verbatim as the commit message, via
     `git commit -F`; the file itself is NOT committed into the repo.
  5. Show changed files before committing.
  6. Commit + push to the current branch's upstream (origin <branch>).

Validation gates enforced here:
  - PATH SAFETY: reject zip-slip (absolute / `..` paths), anything under
    `.git`/`.github`, and any path outside the allowed top-level dirs
    {core, modules, shared, standards, review} or the repo root.
  - OVERWRITE DETECTION: classify each target NEW vs OVERWRITE and report it.
    Overwrites are allowed (e.g. CHANGELOG.md) but shown loudly.
  - DIRTY-TREE GUARD: abort if there are already-staged changes, so the
    release commit can't co-mingle unrelated work.

USAGE
  scripts/apply_release.py ZIP_PATH [--repo REPO_PATH] [--dry-run]

EXAMPLES
  # Preview what a release would do, change nothing:
  scripts/apply_release.py release-003.2.zip --dry-run

  # Apply + commit + push from inside the repo:
  scripts/apply_release.py "/path/to/release-003.2.zip"

  # Apply against a specific repo checkout:
  scripts/apply_release.py release-003.2.zip --repo /path/to/vrims-docs

NOTE
  The script pushes to origin automatically with no prompt. Use --dry-run to
  preview, and rely on the path-safety abort + dirty-tree guard for safety.
  To add an interactive "push? [y/N]" prompt, insert an input() call before
  the push step (search for "PUSH STEP" below).
"""

import argparse
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

# Top-level dirs a release is allowed to write into. Root-level files are
# always allowed. Anything else (e.g. .git/, random dirs) aborts the run.
ALLOWED_TOP_DIRS = {"core", "modules", "shared", "standards", "review"}

# Files that are packaging metadata, not content. They are never written into
# the repo. commit-message.txt is consumed as the commit message.
META_FILES = {"commit-message.txt"}


class ReleaseError(Exception):
    """Raised when a release cannot be safely applied."""


# --------------------------------------------------------------------------- #
# Small helpers
# --------------------------------------------------------------------------- #
def run_git(repo, *args, capture=True, check=True):
    """Run a git command in `repo`, returning completed stdout (str)."""
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=capture,
        text=True,
    )
    if check and result.returncode != 0:
        raise ReleaseError(
            f"git {' '.join(args)} failed ({result.returncode}):\n"
            f"{result.stderr.strip() or '(no stderr)'}"
        )
    return result.stdout.strip() if capture else ""


def info(msg=""):
    print(msg)


def warn(msg):
    # Informational warning, not a fatal error — print to stdout so it stays
    # in order with the rest of the (stdout) reporting.
    print(f"  ⚠️  {msg}")


def good(msg):
    print(f"  ✅ {msg}")


# --------------------------------------------------------------------------- #
# Pre-flight
# --------------------------------------------------------------------------- #
def preflight(repo):
    """Report branch/remote; abort if there are already-staged changes."""
    branch = run_git(repo, "rev-parse", "--abbrev-ref", "HEAD")
    remote = run_git(repo, "remote", "get-url", "origin", check=False) or "(no origin)"
    info(f"Repo   : {repo}")
    info(f"Branch : {branch}")
    info(f"Remote : {remote}")
    info("")

    # Dirty-tree guard: staged changes would be swept into the release commit.
    staged = run_git(repo, "diff", "--cached", "--name-only")
    if staged:
        raise ReleaseError(
            "There are already-staged changes in the repo:\n"
            + "\n".join(f"  {f}" for f in staged.splitlines())
            + "\n\nCommit or stash them first so the release commit stays clean."
        )

    # Warn (don't abort) on unstaged/untracked changes — targeted add won't touch them.
    dirty = run_git(repo, "status", "--short")
    if dirty:
        warn("Working tree is not clean (targeted add will ignore these):")
        for line in dirty.splitlines():
            warn(f"    {line}")
        info("")


# --------------------------------------------------------------------------- #
# Zip inspection + validation
# --------------------------------------------------------------------------- #
def inspect_zip(zip_path):
    """Return (content_entries, commit_message_path) from the zip.

    content_entries: list of (relpath_str,) for files that should be written
    into the repo (i.e. not META_FILES).
    commit_message_path: the in-zip path to commit-message.txt, or None.
    """
    with zipfile.ZipFile(zip_path) as zf:
        names = [n for n in zf.namelist() if not n.endswith("/")]

    content = []
    commit_msg = None
    for name in names:
        # Normalize to forward-slash POSIX relpath; drop any leading "./".
        rel = name.replace("\\", "/").lstrip("./")
        base = rel.split("/")[-1]
        if base == "commit-message.txt":
            commit_msg = name
            continue
        if base in META_FILES:
            # e.g. glm-import-instructions.md is packaging meta -> skip
            continue
        content.append(rel)
    return sorted(content), commit_msg


def validate_paths(content_entries):
    """Path-safety gate. Raises ReleaseError on the first unsafe path."""
    violations = []
    for rel in content_entries:
        parts = rel.split("/")
        # zip-slip / absolute
        if rel.startswith("/") or ".." in parts:
            violations.append(f"{rel}  (absolute or contains '..')")
            continue
        # never touch git internals
        if parts[0] in (".git", ".github"):
            violations.append(f"{rel}  (under .git/.github)")
            continue
        # root-level file is fine; otherwise first part must be an allowed dir
        if len(parts) == 1:
            continue
        if parts[0] not in ALLOWED_TOP_DIRS:
            violations.append(
                f"{rel}  (top-level '{parts[0]}' not in {sorted(ALLOWED_TOP_DIRS)})"
            )
    if violations:
        raise ReleaseError(
            "Path-safety check failed — refusing to apply:\n"
            + "\n".join(f"  ✗ {v}" for v in violations)
        )


def classify(content_entries, repo):
    """Return list of (rel, status) where status is 'NEW' or 'OVERWRITE'."""
    rows = []
    for rel in content_entries:
        status = "OVERWRITE" if (repo / rel).exists() else "NEW"
        rows.append((rel, status))
    return rows


# --------------------------------------------------------------------------- #
# Apply
# --------------------------------------------------------------------------- #
def copy_in(staging, content_entries, repo):
    """Copy release files from the staging dir into the repo, preserving paths."""
    for rel in content_entries:
        src = staging / rel
        dst = repo / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


# --------------------------------------------------------------------------- #
# Orchestration
# --------------------------------------------------------------------------- #
def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Apply a VRIMS doc release ZIP, then commit + push.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("USAGE")[1] if "USAGE" in __doc__ else None,
    )
    parser.add_argument("zip_path", help="Path to the release .zip")
    parser.add_argument("--repo", help="Repo root (default: git toplevel)")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate + classify only; do not copy/commit/push",
    )
    args = parser.parse_args(argv)

    zip_path = Path(args.zip_path).expanduser().resolve()
    if not zip_path.is_file():
        return _fail(f"Zip not found: {zip_path}")

    # Resolve repo root.
    if args.repo:
        repo = Path(args.repo).expanduser().resolve()
    else:
        out = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True,
        )
        if out.returncode != 0:
            return _fail("Not inside a git repo and --repo not given.")
        repo = Path(out.stdout.strip())

    try:
        preflight(repo)

        info(f"Release ZIP : {zip_path}")
        if args.dry_run:
            info("Mode        : DRY-RUN (no writes / commit / push)")
        else:
            info("Mode        : APPLY + commit + push")
        info("")

        # Unzip to a private temp dir.
        staging = Path(tempfile.mkdtemp(prefix="vrims-release-"))
        try:
            with zipfile.ZipFile(zip_path) as zf:
                zf.extractall(staging)

            content, commit_msg_inzip = inspect_zip(zip_path)
            if not content:
                return _fail("Zip contains no content files.")

            info(f"Found {len(content)} content file(s) in the release.")
            if commit_msg_inzip:
                good(f"commit-message.txt found (in-zip: {commit_msg_inzip})")
            else:
                if args.dry_run:
                    warn("no commit-message.txt in zip (dry-run continues)")
                else:
                    return _fail(
                        "No commit-message.txt in zip — cannot satisfy the "
                        "verbatim-commit-message rule. Re-run with --dry-run to preview."
                    )

            # --- validation gates ---
            validate_paths(content)
            good("Path-safety check passed.")

            rows = classify(content, repo)
            info("")
            info("Files to apply:")
            info(f"  {'STATUS':<10} {'PATH'}")
            info(f"  {'-'*10} {'-'*48}")
            n_new = n_over = 0
            for rel, status in rows:
                tag = "NEW" if status == "NEW" else "OVERWRITE"
                info(f"  {tag:<10} {rel}")
                if status == "NEW":
                    n_new += 1
                else:
                    n_over += 1
            info("")
            info(f"Summary: {n_new} new, {n_over} overwrite")
            if n_over:
                warn(f"{n_over} file(s) will be OVERWRITTEN.")
            info("")

            if args.dry_run:
                info("Dry-run complete — no changes made.")
                return 0

            # --- APPLY ---
            copy_in(staging, content, repo)
            good(f"Copied {len(content)} file(s) into {repo}.")

            # Stage only the release paths (never `git add -A`).
            run_git(repo, "add", "--", *content)
            good("Staged release files (targeted add).")

            # Show what's staged before committing (Rule 5).
            staged = run_git(repo, "diff", "--cached", "--name-status")
            info("")
            info("Staged changes (git diff --cached --name-status):")
            for line in staged.splitlines():
                info(f"  {line}")

            # Confirm no .DS_Store sneaked in.
            ds = [
                f for f in staged.splitlines()
                if ".DS_Store" in f
            ]
            if ds:
                return _fail(f".DS_Store got staged unexpectedly: {ds}")
            good("No .DS_Store staged.")

            # Commit with the verbatim commit message.
            if commit_msg_inzip:
                msg_file = staging / commit_msg_inzip
                run_git(repo, "commit", "-F", str(msg_file))
            else:
                # Defensive: dry-run already aborted this case, but be explicit.
                return _fail("Internal error: no commit message available.")

            commit_hash = run_git(repo, "rev-parse", "HEAD")
            short = commit_hash[:7]
            good(f"Committed: {short}")

            # PUSH STEP — pushes automatically. To gate behind a prompt, add:
            #   if input(f"Push {short} to origin? [y/N] ").strip().lower() != "y":
            #       info("Push skipped by user."); return 0
            branch = run_git(repo, "rev-parse", "--abbrev-ref", "HEAD")
            info("")
            info(f"Pushing to origin {branch} ...")
            push_out = subprocess.run(
                ["git", "-C", str(repo), "push", "origin", "HEAD"],
                capture_output=True, text=True,
            )
            if push_out.returncode != 0:
                info(push_out.stdout)
                return _fail(f"git push failed:\n{push_out.stderr.strip()}")
            info(push_out.stdout.strip())

            # Final report.
            info("")
            info("=" * 60)
            good(f"Done. Commit: {commit_hash}")
            info(f"Short hash: {short}")
            info("")
            show = run_git(repo, "show", "--stat", "--oneline", "HEAD")
            info(show)
            return 0
        finally:
            shutil.rmtree(staging, ignore_errors=True)
    except ReleaseError as e:
        return _fail(str(e))
    except subprocess.CalledProcessError as e:
        return _fail(f"Command failed: {e}")


def _fail(msg):
    print(f"\n❌ {msg}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
