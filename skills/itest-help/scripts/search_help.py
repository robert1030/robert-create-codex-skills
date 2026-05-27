import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
DEFAULT_DATA_DIR = SKILL_DIR / "references"
SEARCH_RULES_FILE = "search_rules.json"
PROPERTY_INDEX_FILE = "property_index.jsonl"

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

MATCH_SOURCE_ORDER = [
    "title",
    "h1",
    "page_text",
    "toc",
    "index_metadata",
    "context_metadata",
]

CONTENT_MATCH_SOURCES = {"title", "h1", "page_text"}
METADATA_MATCH_SOURCES = {"index_metadata", "context_metadata"}

FIELD_WEIGHTS = {
    "title": 4.0,
    "h1": 3.4,
    "page_text": 1.0,
    "toc": 1.2,
    "index_metadata": 0.22,
    "context_metadata": 0.18,
}

BM25_K1 = 1.2
BM25_B = 0.75
MMR_LAMBDA = 0.72
MMR_POOL_FLOOR_RATIO = 0.30

SENSITIVE_SCOPE_TERMS = {
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


def normalized_phrase(value):
    return " ".join(tokenize(value))


def load_pages(data_dir):
    pages = []
    with (data_dir / "help_pages.jsonl").open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                pages.append(json.loads(line))
    return pages


def load_index(data_dir):
    return json.loads((data_dir / "search_index.json").read_text(encoding="utf-8"))


def load_search_rules(data_dir):
    path = data_dir / SEARCH_RULES_FILE
    if not path.exists():
        return {"canonical_phrases": [], "source_rules": []}
    return json.loads(path.read_text(encoding="utf-8"))


def load_property_index(data_dir):
    path = data_dir / PROPERTY_INDEX_FILE
    if not path.exists():
        return {}
    index = {}
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            item = json.loads(line)
            index[item["source_ref"].replace("\\", "/")] = item
    return index


def is_specific_token(token):
    return "_" in token or any(char.isdigit() for char in token) or len(token) >= 12


def is_identifier_query(query):
    return bool(re.search(r"[_./+-]", query or ""))


def page_source_ref(page):
    return page.get("source_ref", page.get("relative_path", page.get("file_name", "")))


def page_source_texts(page):
    return {
        "title": page.get("title", ""),
        "h1": page.get("h1", ""),
        "page_text": page.get("text", ""),
        "toc": " ".join(
            page.get("toc_paths", [])
            + page.get("toc_top_categories", [])
            + page.get("toc_labels", [])
        ),
        "index_metadata": " ".join(page.get("index_terms", []) + page.get("index_paths", [])),
        "context_metadata": " ".join(
            page.get("context_ids", []) + page.get("context_labels", [])
        ),
    }


def analyze_match_sources(page, query, query_terms):
    phrase = (query or "").lower().strip()
    sources = []
    exact_match_sources = []
    all_matched_terms = []

    for source in MATCH_SOURCE_ORDER:
        text = page_source_texts(page)[source]
        lowered = text.lower()
        field_tokens = set(tokenize(text))
        matched = [
            term
            for term in query_terms
            if term in field_tokens or (is_specific_token(term) and term in lowered)
        ]
        exact_phrase = bool(phrase and phrase in lowered)
        if matched or exact_phrase:
            if exact_phrase:
                exact_match_sources.append(source)
            all_matched_terms.extend(matched)
            sources.append(
                {
                    "source": source,
                    "matched_terms": matched[:12],
                    "exact_phrase": exact_phrase,
                }
            )

    source_names = [item["source"] for item in sources]
    has_content_match = any(source in CONTENT_MATCH_SOURCES for source in source_names)
    has_page_text_match = "page_text" in source_names
    metadata_only = bool(source_names) and all(
        source in METADATA_MATCH_SOURCES for source in source_names
    )
    metadata_exact_only = bool(exact_match_sources) and all(
        source in METADATA_MATCH_SOURCES for source in exact_match_sources
    )

    if metadata_only:
        evidence_note = (
            "metadata-only candidate: index/context metadata can locate a page, "
            "but product behavior still requires page_text."
        )
    elif metadata_exact_only and not has_page_text_match:
        evidence_note = (
            "exact query matched metadata; use it to locate the page and verify "
            "behavior in page_text."
        )
    elif metadata_exact_only:
        evidence_note = (
            "exact query matched metadata; cite page_text, not metadata, for "
            "product behavior."
        )
    elif not has_page_text_match:
        evidence_note = "no page_text term match; use this mainly as a navigation candidate."
    else:
        evidence_note = "page_text match available for product behavior evidence."

    return {
        "match_sources": sources,
        "match_source_names": source_names,
        "exact_match_sources": exact_match_sources,
        "matched_terms": sorted(set(all_matched_terms)),
        "metadata_only": metadata_only,
        "metadata_exact_only": metadata_exact_only,
        "has_content_match": has_content_match,
        "has_page_text_match": has_page_text_match,
        "evidence_note": evidence_note,
    }


def source_match_boost(match_profile):
    boost = 0
    weights = {
        "title": 70,
        "h1": 60,
        "page_text": 40,
        "toc": 20,
        "index_metadata": 6,
        "context_metadata": 6,
    }
    for item in match_profile["match_sources"]:
        boost += weights[item["source"]]
        if item["exact_phrase"]:
            boost += 40 if item["source"] in CONTENT_MATCH_SOURCES else 8
    if match_profile["metadata_only"]:
        boost -= 80
    elif not match_profile["has_page_text_match"]:
        boost -= 25
    return boost


def format_match_sources(match_profile):
    by_source = {item["source"]: item for item in match_profile["match_sources"]}
    parts = []
    for source in MATCH_SOURCE_ORDER:
        item = by_source.get(source)
        if not item:
            continue
        details = []
        if item["exact_phrase"]:
            details.append("exact")
        details.extend(item["matched_terms"][:5])
        if details:
            parts.append(f"{source}({', '.join(details)})")
        else:
            parts.append(source)
    return "; ".join(parts) if parts else "none"


def present_property_rows(text, candidates):
    lowered = text.lower()
    return [candidate for candidate in candidates if candidate.lower() in lowered]


def property_poc_for_page(page, property_index):
    source_ref = page_source_ref(page).replace("\\", "/")
    text = page.get("text", "")
    headings = [
        item.get("text", "")
        for item in page.get("headings", [])
        if item.get("level", 0) > 1 and item.get("text")
    ]

    definition = property_index.get(source_ref)
    if definition:
        sections = []
        for section in definition["sections"]:
            property_rows = present_property_rows(text, section["property_rows"])
            if section["section"].lower() in text.lower() or property_rows:
                sections.append(
                    {
                        "section": section["section"],
                        "property_rows": property_rows,
                    }
                )
        return {
            "property_scope": definition["property_scope"],
            "source": definition.get("source", "help_pages text/headings"),
            "sections": sections,
            "note": definition.get(
                "note",
                "Property rows are verified against official help page text.",
            ),
        }

    if source_ref.startswith("topics/tce_step_properties_"):
        title = page.get("title", "")
        section = title.split(":", 1)[1].strip() if ":" in title else title
        return {
            "property_scope": "Step Properties section",
            "source": "help_pages text/headings",
            "sections": [{"section": section or "Step Properties section", "property_rows": []}],
            "note": "POC section marker only; no row extraction was added for this page.",
        }

    if source_ref in {
        "topics/arules_global_working_with.htm",
        "topics/arules_working_with.htm",
    }:
        return {
            "property_scope": "Analysis Rule Properties",
            "source": "help_pages text/headings",
            "sections": [
                {
                    "section": heading,
                    "property_rows": [],
                }
                for heading in headings[:4]
            ],
            "note": "POC section marker only; this page is not treated as a property table.",
        }

    return {}


def format_property_poc(property_poc, query_terms=None):
    if not property_poc:
        return ""
    query_terms = set(query_terms or [])
    focus_terms = query_terms - {"analysis", "properties", "property", "rule", "rules", "step"}
    parts = []
    sections = property_poc.get("sections", [])
    if focus_terms:
        def section_score(section):
            section_text = section.get("section", "").lower()
            section_tokens = set(tokenize(section_text))
            row_text = " ".join(section.get("property_rows", [])).lower()
            row_tokens = set(tokenize(row_text))
            return (
                4 * len(focus_terms & section_tokens)
                + 2 * len(focus_terms & row_tokens)
                + sum(1 for term in focus_terms if term in section_text)
                + sum(1 for term in focus_terms if term in row_text)
            )

        display_sections = sorted(sections, key=section_score, reverse=True)
    else:
        display_sections = sections
    for section in display_sections[:3]:
        rows = section.get("property_rows", [])
        if rows:
            matching_rows = [
                row
                for row in rows
                if focus_terms & set(tokenize(row)) or any(term in row.lower() for term in focus_terms)
            ]
            display_rows = matching_rows + [row for row in rows if row not in matching_rows]
            parts.append(f"{section['section']} [{', '.join(display_rows[:4])}]")
        else:
            parts.append(section["section"])
    return f"{property_poc['property_scope']}: " + "; ".join(parts)


def infer_ui_scope(page):
    source_ref = page_source_ref(page)
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


def infer_ui_surface(page, ui_scope=None):
    if ui_scope is None:
        ui_scope = infer_ui_scope(page)
    source_ref = page_source_ref(page).replace("\\", "/").lower()
    title = page.get("title") or page.get("h1") or Path(source_ref).stem
    title = re.sub(r"\s+", " ", title).strip()

    if source_ref == "topics/arw_extractor_selection_page.htm":
        key = "analysis_rule_wizard_custom_extractor"
        label = "Analysis Rule Wizard > Custom Extractor page"
        location = "Analysis Rule Wizard > Custom Extractor page"
    elif source_ref == "topics/arw_processor_selection_page.htm":
        key = "analysis_rule_wizard_processor"
        label = "Analysis Rule Wizard > Processor page"
        location = "Analysis Rule Wizard > Processor page"
    elif source_ref == "topics/arules_extractor_properties.htm":
        key = "analysis_rule_extractor_properties"
        label = "Analysis Rule Properties > Extractor Properties"
        location = "Analysis Rule Properties > Extractor Properties"
    elif source_ref == "topics/arules_processor_properties.htm":
        key = "analysis_rule_processor_action_properties"
        label = "Analysis Rule Properties > Processor/Action Properties"
        location = "Analysis Rule Properties > Processor/Action Properties"
    elif source_ref in {
        "topics/arules_global_working_with.htm",
        "topics/arules_working_with.htm",
    }:
        key = "analysis_rule_editor_properties"
        label = "Analysis Rule editor > Analysis Rule Properties"
        location = "Analysis Rule editor > Analysis Rule Properties"
    elif source_ref.startswith("topics/popups/arules/"):
        key = "analysis_rule_popup_" + Path(source_ref).stem.lower()
        label = "Analysis rule popup reference"
        location = "Analysis rule popup reference > " + title
    elif source_ref.startswith("topics/tce_step_properties_"):
        key = "step_properties_section"
        label = "Test Case Editor > Step Properties section"
        group = title.split(":", 1)[1].strip() if ":" in title else title
        location = "Test Case Editor > Step Properties section > " + group
    elif source_ref == "topics/view_properties.htm":
        key = "properties_view"
        label = "Properties view"
        location = "Properties view"
    elif ui_scope["ui_scope"] == "parameter_custom_types":
        key = "parameter_custom_types"
        label = "Parameters/Test Case/Session Profile editor > Custom Types"
        location = "Parameters/Test Case/Session Profile editor > Custom Types"
    elif ui_scope["ui_scope"] == "session_builder_custom_session_type":
        key = "session_builder_custom_session_type"
        label = "Session Builder > Custom session type"
        location = "Session Builder > Custom session type"
    elif ui_scope["ui_scope"] == "response_map_editor":
        key = "response_map_editor"
        label = "Response Map editor"
        location = "Response Map editor"
    elif ui_scope["ui_scope"] == "test_case_step_action":
        key = "test_case_step_action"
        label = "Test case step/action reference"
        location = "Test case step/action reference"
    elif ui_scope["ui_scope"] == "itest_command_reference":
        key = "itest_command_reference"
        label = "iTest command reference"
        location = "iTest command reference"
    else:
        key = ui_scope["ui_scope"]
        label = ui_scope["ui_scope_label"]
        location = ui_scope["ui_scope_label"]

    return {
        "ui_surface": key,
        "ui_surface_label": label,
        "ui_location": location,
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


def build_surface_summary(results):
    seen = {}
    order = []
    for result in results:
        surface = result["ui_surface"]
        if surface not in seen:
            seen[surface] = {
                "ui_surface": surface,
                "ui_surface_label": result["ui_surface_label"],
                "count": 0,
                "examples": [],
            }
            order.append(surface)
        seen[surface]["count"] += 1
        if len(seen[surface]["examples"]) < 3:
            seen[surface]["examples"].append(result["source_ref"])
    return [seen[surface] for surface in order]


def mixed_scope_warning(query_terms, scope_summary):
    if len(scope_summary) <= 1:
        return ""

    terms = set(query_terms)
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
    if terms & SENSITIVE_SCOPE_TERMS or any(item["ui_scope"] in sensitive_scopes for item in scope_summary):
        return "Search results span multiple UI or product scopes; separate the answer by location/scope or refine with --scope."
    return ""


def build_field_stats(pages, query_terms):
    terms = set(query_terms)
    doc_fields = []
    doc_frequency = Counter()
    total_lengths = Counter()

    for page in pages:
        field_stats = {}
        doc_terms = set()
        texts = page_source_texts(page)
        for field in MATCH_SOURCE_ORDER:
            tokens = tokenize(texts[field])
            counts = Counter(token for token in tokens if token in terms)
            field_stats[field] = {
                "length": len(tokens),
                "counts": counts,
            }
            total_lengths[field] += len(tokens)
            doc_terms.update(counts)
        doc_frequency.update(doc_terms)
        doc_fields.append(field_stats)

    document_count = max(len(pages), 1)
    average_lengths = {
        field: max(total_lengths[field] / document_count, 1.0)
        for field in MATCH_SOURCE_ORDER
    }
    return doc_fields, doc_frequency, average_lengths


def bm25f_scores(pages, query_terms):
    doc_fields, doc_frequency, average_lengths = build_field_stats(pages, query_terms)
    document_count = max(len(pages), 1)
    scores = defaultdict(float)

    for doc_id, field_stats in enumerate(doc_fields):
        score = 0.0
        for term in query_terms:
            df = doc_frequency.get(term, 0)
            if df <= 0:
                continue
            idf = math.log(1.0 + (document_count - df + 0.5) / (df + 0.5))
            term_score = 0.0
            for field, stats in field_stats.items():
                tf = stats["counts"].get(term, 0)
                if tf <= 0:
                    continue
                length = max(stats["length"], 1)
                average_length = average_lengths[field]
                denominator = tf + BM25_K1 * (
                    1.0 - BM25_B + BM25_B * (length / average_length)
                )
                term_score += FIELD_WEIGHTS[field] * ((tf * (BM25_K1 + 1.0)) / denominator)
            score += idf * term_score
        if score > 0:
            scores[doc_id] = score * 100.0

    unmatched_terms = [term for term in query_terms if doc_frequency.get(term, 0) <= 0]
    return scores, unmatched_terms


def rule_matches(rule, query_terms, query_phrase_text=""):
    terms = set(query_terms)
    all_terms = set(rule.get("all_terms", []))
    any_terms = set(rule.get("any_terms", []))
    not_terms = set(rule.get("not_terms", []))
    if not all_terms <= terms:
        return False
    if any_terms and not any_terms & terms:
        return False
    if not_terms and not_terms & terms:
        return False
    all_phrases = [normalized_phrase(phrase) for phrase in rule.get("all_phrases", [])]
    any_phrases = [normalized_phrase(phrase) for phrase in rule.get("any_phrases", [])]
    not_phrases = [normalized_phrase(phrase) for phrase in rule.get("not_phrases", [])]
    if all_phrases and not all(phrase in query_phrase_text for phrase in all_phrases):
        return False
    if any_phrases and not any(phrase in query_phrase_text for phrase in any_phrases):
        return False
    if not_phrases and any(phrase in query_phrase_text for phrase in not_phrases):
        return False
    return True


def source_to_doc_id_map(pages):
    return {
        page_source_ref(page).replace("\\", "/"): doc_id
        for doc_id, page in enumerate(pages)
    }


def apply_source_rules(scores, pages, query_terms, query_phrase_text, rules):
    source_map = source_to_doc_id_map(pages)
    for rule in rules.get("source_rules", []):
        if not rule_matches(rule, query_terms, query_phrase_text):
            continue
        for source_ref, boost in rule.get("sources", {}).items():
            doc_id = source_map.get(source_ref)
            if doc_id is not None:
                scores[doc_id] += float(boost)


def phrase_matches_query(rule, query_terms, query_phrase_text):
    return rule_matches(rule, query_terms, query_phrase_text)


def apply_canonical_phrase_rules(scores, pages, query_terms, query_phrase_text, rules):
    for rule in rules.get("canonical_phrases", []):
        if not phrase_matches_query(rule, query_terms, query_phrase_text):
            continue
        source_refs = set(rule.get("source_refs", []))
        ui_surfaces = set(rule.get("ui_surfaces", []))
        ui_scopes = set(rule.get("ui_scopes", []))
        boost = float(rule.get("boost", 0))
        if boost == 0:
            continue
        for doc_id, page in enumerate(pages):
            source_ref = page_source_ref(page).replace("\\", "/")
            ui_scope = infer_ui_scope(page)
            ui_surface = infer_ui_surface(page, ui_scope)
            if (
                source_ref in source_refs
                or ui_surface["ui_surface"] in ui_surfaces
                or ui_scope["ui_scope"] in ui_scopes
            ):
                scores[doc_id] += boost


def needs_surface_diversity(query_terms):
    return bool(set(query_terms) & SENSITIVE_SCOPE_TERMS)


def page_similarity(left, right):
    left_scope = infer_ui_scope(left)
    right_scope = infer_ui_scope(right)
    left_surface = infer_ui_surface(left, left_scope)
    right_surface = infer_ui_surface(right, right_scope)
    if left_surface["ui_surface"] == right_surface["ui_surface"]:
        return 1.0
    if left_scope["ui_scope"] == right_scope["ui_scope"]:
        return 0.35
    left_top = set(left.get("toc_top_categories", []))
    right_top = set(right.get("toc_top_categories", []))
    if left_top and left_top & right_top:
        return 0.30
    if left.get("doc_set") and left.get("doc_set") == right.get("doc_set"):
        return 0.20
    return 0.0


def rerank_scope_diverse(candidates, pages, query_terms, top, scope=None):
    ranked = sorted(candidates, key=lambda item: item[1], reverse=True)
    if scope or not needs_surface_diversity(query_terms) or top <= 1:
        return ranked[:top]

    best_score = ranked[0][1] if ranked else 0
    if best_score <= 0:
        return ranked[:top]

    pool_floor = best_score * MMR_POOL_FLOOR_RATIO
    pool = [(doc_id, score) for doc_id, score in ranked if score >= pool_floor]
    if not pool:
        return ranked[:top]

    selected = [pool[0]]
    selected_doc_ids = set()
    selected_doc_ids.add(pool[0][0])

    while len(selected) < top:
        best_candidate = None
        best_mmr_score = None
        for doc_id, score in pool:
            if doc_id in selected_doc_ids:
                continue
            relevance = score / best_score
            diversity_penalty = max(
                page_similarity(pages[doc_id], pages[selected_doc_id])
                for selected_doc_id, _ in selected
            )
            mmr_score = MMR_LAMBDA * relevance - (1.0 - MMR_LAMBDA) * diversity_penalty
            if best_mmr_score is None or mmr_score > best_mmr_score:
                best_mmr_score = mmr_score
                best_candidate = (doc_id, score)
        if best_candidate is None:
            break
        selected.append(best_candidate)
        selected_doc_ids.add(best_candidate[0])
        if len(selected) >= top:
            return selected

    for doc_id, score in ranked:
        if doc_id in selected_doc_ids:
            continue
        selected.append((doc_id, score))
        if len(selected) >= top:
            break

    return selected


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
    pages = load_pages(data_dir)
    rules = load_search_rules(data_dir)
    property_index = load_property_index(data_dir)
    tokens = tokenize(query)
    query_terms = sorted(set(tokens))
    query_phrase_text = " ".join(tokens)
    scores, unmatched_terms = bm25f_scores(pages, query_terms)

    phrase = query.lower().strip()
    for doc_id in list(scores.keys()):
        page = pages[doc_id]
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
            scores[doc_id] += 60
        elif phrase and phrase in metadata_haystack:
            scores[doc_id] += 1100 if is_identifier_query(phrase) else 8

    apply_source_rules(scores, pages, query_terms, query_phrase_text, rules)
    apply_canonical_phrase_rules(scores, pages, query_terms, query_phrase_text, rules)

    match_profiles = {}
    for doc_id in list(scores.keys()):
        match_profile = analyze_match_sources(pages[doc_id], query, query_terms)
        match_profiles[doc_id] = match_profile

    if scope and scope not in UI_SCOPE_DETAILS:
        raise ValueError(f"Unknown UI scope: {scope}")

    candidates = []
    for doc_id, score in scores.items():
        ui_scope = infer_ui_scope(pages[doc_id])["ui_scope"]
        if scope and ui_scope != scope:
            continue
        candidates.append((doc_id, score))

    ranked = rerank_scope_diverse(candidates, pages, query_terms, top, scope)
    results = []
    for doc_id, score in ranked:
        page = pages[doc_id]
        ui_scope = infer_ui_scope(page)
        ui_surface = infer_ui_surface(page, ui_scope)
        match_profile = match_profiles[doc_id]
        property_poc = property_poc_for_page(page, property_index)
        result_matched_terms = sorted(set(match_profile["matched_terms"]))
        results.append(
            {
                "score": int(round(score)),
                "file_name": page["file_name"],
                "relative_path": page.get("relative_path", page["file_name"]),
                "title": page["title"],
                "h1": page["h1"],
                "doc_set": page["doc_set"],
                "probable_category": page["probable_category"],
                **ui_scope,
                **ui_surface,
                "toc_primary_path": page.get("toc_primary_path", ""),
                "toc_top_categories": page.get("toc_top_categories", []),
                "toc_paths": page.get("toc_paths", []),
                "index_terms": page.get("index_terms", [])[:24],
                "index_paths": page.get("index_paths", [])[:8],
                "context_ids": page.get("context_ids", [])[:12],
                "context_labels": page.get("context_labels", [])[:12],
                "matched_terms": result_matched_terms,
                "match_sources": match_profile["match_sources"],
                "match_source_summary": format_match_sources(match_profile),
                "metadata_only_match": match_profile["metadata_only"],
                "metadata_exact_match": match_profile["metadata_exact_only"],
                "has_page_text_match": match_profile["has_page_text_match"],
                "evidence_note": match_profile["evidence_note"],
                "property_poc": property_poc,
                "unmatched_terms": unmatched_terms,
                "snippet": compact_snippet(page.get("text", ""), query, tokens),
                "source_ref": page.get("source_ref", page["file_name"]),
            }
        )
    scope_summary = build_scope_summary(results)
    surface_summary = build_surface_summary(results)
    return {
        "query": query,
        "query_terms": query_terms,
        "unmatched_terms": unmatched_terms,
        "scope_filter": scope or "",
        "scope_summary": scope_summary,
        "surface_summary": surface_summary,
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
    if response.get("surface_summary") and response["mixed_scope_warning"]:
        print(
            "ui surfaces: "
            + "; ".join(
                f"{item['ui_surface_label']} ({item['count']})"
                for item in response["surface_summary"]
            )
        )
    if response["mixed_scope_warning"]:
        print(f"warning: {response['mixed_scope_warning']}")

    for rank, result in enumerate(response["results"], start=1):
        print(f"{rank}. [{result['score']}] {result['source_ref']}")
        print(f"   title: {result['title']}")
        print(f"   scope: {result['ui_scope_label']} ({result['ui_scope']})")
        print(f"   location: {result['ui_location']}")
        print(f"   matches: {result['match_source_summary']}")
        print(f"   evidence: {result['evidence_note']}")
        if result.get("property_poc"):
            print(
                "   property poc: "
                + format_property_poc(result["property_poc"], response["query_terms"])
            )
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
