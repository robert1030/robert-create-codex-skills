import argparse
import json
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
DEFAULT_DATA_DIR = SKILL_DIR / "references"

sys.path.insert(0, str(SCRIPT_DIR))
import search_help  # noqa: E402


def source_refs(response):
    return [result["source_ref"] for result in response["results"]]


def scopes(response):
    return [result["ui_scope"] for result in response["results"]]


def surfaces(response):
    return [result["ui_surface"] for result in response["results"]]


def assert_in(item, values, label):
    if item not in values:
        raise AssertionError(f"{label}: expected {item!r} in {values!r}")


def assert_true(condition, label):
    if not condition:
        raise AssertionError(label)


def run_regression(data_dir):
    checks = []

    custom = search_help.search("Custom Extractor Custom Process", data_dir, 6)
    custom_sources = source_refs(custom)
    custom_surfaces = surfaces(custom)
    assert_in("topics/arw_extractor_selection_page.htm", custom_sources, "custom extractor page")
    assert_in("topics/arw_processor_selection_page.htm", custom_sources, "custom processor page")
    assert_in("topics/parameters_custom_types.htm", custom_sources, "custom types page")
    assert_in("analysis_rule_wizard_custom_extractor", custom_surfaces, "custom extractor surface")
    assert_in("analysis_rule_wizard_processor", custom_surfaces, "processor surface")
    assert_in("parameter_custom_types", custom_surfaces, "custom types surface")
    assert_true(custom["mixed_scope_warning"], "custom query should warn about mixed scopes")
    checks.append("custom-scope-diversity")

    properties = search_help.search("Step Properties Analysis Rule Properties", data_dir, 6)
    property_sources = source_refs(properties)
    assert_in("topics/arules_processor_properties.htm", property_sources, "processor properties")
    assert_in("topics/arules_extractor_properties.htm", property_sources, "extractor properties")
    assert_true(
        any(source.startswith("topics/tce_step_properties_") for source in property_sources),
        "properties query should include Step Properties pages",
    )
    assert_true(properties["mixed_scope_warning"], "properties query should warn about mixed scopes")
    assert_true(
        any(result.get("property_poc") for result in properties["results"]),
        "properties query should include property_poc hints",
    )
    checks.append("properties-scope-diversity")

    scoped = search_help.search(
        "Step Properties Analysis Rule Properties",
        data_dir,
        6,
        scope="analysis_rule_processor_properties",
    )
    assert_true(
        all(scope == "analysis_rule_processor_properties" for scope in scopes(scoped)),
        "scope filter should only return processor/action properties",
    )
    assert_true(
        not any(source.startswith("topics/tce_step_properties_") for source in source_refs(scoped)),
        "scope filter should not include Step Properties pages",
    )
    checks.append("scope-filter")

    field_replacements = search_help.search("Field Replacements", data_dir, 3)
    assert_true(
        field_replacements["results"][0]["source_ref"] == "topics/insert_field_tool.htm",
        "Field Replacements should keep insert_field_tool top result",
    )
    assert_true(not field_replacements["mixed_scope_warning"], "Field Replacements should not warn")
    checks.append("field-replacements")

    context = search_help.search("activitywiz_topo_edit_device_session", data_dir, 3)
    assert_true(
        context["results"][0]["source_ref"] == "topics/activitywiz_topo_add_device_session.htm",
        "context id should locate activity wizard page",
    )
    assert_true(
        context["results"][0]["metadata_exact_match"],
        "context id exact match should be marked as metadata exact",
    )
    checks.append("context-metadata")

    clock = search_help.search("tcl clock scan target_date 2049 time conversion", data_dir, 4)
    clock_sources = source_refs(clock)
    assert_in("2049", clock["unmatched_terms"], "clock unmatched 2049")
    assert_in("target_date", clock["unmatched_terms"], "clock unmatched target_date")
    assert_in("topics/command_syntax.htm", clock_sources, "clock command syntax")
    assert_in("topics/command_tcl.htm", clock_sources, "tcl command")
    assert_in("topics/popups/clock.html", clock_sources, "clock popup")
    assert_true(not clock["mixed_scope_warning"], "clock query should not warn about mixed GUI scopes")
    checks.append("clock-regression")

    write_file = search_help.search(
        "writeFile processor properties Encoding",
        data_dir,
        2,
        scope="analysis_rule_processor_properties",
    )
    first = write_file["results"][0]
    assert_true(
        first["source_ref"] == "topics/arules_processor_properties.htm",
        "writeFile query should keep processor properties first",
    )
    assert_true(first.get("property_poc"), "writeFile query should include property_poc")
    sections = first["property_poc"]["sections"]
    assert_true(
        any(
            section["section"] == "writeFile processor properties"
            and "Encoding" in section["property_rows"]
            for section in sections
        ),
        "writeFile property_poc should include Encoding row",
    )
    checks.append("property-index")

    return checks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    checks = run_regression(args.data_dir)
    if args.json:
        print(json.dumps({"status": "ok", "checks": checks}, indent=2))
    else:
        print(f"OK: {len(checks)} regression checks passed")
        for check in checks:
            print(f"- {check}")


if __name__ == "__main__":
    main()
