---
{
  "chunk_id": "itestrt_commands__test_report_comparison_6b7d21c34568836d",
  "source_file": "topics/itestrt_commands.htm",
  "source_original_path": "topics/itestrt_commands.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Runtime: iTestRT",
    "iTestRT command reference"
  ],
  "heading_path": [
    "iTestRT command reference",
    "iTestRT command reference",
    "Test Report Comparison"
  ],
  "anchor": "1253784",
  "context_ids": [
    "itestrt_commands"
  ],
  "index_keywords": [
    "command reference",
    "iTestRT",
    "iTestRT command reference"
  ],
  "index_keyword_paths": [
    "command reference > iTestRT",
    "iTest Runtime > iTestRT command reference",
    "iTestRT > command reference"
  ],
  "related_links": [
    "tr_comparison_editor.htm#1466805",
    "#1227693",
    "#1227731"
  ],
  "images": [],
  "content_hash": "6b7d21c34568836d",
  "level": 2
}
---

# iTestRT command reference > iTestRT command reference > Test Report Comparison

The reportcomparison.comparereports option compares two test reports and generates a “diff” report that shows the differences between the two reports. More details on comparing reports appears in Comparing (“diffing”) two test reports.

The comparereports command uses the following options:

- Test Report options specify report format and location (see Test Report options)

- Test report database options configure the report database options (see Test report database options)

> **Note:** Note You must specify the --configonly database option to configure the test report database properly for this option. See Test report database options.

The long forms of option names begin with: --com.fnfr.open.runtime.reportcomparison.

| --comparereports SourceID,TargetID | SourceID and TargetID are the comma‑separated report IDs of source and target reports that should be compared. |
| --- | --- |
