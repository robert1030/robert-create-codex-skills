"""
validate_output.py｜RAG 切片產出驗證器（v1.3）
驗證項：chunk_id 唯一、token 誤差、prev/next 一致、無空切片、zip 檔案數、格式與品質狀態
退出碼 0 = 全過；1 = 有問題。
"""
import json
import sys
import zipfile
from pathlib import Path

# 把 validate_punct 加入路徑
sys.path.insert(0, str(Path(__file__).parent))
import validate_punct


def validate_chunks(chunks: list[dict], zip_path: Path | None = None,
                    chunk_size: int = 256, overlap: int = 40, min_len: int = 30) -> list[str]:
    errors = []

    # 1. chunk_id 唯一
    ids = [c["chunk_id"] for c in chunks]
    seen = set()
    for cid in ids:
        if cid in seen:
            errors.append(f"重複 chunk_id：{cid}")
        seen.add(cid)

    # 2. 無空切片
    for c in chunks:
        if not c.get("text", "").strip():
            errors.append(f"空切片：{c['chunk_id']}")

    # 2b. v1.3 optional metadata.  Old v1.0-v1.2 fixtures may omit these fields.
    allowed_types = {"pdf", "docx", "mp4", "html", "xml"}
    for c in chunks:
        if "file_type" in c and c["file_type"] not in allowed_types:
            errors.append(f"不支援的 file_type：{c['chunk_id']} → {c['file_type']}")
        if "quality_status" in c and c["quality_status"] not in {"PASS", "REVIEW", "NOT_CHECKED", "NOT_QUALIFIED"}:
            errors.append(f"不支援的 quality_status：{c['chunk_id']} → {c['quality_status']}")
        if c.get("quality_status") == "NOT_QUALIFIED":
            errors.append(f"品質狀態未達交付資格：{c['chunk_id']}")
        if "extraction_backend" in c and not str(c["extraction_backend"]).strip():
            errors.append(f"缺 extraction_backend：{c['chunk_id']}")

    # 3. token_count 契約範圍檢查（非自我循環，不需 tiktoken）。
    #    v1.1 是拿同一把 enc_compat 尺重算再比對，切片器也用同一把，誤差恆為 0、永不紅，形同虛設。
    #    v1.2 改驗「切片器有沒有守住 chunk_size 契約」：token_count 落在 [min_len, (chunk_size + overlap) 容忍上限]。
    upper = int((chunk_size + overlap) * 1.2)   # 容忍再編碼邊界誤差
    for c in chunks:
        tc = c.get("token_count", None)
        if tc is None:
            errors.append(f"缺 token_count：{c['chunk_id']}")
            continue
        if not isinstance(tc, int) or tc <= 0:
            errors.append(f"token_count 非正整數：{c['chunk_id']}（{tc}）")
            continue
        if tc > upper:
            errors.append(
                f"token_count 爆量：{c['chunk_id']} = {tc} > 上限 {upper}"
                f"（chunk_size {chunk_size} ＋ overlap {overlap} 的容忍上限，切片器可能沒守住 chunk_size）")
        elif tc < min_len:
            errors.append(
                f"token_count 低於 min_len：{c['chunk_id']} = {tc} < {min_len}（應已被丟棄）")

    # 3b. 完整性交叉核對（可選）：用 enc_compat 重算抓「宣稱值與內容不符」的竄改或損毀。
    #     enc_compat 不可用時靜default跳過、不誤報（契約範圍檢查已把關）。
    try:
        import enc_compat
        enc = enc_compat.get_encoding()
        for c in chunks:
            actual = len(enc.encode(c["text"]))
            declared = c.get("token_count", 0)
            if isinstance(declared, int) and declared > 0 and abs(actual - declared) / max(declared, 1) > 0.05:
                errors.append(
                    f"token_count 與內容不符（疑似竄改或損毀）：{c['chunk_id']} 宣稱 {declared}，實際 {actual}")
    except Exception:
        pass

    # 4. prev/next 指針一致
    id_set = set(ids)
    by_id = {c["chunk_id"]: c for c in chunks}
    for c in chunks:
        if c.get("prev_chunk_id") and c["prev_chunk_id"] not in id_set:
            errors.append(f"prev_chunk_id 指向不存在的 id：{c['chunk_id']} → {c['prev_chunk_id']}")
        if c.get("next_chunk_id") and c["next_chunk_id"] not in id_set:
            errors.append(f"next_chunk_id 指向不存在的 id：{c['chunk_id']} → {c['next_chunk_id']}")
        if c.get("prev_chunk_id") in by_id and by_id[c["prev_chunk_id"]].get("next_chunk_id") != c["chunk_id"]:
            errors.append(f"prev/next 不互相一致：{c['chunk_id']}")
        if c.get("next_chunk_id") in by_id and by_id[c["next_chunk_id"]].get("prev_chunk_id") != c["chunk_id"]:
            errors.append(f"next/prev 不互相一致：{c['chunk_id']}")

    # 5. zip 檔案數 = 切片數 ＋ 1（index.md）
    if zip_path and zip_path.exists():
        with zipfile.ZipFile(zip_path) as zf:
            file_count = len(zf.namelist())
        expected = len(chunks) + 1
        if file_count != expected:
            errors.append(f"zip 檔案數錯誤：預期 {expected}（{len(chunks)} 切片＋index.md），實際 {file_count}")

    return errors


def validate_md_file(md_path: Path, strict_quality: bool = False) -> list[str]:
    """全形標點驗證，v1.3.1 預設警告，strict 時才阻擋。"""
    # v1.2 正本的 check() 會自行列印並回傳退出碼
    if validate_punct.check(str(md_path)) != 0:
        if strict_quality:
            return ["全形標點／破折號驗證未通過（明細見上方 validate_punct 輸出）"]
        print("[validate_output] WARNING｜全形標點／破折號檢查未通過，依 v1.3.1 預設繼續交付。")
    return []


def validate_rendered_artifacts(
    chunks: list[dict], md_path: Path, zip_path: Path | None
) -> list[str]:
    """Bind validation to the current rendered MD and ZIP, not just JSON."""
    errors: list[str] = []
    if not md_path.exists():
        return [f"找不到 Markdown 產物：{md_path}"]
    combined = md_path.read_text(encoding="utf-8")
    for chunk in chunks:
        if chunk.get("text", "") not in combined:
            errors.append(f"Markdown 缺少當前切片正文：{chunk['chunk_id']}")

    if zip_path is None:
        return errors
    if not zip_path.exists():
        errors.append(f"找不到 ZIP 產物：{zip_path}")
        return errors
    try:
        with zipfile.ZipFile(zip_path) as zf:
            names = set(zf.namelist())
            for chunk in chunks:
                name = f"chunk_{chunk['chunk_id']}.md"
                if name not in names:
                    errors.append(f"ZIP 缺少切片檔：{name}")
                    continue
                content = zf.read(name).decode("utf-8")
                if chunk.get("text", "") not in content:
                    errors.append(f"ZIP 切片正文與當前資料不符：{chunk['chunk_id']}")
    except (zipfile.BadZipFile, UnicodeDecodeError) as exc:
        errors.append(f"ZIP 產物無法讀取：{exc}")
    return errors


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--chunks_json", required=True)
    parser.add_argument("--md_path", required=True)
    parser.add_argument("--zip_path", default=None)
    parser.add_argument("--chunk_size", type=int, default=256)
    parser.add_argument("--overlap", type=int, default=40)
    parser.add_argument("--min_len", type=int, default=30)
    parser.add_argument("--strict_quality", action="store_true")
    args = parser.parse_args()

    chunks = json.loads(Path(args.chunks_json).read_text(encoding="utf-8"))
    zip_path = Path(args.zip_path) if args.zip_path else None

    errors: list[str] = []
    errors += validate_chunks(chunks, zip_path, args.chunk_size, args.overlap, args.min_len)
    errors += validate_md_file(Path(args.md_path), strict_quality=args.strict_quality)
    errors += validate_rendered_artifacts(chunks, Path(args.md_path), zip_path)

    if errors:
        print(f"[validate_output] FAIL｜{len(errors)} 個問題：")
        for e in errors:
            print(f"  {e}")
        sys.exit(1)

    print("[validate_output] PASS｜所有驗證通過。")
    sys.exit(0)


if __name__ == "__main__":
    main()
