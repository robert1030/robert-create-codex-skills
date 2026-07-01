---
{
  "chunk_id": "chart_properties__processors_chart_using_xy_203c3a8cd3a0272a",
  "source_file": "topics/chart_properties.htm",
  "source_original_path": "topics/chart_properties.htm",
  "toc_path": [
    "iTest Online Help",
    "Charting Test Case Data",
    "Specifying the appearance of charts: Chart properties"
  ],
  "heading_path": [
    "Specifying the appearance of charts: Chart properties",
    "Specifying the appearance of charts: Chart properties",
    "Processors > Chart Using XY"
  ],
  "anchor": "1284700",
  "context_ids": [
    "chart_properties"
  ],
  "index_keywords": [
    "charts",
    "properties",
    "specifying the appearance of"
  ],
  "index_keyword_paths": [
    "charts > properties",
    "charts > specifying the appearance of",
    "properties > charts"
  ],
  "related_links": [
    "#1284705"
  ],
  "images": [
    "topics/images/chart_using_xy_property_group.png",
    "topics/images/chart_y_axis_zero_selected_x_axist_not_Selected.png",
    "topics/images/chart_Show_X-Axis_Seleted.png"
  ],
  "content_hash": "203c3a8cd3a0272a",
  "level": 2
}
---

# Specifying the appearance of charts: Chart properties > Specifying the appearance of charts: Chart properties > Processors > Chart Using XY

The properties that you set in this section are represented in summary form in the Details cell of the analysis rule. You can edit the settings in either place.

| Chart name | iTest's identifier for this chart — analysis rules use the Chart name to add data to this particular chart. The label is not the Title of the chart. Instead, analysis rules from several steps and/or several analysis rules from a single step can send data to a particular chart by specifying the same Chart name. If only a single value is charted on the chart, then Chart name is not used. |
| --- | --- |
| Title | The text title that should appear at the top of the chart when you print or view it. |
| Style | Select the charting style that will be used to display: AREA: Area Graphs are Line Graphs with the area below the line filled in with a certain colour or texture. Area Graphs are drawn by first plotting data points, joining a line between the points, and then filling in the space below the completed line. LINE: A line chart displays information as a series of data points called 'markers' connected by straight line segments. SCATTER:Scatter plots are similar to line graphs in that they use horizontal and vertical axes to plot data points. However, Scatter plots show how much one variable is affected by another. The relationship between two variables is called their correlation. TIME-SERIES: A time series chart, is an illustration of data points at successive time intervals. |
| X axis label | The label on the X axis of the chart. In normal orientation (not rotated), the X axis is the horizontal axis. For example, Time or Port Number. This value is also known as the independent variable. |
| Y axis label | The label on the Y axis of the chart. In normal orientation (not rotated), the X axis is the horizontal axis. For example, ICMP echo count or Lost Packets. This value is also known as the dependent variable. |
| Use legend | Check Use Legend to display a legend that displays the symbols and color-coding used on the chart. iTest creates a unique color and symbol (dot, diamond, square) combination for each series. For example, variable1 data points are represented by blue diamonds and variable2 data points are represented by red dots. The Legend displays the list of variables being plotted and their associated symbols. |
| Show Only Input X-Axis Values | Default: Unchecked Checked: The X-Axis on chart show only values from input data values. Unchecked: the chart output shows X-Axis values auto ranged and random values from minimum to maximum values from input data values. Note The Show Only Input X-Axis Values option is not applicable when Style is TIME_SERIES (Style). The option is checked or unchecked based on previous setting.and is grayed. |
| Note | The Show Only Input X-Axis Values option is not applicable when Style is TIME_SERIES (Style). The option is checked or unchecked based on previous setting.and is grayed. |
| Y Axis Must Include Zero | Specifies a value of zero for the origin of the Y axis. This is useful to expand the scale when charting a variable with a small absolute value and a low range. |
| Highlight Line Chart Data Points | Toggle to display round dots for each data point on line charts. Default: Not selected Select to display round dots on the line chart for each data point. Unselect to display the line chart without the round dots for each data point. |
|  | Select to display round dots on the line chart for each data point. |
|  | Unselect to display the line chart without the round dots for each data point. |
| Max item count | Sets the maximum number of data points allowed in the chart. Once the count of data points meets the limit, the oldest data points are deleted from the chart as the newest values are added. As a result, the chart displays only the newest data. This is useful for long-running tests. |
| Series name | The name of the variable being plotted as it should appear in the legend. See Use legend. |
| X value expression | The expression representing the values that are plotted on the X axis. By default, this is time. iTest automatically scales the time scale as needed. If you are charting the value of a single variable as a function of time, then you do not specify a value for the X value expression property. If you are charting one extracted value as a function of another, then specify the expression representing the values that are plotted on the X axis (the independent variable). For example, if you are charting packet loss as a function of port number, then specify the expression that represents the port number, for example $port. |
| Y value expression | The expression representing the values that are plotted on the Y axis. If you are charting only one value, then this is the value extracted by the analysis rule. |
| Export image width | Charts are exported as JPEG files when you export a test report into HTML. Specify the width of the JPG images in pixels. Default: 1000 |
| Export image height | Charts are exported as JPEG files when you export a test report into HTML. Specify the height of the JPG images in pixels. Default: 500 |

Example LINE chart when option Y Axis Must Include Zero is selected and Show Only Input X-Axis Values is not selected.

Example LINE chart when option Show Only Input X-Axis Values is selected and Y Axis Must Include Zero is not selected.

![diagram](topics/images/chart_using_xy_property_group.png) <!-- image_chunk: img_5c9af6ca972bb28b -->

![diagram](topics/images/chart_y_axis_zero_selected_x_axist_not_Selected.png) <!-- image_chunk: img_54fd6867c4b993e3 -->

![diagram](topics/images/chart_Show_X-Axis_Seleted.png) <!-- image_chunk: img_04fbfc2b66dac2bf -->
