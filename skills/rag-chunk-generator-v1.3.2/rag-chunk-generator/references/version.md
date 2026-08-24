# Version History

This file is the progressive-disclosure changelog for `rag-chunk-generator`.
`SKILL.md` describes only the current release. `FROZEN.md` remains the
normative ledger for immutable output and metadata contracts.

## Current Release

### v1.3.2, 2026-08-24

Status: final. Promoted from the independently accepted v1.3.2-dev source
after static, security, runtime fixture, package, and ZIP acceptance gates.
The frozen chunk and delivery contract is unchanged.

Changes from v1.3.1-dev:

- Added progressive-disclosure HTML and XML work specifications in `SKILL.md`
  and `references/html-xml.md`.
- Added an explicit HTML document/article tool matrix, local-file boundary,
  strict BOM／charset decoding, and converted-line locator semantics.
- Added XML safe-parser resource limits, DOCTYPE／ENTITY rejection,
  namespace-aware Clark locators, namespaced attributes, sibling indexes, and
  mixed-content ordering.
- Added HTML and XML fixtures plus positive and negative regression tests.
- Kept the existing `.md`／`.zip` delivery, v1.0 metadata, chunk defaults,
  quality warning behavior, and no chunk-isolation output tree.
- Final package acceptance re-ran the source tree and an independently
  extracted ZIP. HTML document, HTML article, XML safe, and XML MarkItDown
  fallback routes produced validated `.md`／`.zip` artifacts.

Research boundary: HtmlRAG and XML-aware chunking references support preserving
structure as a useful design direction. They do not prove a universal accuracy
gain for this adapter, so no retrieval-quality percentage is claimed here.

### v1.3.1-dev, 2026-08-24

Status: candidate. The original v1.0 delivery names and metadata fields remain
unchanged.

Changes from v1.3.0-dev:

- Added optional `--pdf_backend marker` using the lazy `marker-pdf` dependency
  and an explicit `--disable_ocr` pure text-layer route.
- Added Marker pagination and source-locator parsing without changing chunk
  schema or delivery filenames.
- Changed quality warnings from default hard stop to `quality_status: REVIEW`
  plus console diagnostics. The original Markdown and ZIP are still rendered.
- Added `--strict_quality` for callers that explicitly need a hard quality gate.
- Kept Docling as the default PDF backend, pdfplumber as explicit legacy, and
  Marker as an explicit optional text-layer comparison route.
- Moved historical release notes out of `SKILL.md` into this file.

Runtime note: the isolated Windows runtime installed `marker-pdf` and the
packaged candidate completed a Marker `--disable_ocr` smoke test. No OCR
server is part of this skill route. Marker remains an explicit optional
text-layer comparison adapter and does not replace the Docling default.

## Previous Releases

### v1.3.0-dev, 2026-08-24

- Docling became the default PDF adapter and requires page provenance.
- MarkItDown became the default DOCX adapter with a DOCX conversion smoke test.
- Added HTML document and article routes, plus safe lxml XML parsing.
- Added source locator, extraction backend, block type, and quality status
  metadata.
- Added lazy dependency installation and artifact-binding validation.
- The first candidate used a hard quality stop; v1.3.1-dev changes this to a
  warning by default to preserve the original delivery behavior.

### v1.2, 2026-08-21

- Replaced the vacuous token self-recalculation check with a contract-range
  check and kept v1.0 and v1.1 frozen fields unchanged.

### v1.1, 2026-07-20

- Added PDF text preprocessing, radical normalization, footer filtering,
  heading tracking, offline token encoding, and extractive summary fallback.
- Fixed direct script imports and kept the v1.0 contract unchanged.

### v1.0, frozen

- Initial PDF, DOCX, and MP4 chunking skill.
- Frozen delivery: `{stem}_chunks.md` and `{stem}_chunks.zip`.
- Frozen defaults: `chunk_size=256`, `overlap=40`, `min_len=30`.
- Frozen metadata and LlamaIndex／LangChain compatibility fields.

## Compatibility Policy

- Do not remove v1.0 metadata fields.
- Do not rename or remove the two delivery files.
- New adapters and optional metadata are added only in a new version.
- A backend choice never changes chunk schema or output filenames.
- A quality warning does not create a second output tree. Strict stopping is
  opt-in through `--strict_quality`.
