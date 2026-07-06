# Analysis Rules: Validating Responses > Analysis Rule Wizard: Execution Message page > 第1段

The rule will create an execution issue and associated message for display in the Execution view, the Step Issues view, and in test reports, you will now specify the details of the message. This wizard page has the effect of setting Perform (the Processor property) to message for the resulting analysis rule.

> **Note：** Note Enabling this feature inserts the tag name/value pair into ElasticSearch when running from Velocity. This may be rendered in Kibana dashboards so that you can trend measurements and results across multiple test runs. See Velocity Deployment Guide (on Spirent Knowledge Base). to set up Kibana visualization.

![](images/analysis_rules_6.1.jpg) <!-- image_ref -->

![](images/analysis_rules_5.2.jpg) <!-- image_ref -->

![](images/analysis_rules_5.3.jpg) <!-- image_ref -->

![](images/analysis_rules_4.4.jpg) <!-- image_ref -->

![](images/analysis_rules_3.5.jpg) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

$value is a iTest interpreter variable that stores the data that is extracted by the extractor. $value is created in the heap. For string comparisons, $value is 1 (True, the string matches) or 0 (zero, False) For regex, $value is the extracted value For queries, $value is the result of the query $values is a iTest interpreter variable that stores all of the extracted values in a space-separated list. If a value in the list includes spaces, then it is wrapped in double quotes (“). Note that the list is not a pure Tcl list because any quotes within a value are not escaped. $index: When the extractor extracts multiple items and the processor is invoked for each item, then $index holds the index of each value. For example, you would use a value's index to chart each extracted value on a separate line or series. $itest_value is a Tcl interpreter variable that stores the data that is extracted by the extractor.
