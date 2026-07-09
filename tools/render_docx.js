// VRIMS Document Renderer — Node/docx-js generator.
// Reads a JSON payload from render_docs.py and generates a .docx file.
// Payload: { document_id, title, level, level_label, audience, target_pages, sections[], missing_files[], output_path }

const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  PageBreak, Header, Footer, PageNumber, NumberFormat,
  AlignmentType, HeadingLevel, WidthType, BorderStyle, ShadingType,
  PageOrientation, TableLayoutType, TableOfContents, LevelFormat,
} = require("docx");
const fs = require("fs");

// ── DS-1 palette (Deep Sea) ──────────────────────────────────────────────────
const P = {
  bg: "0B1C2C", primary: "FFFFFF", accent: "529286",
  cover: { titleColor: "FFFFFF", subtitleColor: "B0B8C0", metaColor: "90989F", footerColor: "687078" },
  table: { headerBg: "529286", headerText: "FFFFFF", accentLine: "529286", innerLine: "BECFCC", surface: "E8ECEB" },
  body: "1A2330",
};
const c = (hex) => hex.replace("#", "");
const NB = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: NB, bottom: NB, left: NB, right: NB };
const allNoBorders = { ...noBorders, insideHorizontal: NB, insideVertical: NB };
const FONT = { ascii: "Calibri", eastAsia: "Times New Roman" };
const FONT_HEADING = { ascii: "Calibri", eastAsia: "SimHei" };
const FONT_MONO = { ascii: "Menlo", eastAsia: "Menlo" };

// ── Payload ──────────────────────────────────────────────────────────────────
const payloadPath = process.argv[2];
if (!payloadPath) { console.error("Usage: node render_docx.js <payload.json>"); process.exit(1); }
const payload = JSON.parse(fs.readFileSync(payloadPath, "utf8"));

// ── Markdown rendering helpers ───────────────────────────────────────────────
function splitTitleLines(title, charsPerLine) {
  if (title.length <= charsPerLine) return [title];
  const breakAfter = new Set([..." \t-_/—–·"]);
  const lines = [];
  let remaining = title;
  while (remaining.length > charsPerLine) {
    let breakAt = -1;
    for (let i = charsPerLine; i >= Math.floor(charsPerLine * 0.6); i--) {
      if (i < remaining.length && breakAfter.has(remaining[i - 1])) { breakAt = i; break; }
    }
    if (breakAt === -1) {
      const limit = Math.min(remaining.length, Math.ceil(charsPerLine * 1.3));
      for (let i = charsPerLine + 1; i < limit; i++) {
        if (breakAfter.has(remaining[i - 1])) { breakAt = i; break; }
      }
    }
    if (breakAt === -1) breakAt = charsPerLine;
    lines.push(remaining.slice(0, breakAt).trim());
    remaining = remaining.slice(breakAt).trim();
  }
  if (remaining) lines.push(remaining);
  return lines;
}

function parseInlineMarkdown(text) {
  const runs = [];
  let remaining = text;
  while (remaining.length > 0) {
    let boldMatch = remaining.match(/^(.*?)\*\*(.+?)\*\*/s);
    let codeMatch = remaining.match(/^(.*?)`(.+?)`/s);
    if (boldMatch && (!codeMatch || boldMatch[1].length <= codeMatch[1].length)) {
      if (boldMatch[1]) runs.push(new TextRun({ text: boldMatch[1], size: 24, color: c(P.body), font: FONT }));
      runs.push(new TextRun({ text: boldMatch[2], bold: true, size: 24, color: c(P.body), font: FONT }));
      remaining = remaining.slice(boldMatch[0].length);
    } else if (codeMatch) {
      if (codeMatch[1]) runs.push(new TextRun({ text: codeMatch[1], size: 24, color: c(P.body), font: FONT }));
      runs.push(new TextRun({ text: codeMatch[2], font: FONT_MONO, size: 21, color: "C0392B" }));
      remaining = remaining.slice(codeMatch[0].length);
    } else {
      runs.push(new TextRun({ text: remaining, size: 24, color: c(P.body), font: FONT }));
      remaining = "";
    }
  }
  return runs.length ? runs : [new TextRun({ text: " ", size: 24 })];
}

function parseTableRow(line) {
  const cells = line.split("|").map(s => s.trim());
  // Remove empty first/last from leading/trailing pipes
  if (cells[0] === "") cells.shift();
  if (cells[cells.length - 1] === "") cells.pop();
  return cells;
}

function buildTable(rows) {
  if (!rows.length) return new Paragraph({ children: [] });
  const colCount = rows[0].length;
  const colWidth = Math.floor(100 / colCount);
  const tableRows = rows.map((row, rowIdx) => {
    const isHeader = rowIdx === 0;
    const cells = row.map(cellText => new TableCell({
      children: [new Paragraph({
        spacing: { line: 276 },
        children: [new TextRun({
          text: cellText, bold: isHeader, size: isHeader ? 22 : 21,
          color: isHeader ? c(P.table.headerText) : c(P.body), font: FONT,
        })],
      })],
      shading: { type: ShadingType.CLEAR, fill: isHeader ? P.table.headerBg : "FFFFFF" },
      margins: { top: 60, bottom: 60, left: 120, right: 120 },
      width: { size: colWidth, type: WidthType.PERCENTAGE },
    }));
    return new TableRow({ tableHeader: isHeader, cantSplit: true, children: cells });
  });
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    layout: TableLayoutType.FIXED,
    borders: {
      top: { style: BorderStyle.SINGLE, size: 2, color: P.table.accentLine },
      bottom: { style: BorderStyle.SINGLE, size: 2, color: P.table.accentLine },
      left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 1, color: P.table.innerLine },
      insideVertical: { style: BorderStyle.NONE },
    },
    rows: tableRows,
  });
}

function renderMarkdown(mdText) {
  const elements = [];
  const lines = mdText.split("\n");
  let i = 0;
  // Skip YAML front matter
  if (lines[0] && lines[0].trim() === "---") {
    i = 1;
    while (i < lines.length && lines[i].trim() !== "---") i++;
    i++;
  }
  while (i < lines.length) {
    let line = lines[i];
    // Code block
    if (line.trim().startsWith("```")) {
      const codeLines = [];
      i++;
      while (i < lines.length && !lines[i].trim().startsWith("```")) { codeLines.push(lines[i]); i++; }
      i++;
      for (const cl of codeLines) {
        elements.push(new Paragraph({
          spacing: { line: 276, before: 0, after: 0 },
          shading: { type: ShadingType.CLEAR, fill: "F4F6F8" },
          indent: { left: 200 },
          children: [new TextRun({ text: cl || " ", font: FONT_MONO, size: 20, color: "2A3A4A" })],
        }));
      }
      elements.push(new Paragraph({ spacing: { after: 100 }, children: [] }));
      continue;
    }
    // Table
    if (line.includes("|") && i + 1 < lines.length && /^\s*\|?[\s\-:|]+\|?\s*$/.test(lines[i + 1])) {
      const tableRows = [parseTableRow(line)];
      i += 2;
      while (i < lines.length && lines[i].includes("|")) { tableRows.push(parseTableRow(lines[i])); i++; }
      elements.push(buildTable(tableRows));
      continue;
    }
    // Heading
    const headingMatch = line.match(/^(#{1,6})\s+(.+)$/);
    if (headingMatch) {
      const level = headingMatch[1].length;
      const text = headingMatch[2].trim();
      // Remap: H1 stays H1 (it's the source doc title), H2→H2, etc.
      // But if this is a source title (H1), make it H2 since the Part header is H1
      const docxLevel = level === 1 ? 2 : Math.min(level, 4);
      elements.push(new Paragraph({
        heading: [null, HeadingLevel.HEADING_1, HeadingLevel.HEADING_2, HeadingLevel.HEADING_3, HeadingLevel.HEADING_4][docxLevel],
        spacing: { before: docxLevel <= 2 ? 300 : 240, after: 120, line: 312 },
        children: [new TextRun({ text, bold: true, color: c(P.body), font: FONT_HEADING })],
      }));
      i++;
      continue;
    }
    // Bullet list
    if (/^\s*[-*]\s+/.test(line)) {
      const text = line.replace(/^\s*[-*]\s+/, "");
      const indentLevel = Math.floor((line.match(/^ */)[0].length) / 2);
      elements.push(new Paragraph({
        bullet: { level: Math.min(indentLevel, 2) },
        spacing: { line: 312, after: 40 },
        children: parseInlineMarkdown(text),
      }));
      i++;
      continue;
    }
    // Numbered list
    if (/^\s*\d+\.\s+/.test(line)) {
      const text = line.replace(/^\s*\d+\.\s+/, "");
      elements.push(new Paragraph({
        numbering: { reference: "md-numbered", level: 0 },
        spacing: { line: 312, after: 40 },
        children: parseInlineMarkdown(text),
      }));
      i++;
      continue;
    }
    // Empty line
    if (line.trim() === "") { i++; continue; }
    // Paragraph
    elements.push(new Paragraph({
      alignment: AlignmentType.JUSTIFIED,
      spacing: { line: 312, after: 80 },
      children: parseInlineMarkdown(line),
    }));
    i++;
  }
  return elements;
}

// ── Cover page ───────────────────────────────────────────────────────────────
function buildCover() {
  const padL = 1200, padR = 800;
  const title = payload.title || "VRIMS Document";
  const titleLines = splitTitleLines(title, 30);
  const titlePt = 32;
  const titleSize = titlePt * 2;
  const children = [];
  children.push(new Paragraph({ spacing: { before: 2400 } }));
  children.push(new Paragraph({
    indent: { left: padL, right: padR }, spacing: { after: 500 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: P.accent, space: 8 } },
    children: [new TextRun({ text: (payload.document_id || "VRIMS").split("").join("  "), size: 18, color: P.accent, font: FONT_HEADING, characterSpacing: 40 })],
  }));
  for (let i = 0; i < titleLines.length; i++) {
    children.push(new Paragraph({
      indent: { left: padL },
      spacing: { after: i < titleLines.length - 1 ? 100 : 300, line: Math.ceil(titlePt * 23), lineRule: "atLeast" },
      children: [new TextRun({ text: titleLines[i], size: titleSize, bold: true, color: P.cover.titleColor, font: FONT_HEADING })],
    }));
  }
  const levelLabel = payload.level_label || payload.level;
  children.push(new Paragraph({
    indent: { left: padL }, spacing: { after: 800 },
    children: [new TextRun({ text: `${payload.document_id || ""}  |  ${levelLabel}  |  Version 0.5R`, size: 24, color: P.cover.subtitleColor, font: FONT })],
  }));
  const accentLeft = { style: BorderStyle.SINGLE, size: 8, color: P.accent, space: 12 };
  const audience = Array.isArray(payload.audience) ? payload.audience.join(", ") : (payload.audience || "");
  const metaLines = [
    `Document ID: ${payload.document_id || ""}`,
    `Level: ${levelLabel}`,
    `Audience: ${audience}`,
    `Target Pages: ${payload.target_pages || "n/a"}`,
    `Date: 2026-07-09`,
  ];
  for (const line of metaLines) {
    children.push(new Paragraph({
      indent: { left: padL + 200 }, spacing: { after: 80 },
      border: { left: accentLeft },
      children: [new TextRun({ text: line, size: 24, color: P.cover.metaColor, font: FONT })],
    }));
  }
  children.push(new Paragraph({ spacing: { before: 3000 } }));
  children.push(new Paragraph({
    indent: { left: padL, right: padR },
    border: { top: { style: BorderStyle.SINGLE, size: 2, color: P.accent, space: 8 } },
    spacing: { before: 200 },
    children: [
      new TextRun({ text: "VRIMS Project", size: 16, color: P.cover.footerColor, font: FONT }),
      new TextRun({ text: "                                        " }),
      new TextRun({ text: "Generated from Markdown source — Review Version", size: 16, color: P.cover.footerColor, font: FONT }),
    ],
  }));
  return [new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    layout: TableLayoutType.FIXED,
    borders: allNoBorders,
    rows: [new TableRow({
      height: { value: 16838, rule: "exact" },
      children: [new TableCell({
        shading: { type: ShadingType.CLEAR, fill: P.bg }, borders: noBorders, children,
      })],
    })],
  })];
}

// ── TOC + Document Control ──────────────────────────────────────────────────
function buildFrontMatter() {
  const els = [];
  els.push(new Paragraph({
    spacing: { before: 200, after: 300 },
    children: [new TextRun({ text: "Table of Contents", bold: true, size: 36, color: c(P.body), font: FONT_HEADING })],
  }));
  els.push(new TableOfContents("Table of Contents", { hyperlink: true, headingStyleRange: "1-3" }));
  els.push(new Paragraph({
    spacing: { before: 200 },
    children: [new TextRun({ text: "Right-click the table above and select \u201cUpdate Field\u201d to refresh page numbers.", italics: true, size: 20, color: "888888", font: FONT })],
  }));
  // Document control on new page
  els.push(new Paragraph({
    heading: HeadingLevel.HEADING_1, spacing: { before: 200, after: 200 },
    children: [new PageBreak(), new TextRun({ text: "Document Control", bold: true, color: c(P.body), font: FONT_HEADING })],
  }));
  const ctrlRows = [
    ["Field", "Value"],
    ["Document ID", payload.document_id || ""],
    ["Title", payload.title || ""],
    ["Level", payload.level_label || payload.level],
    ["Audience", Array.isArray(payload.audience) ? payload.audience.join(", ") : (payload.audience || "")],
    ["Target Pages", payload.target_pages || "n/a"],
    ["Version", "0.5R"],
    ["Status", "Review Version (not final sign-off)"],
    ["Source", "vrims-docs Markdown repository"],
    ["Date", "2026-07-09"],
  ];
  els.push(buildTable(ctrlRows));

  // Missing content report
  if (payload.missing_files && payload.missing_files.length > 0) {
    els.push(new Paragraph({
      heading: HeadingLevel.HEADING_2, spacing: { before: 300, after: 120 },
      children: [new TextRun({ text: "Missing Content Report", bold: true, color: "C0392B", font: FONT_HEADING })],
    }));
    els.push(new Paragraph({
      spacing: { line: 312, after: 80 },
      children: [new TextRun({ text: "The following source files are referenced in build-order.yaml but do not exist in the repository. Per render guide rule 6, missing content is reported rather than created.", size: 24, color: c(P.body), font: FONT })],
    }));
    for (const m of payload.missing_files) {
      els.push(new Paragraph({
        bullet: { level: 0 }, spacing: { line: 312, after: 40 },
        children: [new TextRun({ text: m, size: 24, color: "C0392B", font: FONT_MONO })],
      }));
    }
  }
  return els;
}

// ── Body content ────────────────────────────────────────────────────────────
function buildBody() {
  const els = [];
  let sectionIdx = 0;
  for (const sec of payload.sections) {
    sectionIdx++;
    // Part header
    els.push(new Paragraph({
      heading: HeadingLevel.HEADING_1, spacing: { before: 360, after: 200, line: 312 },
      children: [
        ...(sectionIdx > 1 ? [new PageBreak()] : []),
        new TextRun({ text: `Source: ${sec.source}`, bold: true, color: c(P.body), font: FONT_HEADING }),
      ],
    }));
    // Render the filtered markdown
    els.push(...renderMarkdown(sec.markdown));
  }
  return els;
}

// ── Assemble document ────────────────────────────────────────────────────────
const headerText = `${payload.document_id || "VRIMS"} ${payload.title || ""} — ${payload.level_label || payload.level}`;
const doc = new Document({
  creator: "VRIMS Render Tool",
  title: `${payload.document_id} ${payload.title} — ${payload.level}`,
  styles: {
    default: {
      document: {
        run: { font: FONT, size: 24, color: c(P.body) },
        paragraph: { spacing: { line: 312 } },
      },
      heading1: { run: { font: FONT_HEADING, size: 32, bold: true, color: c(P.body) }, paragraph: { spacing: { before: 360, after: 160, line: 312 } } },
      heading2: { run: { font: FONT_HEADING, size: 28, bold: true, color: c(P.body) }, paragraph: { spacing: { before: 240, after: 120, line: 312 } } },
      heading3: { run: { font: FONT_HEADING, size: 24, bold: true, color: c(P.body) }, paragraph: { spacing: { before: 200, after: 100, line: 312 } } },
    },
  },
  numbering: {
    config: [{
      reference: "md-numbered",
      levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }],
    }],
  },
  sections: [
    // Cover
    { properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 0, bottom: 0, left: 0, right: 0 } } }, children: buildCover() },
    // Front matter (TOC + control)
    {
      properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1440, bottom: 1440, left: 1701, right: 1417 }, pageNumbers: { start: 1, formatType: NumberFormat.LOWER_ROMAN } } },
      headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: headerText, size: 18, color: "888888", font: FONT })] })] }) },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], size: 18, color: "888888", font: FONT })] })] }) },
      children: buildFrontMatter(),
    },
    // Body
    {
      properties: { page: { size: { width: 11906, height: 16838 }, margin: { top: 1440, bottom: 1440, left: 1701, right: 1417 }, pageNumbers: { start: 1, formatType: NumberFormat.DECIMAL } } },
      headers: { default: new Header({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: headerText, size: 18, color: "888888", font: FONT })] })] }) },
      footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ children: [PageNumber.CURRENT], size: 18, color: "888888", font: FONT })] })] }) },
      children: buildBody(),
    },
  ],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(payload.output_path, buf);
  console.log(`✅ Node generator: wrote ${payload.output_path} (${(buf.length / 1024).toFixed(1)} KB)`);
});
