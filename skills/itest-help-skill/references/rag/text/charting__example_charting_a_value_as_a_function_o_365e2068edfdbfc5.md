---
{
  "chunk_id": "charting__example_charting_a_value_as_a_function_o_365e2068edfdbfc5",
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
    "Example: Charting a value as a function of time"
  ],
  "anchor": "1176247",
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
  "images": [
    "topics/images/chart_steps.png",
    "topics/images/chart_using_xy_property_group.png"
  ],
  "content_hash": "365e2068edfdbfc5",
  "level": 2
}
---

# Charting test case data > Charting test case data > Example: Charting a value as a function of time

Let's work through an example of charting a value as it changes over time (that is, charting the value as a function of time — a time series).

Our example test case opens a session with a device and then submits a command that requests IP traffic values. The step is contained within a for loop that repeats the command x times.

As a result, we might expect that the device should respond with ten different values, one for each time that the step executes.

You may also select the step so we can view the most recent response in the Response view, select the value to chart, right-click the value to add an analysis rule that extracts the value and charts it (Quick Analysis Rule > Regular expression>).

> **Note:** Note iTest adds the analysis rule and the Perform action charts the value.

Select the Step Chart_as_xy, click open the Processor Properties section. Click the Chart Using XY property group.

The Chart name property is iTest's identifier for this chart — analysis rules specify a particular Chart name to add data to a particular chart. This is helpful when several variables appear on a single chart or when you will chart multiple values on independent charts during execution.

- Enter a Title for the graph and label the X axis and Y axis.

- Select Highlight Line Chart Data Points to mark each data point (round dots) on line charts. Highlight Line Chart Data Points is not selected by default.

> **Note:** Note When iTest extracts a value using an analysis rule, it puts the value into a variable named value. You can also set the extractor to none and use any expression or variable to extract data.

The Y value expression property value is y[i] — the extracted value for received packets. The X value expression property is x[i]. If you do not specify a value for the value along the X axis (the independent variable), then iTest plots time on the X axis.

Open the Charts view and then save and execute the test case. The data is charted during execution and remains in view when execution stops.

![diagram](topics/images/chart_steps.png) <!-- image_chunk: img_3793debf7a3d85ea -->

![diagram](topics/images/chart_using_xy_property_group.png) <!-- image_chunk: img_5c9af6ca972bb28b -->
