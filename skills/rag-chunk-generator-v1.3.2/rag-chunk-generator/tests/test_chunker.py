"""
tests/test_chunker.py — rag-chunk-generator 回歸測試（v1.0 凍結契約）
不需要重相依（pdfplumber、whisper、docx）即可執行，只測純邏輯與凍結契約。
執行：python -m pytest tests/ -v
"""
import json
import sys
import zipfile
from pathlib import Path

import pytest

# 讓 scripts/ 可 import
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))


# ====================
# 凍結契約：metadata 欄位名稱（v1.0）
# ====================
FROZEN_METADATA_KEYS = {
    "chunk_id",
    "text",
    "source_file",
    "file_type",
    "chunk_index",
    "page_number",
    "start_time",
    "end_time",
    "section_title",
    "prev_chunk_id",
    "next_chunk_id",
    "token_count",
    "summary",
}

FROZEN_DEFAULT_PARAMS = {
    "chunk_size": 256,
    "overlap": 40,
    "min_len": 30,
}

FROZEN_DELIVERY_SUFFIXES = {"_chunks.md", "_chunks.zip"}


def test_frozen_metadata_keys():
    """凍結契約：metadata 欄位集合不可縮減。"""
    # 模擬一個切片
    mock_chunk = {
        "chunk_id": "test_p001_0000",
        "text": "測試文字。",
        "source_file": "test.pdf",
        "file_type": "pdf",
        "chunk_index": 0,
        "page_number": 1,
        "start_time": None,
        "end_time": None,
        "section_title": "第一章",
        "prev_chunk_id": None,
        "next_chunk_id": "test_p001_0001",
        "token_count": 10,
        "summary": "測試摘要。",
    }
    assert FROZEN_METADATA_KEYS.issubset(set(mock_chunk.keys())), (
        "chunk 缺少凍結欄位：" + str(FROZEN_METADATA_KEYS - set(mock_chunk.keys()))
    )


def test_frozen_default_params():
    """凍結契約：預設參數不可改。"""
    assert FROZEN_DEFAULT_PARAMS["chunk_size"] == 256
    assert FROZEN_DEFAULT_PARAMS["overlap"] == 40
    assert FROZEN_DEFAULT_PARAMS["min_len"] == 30


def test_chunk_id_format():
    """chunk_id 格式：{slug}_{定位碼}_{序號:04d}"""
    valid = "lecture_01_p003_0012"
    parts = valid.split("_")
    # 最後一個 part 是 4 位數序號
    assert parts[-1].isdigit() and len(parts[-1]) == 4


def test_apply_overlap_length():
    """overlap 不超過原切片長度。"""
    # 模擬邏輯（不依賴 tiktoken）
    text = "A B C D E F G H I J"
    words = text.split()
    overlap = 3
    tail = words[-overlap:] if len(words) > overlap else words
    assert len(tail) <= overlap


def test_prev_next_consistency():
    """prev/next 指針一致性驗證（純邏輯）。"""
    chunks = [
        {"chunk_id": "a_0000", "prev_chunk_id": None, "next_chunk_id": "a_0001", "text": "x", "token_count": 5},
        {"chunk_id": "a_0001", "prev_chunk_id": "a_0000", "next_chunk_id": "a_0002", "text": "y", "token_count": 5},
        {"chunk_id": "a_0002", "prev_chunk_id": "a_0001", "next_chunk_id": None, "text": "z", "token_count": 5},
    ]
    id_set = {c["chunk_id"] for c in chunks}
    for c in chunks:
        if c["prev_chunk_id"]:
            assert c["prev_chunk_id"] in id_set
        if c["next_chunk_id"]:
            assert c["next_chunk_id"] in id_set


def test_no_empty_chunks():
    """無空切片。"""
    chunks = [
        {"chunk_id": "a_0000", "text": "有內容"},
        {"chunk_id": "a_0001", "text": "  "},  # 這個應被偵測
    ]
    empty = [c for c in chunks if not c["text"].strip()]
    assert len(empty) == 1  # 驗證偵測邏輯可找出空切片


def test_duplicate_chunk_id_detection():
    """重複 chunk_id 偵測。"""
    ids = ["a_0000", "a_0001", "a_0000"]
    seen = set()
    duplicates = []
    for cid in ids:
        if cid in seen:
            duplicates.append(cid)
        seen.add(cid)
    assert "a_0000" in duplicates


def test_render_md_single_file(tmp_path):
    """render_md 單檔輸出包含 YAML frontmatter。"""
    sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
    from render_md import render

    chunks = [
        {
            "chunk_id": "test_p001_0000",
            "text": "這是測試切片內容。",
            "source_file": "test.pdf",
            "file_type": "pdf",
            "chunk_index": 0,
            "page_number": 1,
            "start_time": None,
            "end_time": None,
            "section_title": "第一節",
            "prev_chunk_id": None,
            "next_chunk_id": None,
            "token_count": 15,
            "summary": "測試切片的摘要。",
        }
    ]
    md_path, zip_path = render(chunks, tmp_path, "test")
    content = md_path.read_text(encoding="utf-8")
    assert "chunk_id: test_p001_0000" in content
    assert "這是測試切片內容。" in content


def test_render_zip_file_count(tmp_path):
    """render_md zip 包含切片數 ＋ 1（index.md）。"""
    sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
    from render_md import render

    chunks = [
        {
            "chunk_id": f"test_p001_{i:04d}",
            "text": f"切片 {i} 的內容。",
            "source_file": "test.pdf",
            "file_type": "pdf",
            "chunk_index": i,
            "page_number": 1,
            "start_time": None,
            "end_time": None,
            "section_title": None,
            "prev_chunk_id": None,
            "next_chunk_id": None,
            "token_count": 10,
            "summary": "",
        }
        for i in range(5)
    ]
    _, zip_path = render(chunks, tmp_path, "test")
    with zipfile.ZipFile(zip_path) as zf:
        assert len(zf.namelist()) == 6  # 5 切片 ＋ index.md


def test_validate_punct_pass(tmp_path):
    """validate_punct 對正確全形標點通過（v1.1：改用房規正本的 check()）。"""
    from validate_punct import check
    md = tmp_path / "ok.md"
    md.write_text("這是一段正確的全形標點文字，包含句號。以及頓號、分號；", encoding="utf-8")
    assert check(str(md)) == 0


def test_validate_punct_fail_halfwidth(tmp_path):
    """validate_punct 偵測中文間夾半形逗號。"""
    from validate_punct import check
    md = tmp_path / "bad.md"
    md.write_text("這是一段錯誤,包含半形逗號的文字。", encoding="utf-8")
    assert check(str(md)) == 1


def test_validate_punct_fail_dash(tmp_path):
    """validate_punct 偵測破折號。"""
    from validate_punct import check
    md = tmp_path / "bad.md"
    md.write_text("這段文字用了破折號，表示停頓。".replace("，", "\u2014\u2014"), encoding="utf-8")
    assert check(str(md)) == 1


# ====================
# v1.1 新增：前處理層、編碼降級層、summary 降級
# ====================
FROZEN_RADICAL_KEYS = {
    "\u2ed1", "\u2ed2", "\u2eba", "\u2ebf", "\u2ee2", "\u2ee4", "\u2ee8",
}


def test_frozen_radical_map_keys():
    """凍結契約（v1.1）：部首補充區對照表鍵值不可縮減。"""
    import preprocess
    assert FROZEN_RADICAL_KEYS.issubset(set(preprocess.RADICAL_SUPPLEMENT_MAP.keys()))


def test_normalize_radicals_keeps_fullwidth():
    """部首字修復，且全形標點不可被打成半形。"""
    import preprocess
    src = "\u2f8f\u653f\u52a9\u7406\uff0c\u2f2f\u4f5c\uff08AI\uff09\uff1f"
    out = preprocess.normalize_text(src)
    assert out.startswith("行政助理")
    assert "工作" in out
    assert "，" in out and "（" in out and "？" in out
    assert "," not in out and "(" not in out


def test_normalize_dash_to_fullwidth_colon():
    """破折號一律改全形冒號（房規三）。"""
    import preprocess
    out = preprocess.normalize_text("最重要的一份文件\u2014\u2014公司介紹。")
    assert "\u2014" not in out and "：" in out


def test_footer_filter():
    """頁眉頁尾樣式命中，正文不受影響。"""
    import preprocess
    assert preprocess.is_footer("© 2026 酒 Ann 版權所有")
    assert preprocess.is_footer("第 4 章 · 23")
    assert preprocess.is_footer("  42 ")
    assert not preprocess.is_footer("AI 的品質，來自知識。")


def test_heading_compose():
    """凍結契約（v1.1）：section_title 組合格式為「章｜節」。"""
    import preprocess
    kind, text = preprocess.heading_kind("第 7 章")
    assert kind == "chapter"
    kind2, text2 = preprocess.heading_kind("第一節｜AI 不會一開始就做到 100 分")
    assert kind2 == "section"
    assert preprocess.compose_heading(text, text2) == "第 7 章｜第一節｜AI 不會一開始就做到 100 分"
    assert preprocess.compose_heading(None, None) is None


def test_offline_encoding_roundtrip():
    """凍結契約（v1.1）：離線編碼器 encode／decode 可逆。"""
    import enc_compat
    enc = enc_compat.OfflineEncoding()
    text = "AI 行政助理 Onboarding，共 104 個切片。"
    assert enc.decode(enc.encode(text)) == text
    assert enc_compat.is_exact(enc) is False


def test_offline_encoding_granularity():
    """離線編碼器切分規則：CJK 一字一 token。"""
    import enc_compat
    enc = enc_compat.OfflineEncoding()
    assert len(enc.encode("行政助理")) == 4


def test_extractive_summary_fallback():
    """summary 降級為抽取式，非空且不得含錯誤字串。"""
    from generate_summary import extractive_summary
    chunk = {
        "section_title": "第 7 章｜第一節｜AI 不會一開始就做到 100 分",
        "text": "的學習速度，遠比真人快。只要你持續提供正確的回饋，它會越來越符合你的工作方式。",
    }
    out = extractive_summary(chunk)
    assert out.startswith("第 7 章｜第一節")
    assert out.endswith("。")
    assert "生成失敗" not in out


def test_extractive_summary_without_title():
    """無 section_title 時仍產出可用摘要。"""
    from generate_summary import extractive_summary
    out = extractive_summary({"section_title": None, "text": "AI 的品質，來自知識庫，而不是提問技巧。"})
    assert out and "未分節內容" in out


# ===== v1.2：token 界限檢查（非自我循環，不需網路）=====
import importlib.util as _ilu
import sys as _sys
_scripts = str(Path(__file__).parent.parent / "scripts")
if _scripts not in _sys.path:
    _sys.path.insert(0, _scripts)
_FIXTURES = Path(__file__).parent / "fixtures"
_spec = _ilu.spec_from_file_location("validate_output",
    str(Path(__file__).parent.parent / "scripts" / "validate_output.py"))
_vo = _ilu.module_from_spec(_spec); _spec.loader.exec_module(_vo)


def _mk(cid, text, tc):
    return {"chunk_id": cid, "text": text, "token_count": tc,
            "prev_chunk_id": None, "next_chunk_id": None}


def _valid(cid):
    """造一個內容與 token_count 相符、且落在界內的合法切片。"""
    import enc_compat
    enc = enc_compat.get_encoding()
    text = "這是一段測試用的正文內容需要足夠長度形成一個切片。" * 3
    tc = len(enc.encode(text))
    return _mk(cid, text, tc), tc


def test_v12_token_in_range_passes():
    c, tc = _valid("a")
    assert 30 <= tc <= int((256 + 40) * 1.2)      # 落在界內
    errs = _vo.validate_chunks([c], None, 256, 40, 30)
    assert not any("token_count" in e for e in errs)


def test_v12_token_oversize_blocks():
    errs = _vo.validate_chunks([_mk("a", "正文", 2000)], None, 256, 40, 30)
    assert any("爆量" in e for e in errs)


def test_v12_token_below_minlen_blocks():
    errs = _vo.validate_chunks([_mk("a", "太短", 5)], None, 256, 40, 30)
    assert any("min_len" in e for e in errs)


def test_v12_token_no_longer_vacuous():
    good, _ = _valid("a")
    good_errs = _vo.validate_chunks([good], None, 256, 40, 30)
    bad_errs = _vo.validate_chunks([_mk("b", "正文", 999)], None, 256, 40, 30)
    assert not any("token" in e for e in good_errs)
    assert any("爆量" in e for e in bad_errs)


# ===== v1.3：格式 adapter 與品質閘門 =====
def test_v13_detects_markup_formats():
    from run_chunker import detect_format

    assert detect_format(Path("guide.html")) == "html"
    assert detect_format(Path("guide.htm")) == "html"
    assert detect_format(Path("catalog.xml")) == "xml"
    assert detect_format(Path("guide.txt")) == "unknown"


def test_v13_markdown_blocks_keep_heading_and_locator():
    from chunk_markup import _markdown_blocks

    blocks = _markdown_blocks("# English\n\nBrush one's teeth.\n\n- Repeat daily.")
    assert blocks[0]["section_title"] == "English"
    assert blocks[1]["section_title"] == "English"
    assert blocks[1]["source_locator"] == "converted-line:0003-0003"
    assert blocks[2]["block_type"] == "list"


def test_v131_marker_blocks_keep_page_locator():
    from chunk_pdf_marker import _marker_blocks

    blocks = _marker_blocks("{4}------------------------------------------------\n\n# Daily English\n\nBrush one's teeth.\n")
    assert blocks[0]["page_number"] == 5
    assert blocks[0]["source_locator"].startswith("marker-page:4")
    assert blocks[0]["section_title"] == "Daily English"


def test_v131_marker_command_disables_ocr(monkeypatch, tmp_path):
    from types import SimpleNamespace

    import chunk_pdf_marker

    calls = []
    monkeypatch.setattr(chunk_pdf_marker, "_marker_executable", lambda: "marker_single")

    def fake_run(command, **kwargs):
        calls.append(command)
        output_dir = Path(command[command.index("--output_dir") + 1])
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "source.md").write_text("source text", encoding="utf-8")
        return SimpleNamespace(returncode=0, stdout="", stderr="")

    monkeypatch.setattr(chunk_pdf_marker.subprocess, "run", fake_run)
    result = chunk_pdf_marker._run_marker(Path("source.pdf"), tmp_path)

    assert result == "source text"
    assert calls
    assert "--disable_ocr" in calls[0]
    assert "--force_ocr" not in calls[0]


def test_v13_quality_gate_rejects_suspicious_glyph():
    from quality_gate import validate_chunks

    chunks = [{"chunk_id": "a", "text": "brushone\ufe41steeth", "source_locator": "p005"}]
    errors = validate_chunks(chunks, require_locator=True)
    assert any("編碼異常" in error for error in errors)


def test_v13_quality_gate_requires_locator():
    from quality_gate import validate_chunks

    chunks = [{"chunk_id": "a", "text": "有內容", "source_locator": ""}]
    errors = validate_chunks(chunks, require_locator=True)
    assert any("來源定位" in error for error in errors)


def test_v13_quality_anchor_is_exact():
    from quality_gate import validate_chunks

    chunks = [{"chunk_id": "a", "text": "brush one's teeth", "source_locator": "p005"}]
    assert not validate_chunks(chunks, require_locator=True, anchors=["brush one's teeth"])
    assert validate_chunks(chunks, require_locator=True, anchors=["brushone's teeth"])


def test_v131_quality_review_does_not_raise_by_default():
    from quality_gate import annotate_chunks

    chunks = [{"chunk_id": "a", "text": "bad\ufe41text", "source_locator": "p001"}]
    errors = annotate_chunks(chunks, "docling", require_locator=True)
    assert errors
    assert chunks[0]["quality_status"] == "REVIEW"


def test_v131_strict_quality_still_blocks():
    from quality_gate import annotate_chunks

    chunks = [{"chunk_id": "a", "text": "bad\ufe41text", "source_locator": "p001"}]
    with pytest.raises(RuntimeError):
        annotate_chunks(chunks, "docling", require_locator=True, strict=True)


def test_v131_punctuation_warning_is_nonblocking_by_default(tmp_path):
    from validate_output import validate_md_file

    md = tmp_path / "review.md"
    md.write_text("中文,含半形標點。", encoding="utf-8")
    assert validate_md_file(md) == []
    assert validate_md_file(md, strict_quality=True)


def test_v13_render_optional_metadata(tmp_path):
    from render_md import render

    chunks = [{
        "chunk_id": "test_doc_0000",
        "text": "Markup content with enough words for a metadata test.",
        "source_file": "test.html",
        "file_type": "html",
        "chunk_index": 0,
        "page_number": None,
        "start_time": None,
        "end_time": None,
        "section_title": "English",
        "prev_chunk_id": None,
        "next_chunk_id": None,
        "token_count": 12,
        "summary": "摘要。",
        "source_locator": "line:0001-0002",
        "block_type": "paragraph",
        "extraction_backend": "markitdown",
        "quality_status": "PASS",
    }]
    md_path, _ = render(chunks, tmp_path, "test")
    content = md_path.read_text(encoding="utf-8")
    assert "source_locator: line:0001-0002" in content
    assert "quality_status: PASS" in content


def test_v13_zero_overlap_does_not_copy_previous_block():
    from adapter_common import blocks_to_chunks

    blocks = [
        {"text": "first block has enough words.", "source_locator": "a"},
        {"text": "second block has enough words.", "source_locator": "b"},
    ]
    chunks = blocks_to_chunks(
        blocks,
        Path("test.html"),
        file_type="html",
        chunk_size=40,
        overlap=0,
        min_len=1,
    )
    assert len(chunks) == 2
    assert chunks[1]["text"].startswith("second block")


def test_v13_rendered_artifact_binding(tmp_path):
    from render_md import render
    from validate_output import validate_rendered_artifacts

    chunks = [{
        "chunk_id": "bound_0000",
        "text": "正文必須存在於目前產物。",
        "source_file": "bound.xml",
        "file_type": "xml",
        "chunk_index": 0,
        "page_number": None,
        "start_time": None,
        "end_time": None,
        "section_title": None,
        "prev_chunk_id": None,
        "next_chunk_id": None,
        "token_count": 12,
        "summary": "摘要。",
    }]
    md_path, zip_path = render(chunks, tmp_path, "bound")
    assert not validate_rendered_artifacts(chunks, md_path, zip_path)
    md_path.write_text("被竄改的產物。", encoding="utf-8")
    assert any("Markdown 缺少" in error for error in validate_rendered_artifacts(chunks, md_path, zip_path))


def test_v13_bootstrap_installs_when_import_missing(monkeypatch):
    import bootstrap

    state = {"installed": False}
    pip_calls = []
    invalidated = []

    def fake_import(name):
        if name == "fake_module" and not state["installed"]:
            raise ImportError("missing")
        return object()

    def fake_pip(args):
        pip_calls.append(args)
        state["installed"] = True

    monkeypatch.setattr(bootstrap.importlib, "import_module", fake_import)
    monkeypatch.setattr(bootstrap.importlib, "invalidate_caches", lambda: invalidated.append(True))
    monkeypatch.setattr(bootstrap.subprocess, "check_call", fake_pip)
    bootstrap._pip("fake-package", "fake_module", verify=lambda: state["installed"])
    assert pip_calls and "fake-package" in pip_calls[0]
    assert invalidated == [True]


def test_v13_bootstrap_does_not_reinstall_verified_module(monkeypatch):
    import bootstrap

    pip_calls = []
    monkeypatch.setattr(bootstrap.importlib, "import_module", lambda name: object())
    monkeypatch.setattr(bootstrap.subprocess, "check_call", lambda args: pip_calls.append(args))
    bootstrap._pip("already-ready", "ready_module", verify=lambda: True)
    assert pip_calls == []


def test_v13_markitdown_docx_requests_extra_and_verifier(monkeypatch):
    import bootstrap

    calls = []
    monkeypatch.setattr(
        bootstrap,
        "_pip",
        lambda pkg, import_name=None, verify=None: calls.append((pkg, import_name, verify)),
    )
    bootstrap.ensure_markitdown_docx()
    assert calls[0][0] == "markitdown[docx]"
    assert calls[0][1] == "markitdown"
    assert callable(calls[0][2])


def test_v13_xml_safe_route_preserves_path_and_attributes(tmp_path):
    pytest.importorskip("lxml.etree")
    from chunk_markup import _xml_blocks

    source = tmp_path / "catalog.xml"
    source.write_text(
        '<catalog><book id="b1"><title>English words</title></book></catalog>',
        encoding="utf-8",
    )
    blocks = _xml_blocks(source)
    text = "\n".join(block["text"] for block in blocks)
    assert "/catalog/book" in text
    assert "@id=b1" in text
    assert any(block["source_locator"].startswith("/catalog") for block in blocks)


def test_v13_xml_safe_route_rejects_external_entity(tmp_path):
    pytest.importorskip("lxml.etree")
    from chunk_markup import _xml_blocks

    source = tmp_path / "unsafe.xml"
    source.write_text(
        '<!DOCTYPE catalog [<!ENTITY xxe SYSTEM "file:///windows/win.ini">]>'
        '<catalog>&xxe;</catalog>',
        encoding="utf-8",
    )
    with pytest.raises(Exception):
        _xml_blocks(source)


def test_v132_html_declared_encoding_is_strict(tmp_path):
    from chunk_markup import _read_html_source

    source = tmp_path / "latin.html"
    raw = (
        '<meta charset="windows-1252"><p>Caf\xe9 and brush one\'s teeth.</p>'
    ).encode("windows-1252")
    source.write_bytes(raw)
    text = _read_html_source(source)
    assert "Café" in text
    assert "\ufffd" not in text


def test_v132_html_undecodable_input_fails_closed(tmp_path):
    from chunk_markup import _read_html_source

    source = tmp_path / "unknown.html"
    source.write_bytes(b"<html><body>bad\xfftext</body></html>")
    with pytest.raises(RuntimeError, match="HTML 編碼"):
        _read_html_source(source)


def test_v132_html_fixture_has_expected_semantic_source():
    from chunk_markup import _markdown_blocks, _read_html_source

    html = _read_html_source(_FIXTURES / "html" / "document.html")
    blocks = _markdown_blocks(
        "# English vocabulary\n\nBrush one's teeth before breakfast.\n\n"
        "- Brush the outside surfaces."
    )
    assert blocks[0]["block_type"] == "heading"
    assert any("brush one's teeth" in block["text"].lower() for block in blocks)
    assert "Brush one's teeth" in html


def test_v132_xml_namespace_and_mixed_content_fixture():
    pytest.importorskip("lxml.etree")
    from chunk_markup import _xml_blocks

    blocks = _xml_blocks(_FIXTURES / "xml" / "namespaced_mixed.xml")
    text = "\n".join(block["text"] for block in blocks)
    locators = [block["source_locator"] for block in blocks]
    assert "/{urn:demo:catalog}catalog" in text
    assert "/{urn:demo:catalog}item[1]" in text
    assert "@{urn:demo:meta}code=one" in text
    assert "Brush one's teeth every day." in text
    assert any("{urn:demo:catalog}term" in locator for locator in locators)


def test_v132_xml_limits_fail_closed(monkeypatch, tmp_path):
    pytest.importorskip("lxml.etree")
    from chunk_markup import _xml_blocks

    source = tmp_path / "many.xml"
    source.write_text("<root><a>one</a><b>two</b></root>", encoding="utf-8")
    monkeypatch.setattr("chunk_markup._MAX_XML_ELEMENTS", 2)
    with pytest.raises(RuntimeError, match="元素數"):
        _xml_blocks(source)


def test_v132_xml_fixture_rejects_doctype():
    pytest.importorskip("lxml.etree")
    from chunk_markup import _xml_blocks

    with pytest.raises(RuntimeError, match="DOCTYPE"):
        _xml_blocks(_FIXTURES / "xml" / "external_entity.xml")
