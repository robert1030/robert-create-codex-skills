"""rag-chunk-generator v1.3 主入口。"""
import argparse
import json
import sys
from pathlib import Path

# 確保 scripts/ 在 path 內
sys.path.insert(0, str(Path(__file__).parent))
import bootstrap


def detect_format(path: Path) -> str:
    ext = path.suffix.lower()
    if ext == ".pdf":
        return "pdf"
    elif ext == ".docx":
        return "docx"
    elif ext in {".html", ".htm"}:
        return "html"
    elif ext == ".xml":
        return "xml"
    elif ext == ".mp4":
        return "mp4"
    else:
        return "unknown"


def main():
    parser = argparse.ArgumentParser(description="高細緻度 RAG 切片產生器")
    parser.add_argument("--input", required=True, help="輸入檔案路徑（PDF／DOCX／HTML／XML／MP4）")
    parser.add_argument("--chunk_size", type=int, default=256)
    parser.add_argument("--overlap", type=int, default=40)
    parser.add_argument("--min_len", type=int, default=30)
    parser.add_argument("--summary_lang", default="auto", choices=["auto", "zh", "en"])
    parser.add_argument("--summary_mode", default="extractive", choices=["extractive", "api"])
    parser.add_argument("--whisper_model", default="base", choices=["tiny", "base", "small", "medium", "large"])
    parser.add_argument("--pdf_backend", default="docling", choices=["docling", "marker", "legacy"])
    parser.add_argument("--marker_page_range", default=None)
    parser.add_argument("--docx_backend", default="markitdown", choices=["markitdown", "legacy"])
    parser.add_argument("--html_mode", default="document", choices=["document", "article"])
    parser.add_argument("--xml_backend", default="safe", choices=["safe", "markitdown"])
    parser.add_argument(
        "--quality_anchor",
        action="append",
        default=[],
        help="要求正文必須包含的精確文字，可重複指定；用於已知關鍵詞／句子的品質驗證",
    )
    parser.add_argument(
        "--strict_quality",
        action="store_true",
        help="品質閘門未通過時停止；預設只警告並依原契約輸出",
    )
    parser.add_argument("--skip_summary", action="store_true")
    parser.add_argument("--output_dir", default="/home/claude/output")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"[錯誤] 找不到檔案：{input_path}", file=sys.stderr)
        sys.exit(1)

    fmt = detect_format(input_path)
    if fmt == "unknown":
        print(
            f"[錯誤] 不支援的格式：{input_path.suffix}（支援 .pdf / .docx / .html / .xml / .mp4）",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"[run_chunker] 格式：{fmt.upper()}｜chunk_size={args.chunk_size}｜overlap={args.overlap}｜min_len={args.min_len}")
    if args.chunk_size <= 0:
        parser.error("--chunk_size 必須大於 0")
    if args.overlap < 0:
        parser.error("--overlap 不可小於 0")
    if args.min_len < 0:
        parser.error("--min_len 不可小於 0")
    bootstrap.ensure_tiktoken()

    # 切片
    params = {
        "chunk_size": args.chunk_size,
        "overlap": args.overlap,
        "min_len": args.min_len,
    }

    extraction_backend = "unknown"
    require_locator = False

    if fmt == "pdf" and args.pdf_backend == "docling":
        from chunk_pdf_docling import chunk_pdf_docling
        chunks = chunk_pdf_docling(input_path, **params)
        extraction_backend = "docling"
        require_locator = True

    elif fmt == "pdf" and args.pdf_backend == "marker":
        from chunk_pdf_marker import chunk_pdf_marker
        chunks = chunk_pdf_marker(
            input_path,
            page_range=args.marker_page_range,
            **params,
        )
        extraction_backend = "marker"
        require_locator = True

    elif fmt == "pdf":
        print("[run_chunker] 警告：使用 pdfplumber legacy diagnostic route。", file=sys.stderr)
        bootstrap.ensure_pdf()
        from chunk_pdf import chunk_pdf
        chunks = chunk_pdf(input_path, **params)
        extraction_backend = "pdfplumber-legacy"

    elif fmt == "docx" and args.docx_backend == "markitdown":
        from chunk_markup import chunk_markup
        chunks = chunk_markup(input_path, file_type="docx", **params)
        extraction_backend = "markitdown"
        require_locator = True

    elif fmt == "docx":
        print("[run_chunker] 警告：使用 python-docx legacy compatibility route。", file=sys.stderr)
        bootstrap.ensure_docx()
        from chunk_docx import chunk_docx
        chunks = chunk_docx(input_path, **params)
        extraction_backend = "python-docx-legacy"

    elif fmt in {"html", "xml"}:
        from chunk_markup import chunk_markup
        chunks = chunk_markup(
            input_path,
            file_type=fmt,
            html_mode=args.html_mode,
            xml_backend=args.xml_backend,
            **params,
        )
        extraction_backend = chunks[0].get("extraction_backend", "unknown") if chunks else "unknown"
        require_locator = True

    elif fmt == "mp4":
        bootstrap.ensure_mp4()
        from chunk_mp4 import chunk_mp4
        chunks = chunk_mp4(input_path, whisper_model=args.whisper_model, **params)
        extraction_backend = "whisper"

    from quality_gate import annotate_chunks
    try:
        quality_errors = annotate_chunks(
            chunks,
            extraction_backend=extraction_backend,
            require_locator=require_locator,
            anchors=args.quality_anchor,
            strict=args.strict_quality,
        )
    except RuntimeError as exc:
        print(f"[run_chunker] {exc}", file=sys.stderr)
        sys.exit(1)

    if quality_errors:
        print(f"[run_chunker] 品質狀態：REVIEW，已保留原本 md／zip 交付契約。", file=sys.stderr)

    print(f"[run_chunker] 切片完成：{len(chunks)} 個切片")

    # Summary 生成
    from generate_summary import generate_summaries
    chunks = generate_summaries(
        chunks,
        lang=args.summary_lang,
        mode=args.summary_mode,
        skip=args.skip_summary,
    )

    # 暫存 chunks JSON
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    tmp_json = output_dir / f"{input_path.stem}_chunks_tmp.json"
    tmp_json.write_text(json.dumps(chunks, ensure_ascii=False, indent=2), encoding="utf-8")

    # Render MD ＋ ZIP
    from render_md import render
    md_path, zip_path = render(chunks, output_dir, input_path.stem, params)
    print(f"[run_chunker] 單檔：{md_path}")
    print(f"[run_chunker] ZIP：{zip_path}")

    # 驗證
    import subprocess
    validation_command = [
        sys.executable, str(Path(__file__).parent / "validate_output.py"),
        "--chunks_json", str(tmp_json),
        "--md_path", str(md_path),
        "--zip_path", str(zip_path),
        "--chunk_size", str(args.chunk_size),
        "--overlap", str(args.overlap),
        "--min_len", str(args.min_len),
    ]
    if args.strict_quality:
        validation_command.append("--strict_quality")
    result = subprocess.run(validation_command, capture_output=False)
    if result.returncode != 0:
        print("[run_chunker] 驗證未通過，請檢查上方錯誤訊息。", file=sys.stderr)
        sys.exit(1)

    print("[run_chunker] 全部完成，可交付。")
    return md_path, zip_path


if __name__ == "__main__":
    main()
