---
{
  "chunk_id": "chart_properties__processors_chart_using_bar_65336be94937b8ce",
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
    "Processors > Chart Using Bar"
  ],
  "anchor": "1284756",
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
  "related_links": [],
  "images": [
    "topics/images/chart_usingBar.png"
  ],
  "content_hash": "65336be94937b8ce",
  "level": 2
}
---

# Specifying the appearance of charts: Chart properties > Specifying the appearance of charts: Chart properties > Processors > Chart Using Bar

The properties that you set in this section are represented in summary form in the Details cell of the analysis rule. You can edit the settings in either place.

| Chart name | The label that analysis rules use to refer to the chart. The label is not the Title of the chart. Instead, analysis rules from several steps and/or several analysis rules from a single step can send data to a particular chart by specifying the same Chart name. If only a single value is charted on the chart, then Chart name is unimportant. |
| --- | --- |
| Title | The text title that appears at the top of the chart when you print or view it. |
| Stacked | Checked Stacked only if you are charting more than one value. When checked, values are added to the chart |
| Use legend | Check Use Legend to display a legend that displays the color-coding used on the chart. iTest creates a unique color for each series. For example, Variable1 data points are represented by blue diamonds and variable2 data points are represented by red dots. The Legend displays the list of variables being plotted and their associated symbols. |
| X axis label | The label that should appear for the X axis (independent variable) of the chart. For example, Port Number. |
| Y axis label | The label that should appear for the Y axis (dependant variable) of the chart. For example, Dropped Packets. |
| Y axis must include zero | Specifies a value of zero for the origin of the Y axis. This is useful for expanding the scale when charting a variable with a small absolute value and a low range. |
| Category | Specify the expression for the extracted value that distinguishes a particular individual bar. One bar of each Category appears along the X axis. The bar is named using the associated Expression property setting. If you are charting one extracted value as a function of another, then specify the expression representing the values that are plotted on the X axis (the independent variable). For example, if you are charting packet loss as a function of port number, then specify the expression that represents the port number, for example $port. |
| Series name | A series is the set of values associated with a single variable. The Series name is the label for the data as it appears on the chart. All Series names appear in the legend with its associated color. See Use legend. |
| Expression | The variable name to plot on the vertical axis of the chart. Usually this will be a value extracted from the response. |
| Rotate | In the default chart orientation, bars appear to increase vertically. Check Rotate to cause bars to be displayed horizontally and increasing to the right. When a chart is rotated, each additional bar is added further in the downward direction. |

![diagram](topics/images/chart_usingBar.png) <!-- image_chunk: img_6508ea23aba47ab3 -->
