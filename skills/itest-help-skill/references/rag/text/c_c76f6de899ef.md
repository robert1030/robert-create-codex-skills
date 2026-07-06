# Analysis Rules: Validating Responses > Adding and working with Global analysis rules > Adding a Global analysis rule

1. 1 In the editor, click the Global Rules tab.

![](images/analysis_rules.01.jpg) <!-- image_ref -->

1. 2 Click Add . iTest adds a default rule.

1. 3 Click in the Extract using cell to select an extractor type for the rule. Based on your selection, iTest places default text in the What to extract cell. Replace the text with the value that the extractor should use to get the data from the response.

![](images/analysis_rules.02.jpg) <!-- image_ref -->

Important For query extractors, do not use right-click to insert a query value into the What to Extract cell. Instead, paste or type a query from the Queries view.

1. 4 Click in the Perform cell to select a processor type for the rule. Based on your selection, iTest places default text in the Details cell. If appropriate, replace the text with the value that the processor should use to process the data that is returned by the extractor.

![](images/analysis_rules.03.jpg) <!-- image_ref -->

1. 5 Now, you have the option to modify the property settings of the rule’s extractors and processors. Click More to open the Analysis Rule Properties section. In the example, we selected Regex so that we could edit the properties associated with the Regex extractor. For details, see Analysis rules: Properties of the extractor and Analysis rules: Properties of the processor.

![](images/analysis_rules.04.jpg) <!-- image_ref -->

1. 6 Optional: You can use the Skip check box or Skip to skip the rule while developing/debugging a test case.

![](images/analysis_rules.05.jpg) <!-- image_ref -->

![](images/analysis_rules.06.jpg) <!-- image_ref -->

1. 7 Optional: You can use Move Up/Move Down to move a selected rule in the list. Rules are applied in the listed order.
