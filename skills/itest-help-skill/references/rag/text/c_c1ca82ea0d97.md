# Charting Test Case Data > Charting test case data > Overview of the process of creating and viewing a chart

To generate a chart, you follow this overall process:

![*](bullet_blue.jpg) <!-- image_ref -->

1. Set Charting View Preferences. Go to Setting preferences for Charting View and select the chart color.

1. 2 Decide what you want to chart and therefore which values to extract. To view a time-series, you'll need to repeat the step that generates the value (typically by placing it within a loop). To view one value as a function of another, you'll need to extract one value, store it using an analysis rule, and then extract the other value. You can use any type of extractor to extract values; Regex, queries based on a response map,

1. 3 Execute the test case so that iTest has an example response for the step.

1. 4 Create an analysis rule. In the Response view, select the value to chart and then right-click to create an analysis rule that extracts the value and applies the appropriate chart processor (X-Y, bar, pie).

1. 5 Specify property settings for the chart.

1. 6 Open the Charts view.

1. 7 Execute the test case. Chart values are updated in real time and the chart remains visible when execution stops. If you chart a value for a long-running test, you can specify how much of the most recent data the chart should display.
