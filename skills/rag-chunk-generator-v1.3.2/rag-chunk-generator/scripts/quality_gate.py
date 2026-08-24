"""Deterministic extraction quality gate for v1.3 adapters."""
import re
from typing import Iterable


# These compatibility punctuation characters are a known source of visually
# correct but retrieval-incorrect PDF text.  They are intentionally flagged.
SUSPICIOUS_GLYPHS = {
    "\ufffd",  # replacement character
    "\ufe41", "\ufe42", "\ufe43", "\ufe44", "\ufe45", "\ufe46",
    "\ufe47", "\ufe48", "\ufe49", "\ufe4a", "\ufe4b", "\ufe4c",
    "\ufe4d", "\ufe4e", "\ufe4f", "\ufb00", "\ufb01", "\ufb02",
    "\ufb03", "\ufb04", "\ufb05", "\ufb06",
}
_PRIVATE_USE_RE = re.compile(r"[\ue000-\uf8ff]")


def _all_text(chunks: list[dict]) -> str:
    return "\n".join(str(c.get("text", "")) for c in chunks)


def validate_chunks(
    chunks: list[dict],
    require_locator: bool = False,
    anchors: Iterable[str] = (),
) -> list[str]:
    """Return hard quality failures.  An empty list is a quality PASS."""
    errors: list[str] = []
    if not chunks:
        return ["沒有產生任何切片"]
    for chunk in chunks:
        chunk_id = chunk.get("chunk_id", "<unknown>")
        text = str(chunk.get("text", ""))
        if not text.strip():
            errors.append(f"空切片：{chunk_id}")
        if require_locator and not str(chunk.get("source_locator", "")).strip():
            errors.append(f"缺少來源定位：{chunk_id}")
        bad = sorted({ch for ch in text if ch in SUSPICIOUS_GLYPHS})
        if bad:
            codepoints = ", ".join(f"U+{ord(ch):04X}" for ch in bad)
            errors.append(f"疑似字型／編碼異常：{chunk_id}（{codepoints}）")
        if _PRIVATE_USE_RE.search(text):
            errors.append(f"含 Private Use Area 字元：{chunk_id}")

    text = _all_text(chunks)
    for anchor in anchors:
        if anchor and anchor not in text:
            errors.append(f"找不到品質錨點：{anchor}")
    return errors


def annotate_chunks(
    chunks: list[dict],
    extraction_backend: str,
    require_locator: bool = False,
    anchors: Iterable[str] = (),
    strict: bool = False,
) -> list[str]:
    errors = validate_chunks(chunks, require_locator=require_locator, anchors=anchors)
    status = "REVIEW" if errors else "PASS"
    for chunk in chunks:
        chunk["extraction_backend"] = chunk.get("extraction_backend") or extraction_backend
        chunk["quality_status"] = status
    if errors:
        print(f"[quality_gate] REVIEW｜{len(errors)} 個問題，仍依原契約輸出：")
        for error in errors:
            print(f"  {error}")
        if strict:
            raise RuntimeError("抽取品質閘門未通過，因 --strict_quality 停止輸出")
    return errors


def annotate_or_raise(
    chunks: list[dict],
    extraction_backend: str,
    require_locator: bool = False,
    anchors: Iterable[str] = (),
) -> None:
    """Backward-compatible strict wrapper for callers that require a hard gate."""
    annotate_chunks(
        chunks,
        extraction_backend=extraction_backend,
        require_locator=require_locator,
        anchors=anchors,
        strict=True,
    )
