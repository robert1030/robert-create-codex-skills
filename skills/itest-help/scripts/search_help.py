import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_DATA_DIR = SKILL_DIR / "references"

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "for", "from",
    "has", "have", "how", "in", "into", "is", "it", "its", "of", "on",
    "not", "or", "that", "the", "this", "to", "with", "you", "your",
}

UI_SCOPE_DETAILS = {
    "analysis_rule_wizard_page": {
        "label": "Analysis Rule Wizard page",
        "note": "Wizard UI page; selections may map to generated analysis rule properties.",
    },
    "analysis_rule_extractor_properties": {
        "label": "Analysis rule extractor properties",
        "note": "Extractor settings and behavior inside analysis rules; not a general step setting.",
    },
    "analysis_rule_processor_properties": {
        "label": "Analysis rule processor/action properties",
        "note": "Processor and When True/When False action behavior inside analysis rules.",
    },
    "analysis_rule_popup_reference": {
        "label": "Analysis rule popup reference",
        "note": "Popup reference page for an analysis rule item; inspect the page title for the exact owner.",
    },
    "analysis_rule_editor_properties": {
        "label": "Analysis rule editor properties",
        "note": "Analysis Rule Properties section for editing rule extractor/processor settings.",
    },
    "step_properties_section": {
        "label": "Step Properties section",
        "note": "Step-level settings in the Test Case Editor or Properties view.",
    },
    "properties_view": {
        "label": "Properties view",
        "note": "General Properties view behavior; selected object determines which properties appear.",
    },
    "parameter_custom_types": {
        "label": "Parameter custom types",
        "note": "Custom parameter type/value definitions; unrelated to Custom Extractor/Processor.",
    },
    "session_builder_custom_session_type": {
        "label": "Session Builder custom session type",
        "note": "Custom session type creation/installation/use; unrelated to analysis rule custom pages.",
    },
    "response_map_editor": {
        "label": "Response Map editor",
        "note": "Response map/query/parser authoring surface.",
    },
    "test_case_step_action": {
        "label": "Test case step/action reference",
        "note": "Action or step behavior; related properties may appear under Step Properties.",
    },
    "itest_command_reference": {
        "label": "iTest command reference",
        "note": "Interpreter or field-replacement command reference.",
    },
    "analysis_rule_topic": {
        "label": "Analysis rule topic",
        "note": "General analysis rule documentation; inspect page text for exact UI layer.",
    },
    "test_case_editor_topic": {
        "label": "Test Case Editor topic",
        "note": "General Test Case Editor documentation; inspect page text for exact UI layer.",
    },
    "general_help_page": {
        "label": "General help page",
        "note": "No narrower UI scope inferred from packaged metadata.",
    },
}


def tokenize(value):
    value = (value or "").lower()
    tokens = re.findall(r"[a-z0-9][a-z0-9_./+-]*", value)
    normalized = []
    for token in tokens:
        for part in re.split(r"[_./+-]+", token):
            if len(part) < 2 or part in STOPWORDS:
                continue
            normalized.append(part)
        if len(token) >= 2 and token not in STOPWORDS:
            normalized.append(token)
    return normalized


def load_pages(data_dir):
    pages = []
    with (data_dir / "help_pages.jsonl").open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                pages.append(json.loads(line))
    return pages


def load_index(data_dir):
    return json.loads((data_dir / "search_index.json").read_text(encoding="utf-8"))


def is_specific_token(token):
    return "_" in token or any(char.isdigit() for char in token) or len(token) >= 12


def infer_ui_scope(page):
    source_ref = page.get("source_ref", page.get("relative_path", page.get("file_name", "")))
    source_ref = source_ref.replace("\\", "/").lower()
    title_text = " ".join(
        [
            page.get("title", ""),
            page.get("h1", ""),
            " ".join(item.get("text", "") for item in page.get("headings", [])),
        ]
    ).lower()
    toc_text = " ".join(page.get("toc_paths", []) + page.get("toc_top_categories", [])).lower()
    doc_set = (page.get("doc_set", "") or "").lower()

    if source_ref.startswith("topics/popups/arules/"):
        if "extractor" in title_text:
            scope = "analysis_rule_extractor_properties"
        elif "processor" in title_text or "action" in title_text:
            scope = "analysis_rule_processor_properties"
        else:
            scope = "analysis_rule_popup_reference"
    elif source_ref.startswith("topics/arw_") or title_text.startswith("analysis rule wizard:"):
        scope = "analysis_rule_wizard_page"
    elif source_ref == "topics/arules_extractor_properties.htm":
        scope = "analysis_rule_extractor_properties"
    elif source_ref == "topics/arules_processor_properties.htm":
        scope = "analysis_rule_processor_properties"
    elif source_ref in {
        "topics/arules_global_working_with.htm",
        "topics/arules_working_with.htm",
    } or "analysis rule properties" in title_text:
        scope = "analysis_rule_editor_properties"
    elif source_ref.startswith("topics/tce_step_properties_") or title_text.startswith("step properties section:"):
        scope = "step_properties_section"
    elif source_ref == "topics/view_properties.htm":
        scope = "properties_view"
    elif "custom type" in title_text or "custom types" in title_text:
        scope = "parameter_custom_types"
    elif "custom session type" in title_text or (source_ref.startswith("topics/sb_") and "session builder" in toc_text):
        scope = "session_builder_custom_session_type"
    elif "response map editor" in title_text or doc_set == "response_mapping":
        scope = "response_map_editor"
    elif doc_set == "actions":
        scope = "test_case_step_action"
    elif doc_set == "commands":
        scope = "itest_command_reference"
    elif doc_set == "analysis_rules":
        scope = "analysis_rule_topic"
    elif doc_set == "test_case_editor":
        scope = "test_case_editor_topic"
    else:
        scope = "general_help_page"

    detail = UI_SCOPE_DETAILS[scope]
    return {
        "ui_scope": scope,
        "ui_scope_label": detail["label"],
        "ui_scope_note": detail["note"],
    }


def build_scope_summary(results):
    seen = {}
    order = []
    for result in results:
        scope = result["ui_scope"]
        if scope not in seen:
            seen[scope] = {
                "ui_scope": scope,
                "ui_scope_label": result["ui_scope_label"],
                "count": 0,
                "examples": [],
            }
            order.append(scope)
        seen[scope]["count"] += 1
        if len(seen[scope]["examples"]) < 3:
            seen[scope]["examples"].append(result["source_ref"])
    return [seen[scope] for scope in order]


def mixed_scope_warning(query_terms, scope_summary):
    if len(scope_summary) <= 1:
        return ""

    terms = set(query_terms)
    sensitive_terms = {
        "action",
        "analysis",
        "click",
        "custom",
        "dialog",
        "editor",
        "extractor",
        "page",
        "process",
        "processor",
        "properties",
        "property",
        "rule",
        "rules",
        "setting",
        "settings",
        "step",
        "view",
        "wizard",
    }
    sensitive_scopes = {
        "analysis_rule_editor_properties",
        "analysis_rule_extractor_properties",
        "analysis_rule_popup_reference",
        "analysis_rule_processor_properties",
        "analysis_rule_wizard_page",
        "parameter_custom_types",
        "properties_view",
        "response_map_editor",
        "session_builder_custom_session_type",
        "step_properties_section",
        "test_case_editor_topic",
        "test_case_step_action",
    }
    if terms & sensitive_terms or any(item["ui_scope"] in sensitive_scopes for item in scope_summary):
        return "Search results span multiple UI or product scopes; separate the answer by location/scope or refine with --scope."
    return ""


def guardrail_boost(page, query_terms):
    terms = set(query_terms)
    source_ref = page.get("source_ref", page.get("relative_path", page["file_name"]))
    boost = 0

    if {"itest_value", "itest_index"} & terms:
        if source_ref in {
            "topics/arules_extractor_properties.htm",
            "topics/arules_processor_properties.htm",
            "topics/commands_built_in_local_variables.htm",
            "topics/arw_assertion_page.htm",
            "topics/arw_message_page.htm",
        }:
            boost += 220

    if {"thread", "safe"} <= terms:
        if source_ref in {
            "topics/arules_extractor_properties.htm",
            "topics/arules_processor_properties.htm",
            "topics/commands_built_in_local_variables.htm",
        }:
            boost += 120

    if "secret" in terms and ({"wizard", "rule", "rules"} & terms or {"mask", "masked"} & terms):
        if source_ref in {
            "topics/arw_rule_type_selection_page.htm",
            "topics/arw_extractor_selection_page.htm",
            "topics/param_parameters_type_secret.htm",
            "topics/arules_processor_properties.htm",
        }:
            boost += 180

    if "query" in terms and ({"right", "click", "right-click"} & terms) and {"analysis", "rule", "rules"} & terms:
        if source_ref in {
            "topics/arules_extractor_properties.htm",
            "topics/arules_global_working_with.htm",
        }:
            boost += 180

    if "custom" in terms and "extractor" in terms:
        if source_ref == "topics/arw_extractor_selection_page.htm":
            boost += 260
        if source_ref == "topics/arules_extractor_properties.htm":
            boost += 180

    if "custom" in terms and ({"processor", "process"} & terms):
        if source_ref == "topics/arw_processor_selection_page.htm":
            boost += 260
        if source_ref == "topics/arules_processor_properties.htm":
            boost += 180

    if {"analysis", "rule", "properties"} <= terms:
        if source_ref in {
            "topics/arules_extractor_properties.htm",
            "topics/arules_processor_properties.htm",
        }:
            boost += 560
        if source_ref in {
            "topics/arules_global_working_with.htm",
            "topics/arules_working_with.htm",
        }:
            boost += 420

    if {"step", "properties"} <= terms:
        if source_ref.startswith("topics/tce_step_properties_"):
            boost += 160
        if source_ref == "topics/view_properties.htm":
            boost += 120

    if "clock" in terms and (
        {"scan", "format", "time", "date", "conversion", "2038", "2041", "2049"} & terms
    ):
        if source_ref == "topics/command_syntax.htm":
            boost += 300
        if source_ref == "topics/popups/clock.html":
            boost += 520
        if "tcl" in terms and source_ref == "topics/command_tcl.htm":
            boost += 180

    return boost


def compact_snippet(text, query, tokens, width=240):
    lowered = text.lower()
    needle = query.lower().strip()
    pos = lowered.find(needle) if needle else -1
    if pos < 0:
        for token in tokens:
            pos = lowered.find(token)
            if pos >= 0:
                break
    if pos < 0:
        pos = 0

    start = max(0, pos - 80)
    end = min(len(text), start + width)
    start = max(0, end - width)
    snippet = re.sub(r"\s+", " ", text[start:end]).strip()
    if start > 0:
        snippet = "... " + snippet
    if end < len(text):
        snippet += " ..."
    return snippet


def search(query, data_dir, top, scope=None):
    index = load_index(data_dir)
    pages = load_pages(data_dir)
    tokens = tokenize(query)
    query_terms = sorted(set(tokens))
    unmatched_terms = [token for token in query_terms if token not in index["terms"]]
    scores = defaultdict(int)
    matched_terms = defaultdict(list)

    for token in tokens:
        for doc_id, score in index["terms"].get(token, []):
            scores[doc_id] += score
            if is_specific_token(token):
                scores[doc_id] += 120
            matched_terms[doc_id].append(token)

    phrase = query.lower().strip()
    for doc_id in list(scores.keys()):
        page = pages[doc_id]
        scores[doc_id] += guardrail_boost(page, query_terms)
        evidence_haystack = "\n".join(
            [
                page.get("title", ""),
                page.get("h1", ""),
                " ".join(item["text"] for item in page.get("headings", [])),
                " ".join(page.get("toc_paths", [])),
                " ".join(page.get("toc_top_categories", [])),
                page.get("text", ""),
            ]
        ).lower()
        metadata_haystack = "\n".join(
            [
                " ".join(page.get("index_terms", [])),
                " ".join(page.get("index_paths", [])),
                " ".join(page.get("context_ids", [])),
                " ".join(page.get("context_labels", [])),
            ]
        ).lower()
        if phrase and phrase in evidence_haystack:
            scores[doc_id] += 50
        elif phrase and phrase in metadata_haystack:
            scores[doc_id] += 10

    if scope and scope not in UI_SCOPE_DETAILS:
        raise ValueError(f"Unknown UI scope: {scope}")

    candidates = []
    for doc_id, score in scores.items():
        ui_scope = infer_ui_scope(pages[doc_id])["ui_scope"]
        if scope and ui_scope != scope:
            continue
        candidates.append((doc_id, score))

    ranked = sorted(candidates, key=lambda item: item[1], reverse=True)[:top]
    results = []
    for doc_id, score in ranked:
        page = pages[doc_id]
        ui_scope = infer_ui_scope(page)
        results.append(
            {
                "score": score,
                "file_name": page["file_name"],
                "relative_path": page.get("relative_path", page["file_name"]),
                "title": page["title"],
                "h1": page["h1"],
                "doc_set": page["doc_set"],
                "probable_category": page["probable_category"],
                **ui_scope,
                "toc_primary_path": page.get("toc_primary_path", ""),
                "toc_top_categories": page.get("toc_top_categories", []),
                "toc_paths": page.get("toc_paths", []),
                "index_terms": page.get("index_terms", [])[:24],
                "index_paths": page.get("index_paths", [])[:8],
                "context_ids": page.get("context_ids", [])[:12],
                "context_labels": page.get("context_labels", [])[:12],
                "matched_terms": sorted(set(matched_terms[doc_id])),
                "unmatched_terms": unmatched_terms,
                "snippet": compact_snippet(page.get("text", ""), query, tokens),
                "source_ref": page.get("source_ref", page["file_name"]),
            }
        )
    scope_summary = build_scope_summary(results)
    return {
        "query": query,
        "query_terms": query_terms,
        "unmatched_terms": unmatched_terms,
        "scope_filter": scope or "",
        "scope_summary": scope_summary,
        "mixed_scope_warning": mixed_scope_warning(query_terms, scope_summary),
        "results": results,
    }


def show_file(file_name, data_dir, text_only):
    pages = load_pages(data_dir)
    needle = file_name.replace("\\", "/").lower()
    matches = []
    for page in pages:
        candidates = {
            page["file_name"].lower(),
            page.get("relative_path", page["file_name"]).lower(),
            page.get("source_ref", page["file_name"]).lower(),
        }
        source_ref = page.get("source_ref", "")
        if source_ref.lower().startswith("topics/"):
            candidates.add(source_ref[7:].lower())
        if needle in candidates:
            matches.append(page)

    if len(matches) == 1:
        page = matches[0]
        if text_only:
            print(page["text"])
        else:
            print(json.dumps(page, ensure_ascii=False, indent=2))
        return 0
    if len(matches) > 1:
        print(f"Multiple help pages match: {file_name}")
        for page in matches:
            print(page.get("source_ref", page.get("relative_path", page["file_name"])))
        print("Use --show-file with the relative path or source_ref.")
        return 1
    print(f"No help page found for file: {file_name}")
    return 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", nargs="?")
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--top", type=int, default=8)
    parser.add_argument("--scope", choices=sorted(UI_SCOPE_DETAILS))
    parser.add_argument("--list-scopes", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--show-file")
    parser.add_argument("--text", action="store_true")
    args = parser.parse_args()

    if args.list_scopes:
        for scope in sorted(UI_SCOPE_DETAILS):
            print(f"{scope}: {UI_SCOPE_DETAILS[scope]['label']}")
        return
    if args.show_file:
        raise SystemExit(show_file(args.show_file, args.data_dir, args.text))
    if not args.query:
        parser.error("query is required unless --show-file is used")

    response = search(args.query, args.data_dir, args.top, args.scope)
    if args.json:
        print(json.dumps(response, ensure_ascii=False, indent=2))
        return

    if response["scope_filter"]:
        print(f"scope filter: {response['scope_filter']}")
    if response["unmatched_terms"]:
        print(f"unmatched terms: {', '.join(response['unmatched_terms'])}")
    if not response["results"]:
        print("No matching help pages found.")
        return
    if response["scope_summary"]:
        print(
            "ui scopes: "
            + "; ".join(
                f"{item['ui_scope_label']} ({item['count']})"
                for item in response["scope_summary"]
            )
        )
    if response["mixed_scope_warning"]:
        print(f"warning: {response['mixed_scope_warning']}")

    for rank, result in enumerate(response["results"], start=1):
        print(f"{rank}. [{result['score']}] {result['source_ref']}")
        print(f"   title: {result['title']}")
        print(f"   scope: {result['ui_scope_label']} ({result['ui_scope']})")
        if result.get("toc_primary_path"):
            print(f"   toc: {result['toc_primary_path']}")
        if result.get("index_paths"):
            print(f"   index: {result['index_paths'][0]}")
        if result.get("context_ids"):
            print(f"   contexts: {', '.join(result['context_ids'][:5])}")
        print(f"   category: {result['probable_category']} / {result['doc_set']}")
        print(f"   snippet: {result['snippet']}")


if __name__ == "__main__":
    main()
