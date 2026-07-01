---
{
  "chunk_id": "charting__overview_of_the_process_of_creating_and__f9bda93877ff6621",
  "source_file": "topics/charting.htm",
  "source_original_path": "topics/charting.htm",
  "toc_path": [
    "iTest Online Help",
    "Charting Test Case Data",
    "Charting test case data"
  ],
  "heading_path": [
    "Charting test case data",
    "Charting test case data",
    "Overview of the process of creating and viewing a chart"
  ],
  "anchor": "1176237",
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
  "related_links": [
    "chart_setting_preferences.htm#1374305"
  ],
  "images": [],
  "content_hash": "f9bda93877ff6621",
  "level": 2
}
---

# Charting test case data > Charting test case data > Overview of the process of creating and viewing a chart

To generate a chart, you follow this overall process:

1. Set Charting View Preferences. Go to Setting preferences for Charting View and select the chart color.

1. 2

1. Decide what you want to chart and therefore which values to extract. To view a time-series, you'll need to repeat the step that generates the value (typically by placing it within a loop). To view one value as a function of another, you'll need to extract one value, store it using an analysis rule, and then extract the other value. You can use any type of extractor to extract values; Regex, queries based on a response map,

1. 3

1. Execute the test case so that iTest has an example response for the step.

1. 4

1. Create an analysis rule. In the Response view, select the value to chart and then right-click to create an analysis rule that extracts the value and applies the appropriate chart processor (X-Y, bar, pie).

1. 5

1. Specify property settings for the chart.

1. 6

1. Open the Charts view.

1. 7

1. Execute the test case. Chart values are updated in real time and the chart remains visible when execution stops. If you chart a value for a long-running test, you can specify how much of the most recent data the chart should display.
