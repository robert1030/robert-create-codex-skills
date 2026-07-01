---
{
  "chunk_id": "charting__charting_test_case_data_3d40f697d2a1c2ad",
  "source_file": "topics/charting.htm",
  "source_original_path": "topics/charting.htm",
  "toc_path": [
    "iTest Online Help",
    "Charting Test Case Data",
    "Charting test case data"
  ],
  "heading_path": [
    "Charting test case data",
    "Charting test case data"
  ],
  "anchor": "1301973",
  "context_ids": [
    "charting"
  ],
  "index_keywords": [
    "charting",
    "charting values",
    "charting view",
    "generating from test case data"
  ],
  "index_keyword_paths": [
    "charts > generating from test case data",
    "preferences > charting view",
    "responses > charting values",
    "views > charting"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "3d40f697d2a1c2ad",
  "level": 1
}
---

# Charting test case data > Charting test case data

You can generate charts of the data returned during test execution. Charts are updated in real time and appear in the Charts view (Window > Show View >Charting).

> **Note:** Note You can chart only numeric data.

To generate a chart, you associate an analysis rule with the step. The rule generates the data to be charted. Analysis rules have two main parts:

- The extractor (the Extract using cell) that defines how to extract the value from a response (using regex or response maps, for example)

- The processor (the Perform cell) that processes the data. You'll use the chart processor to generate charts.

You can generate the following kinds of charts:

- X-Y graphs: area, line, scatter, or time series

- Bar charts

- Pie charts
