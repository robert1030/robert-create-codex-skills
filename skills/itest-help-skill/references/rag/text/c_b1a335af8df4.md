# Analysis Rules: Validating Responses > Analysis rules: Properties of the extractor > Predefined local variables used by extractors

iTest populates predefined local variables while processing an analysis rule:

![*](bullet_blue.jpg) <!-- image_ref -->

- $value is an iTest interpreter variable that stores the data that is extracted by the extractor. $value is created in the heap.

![*](bullet_blue.jpg) <!-- image_ref -->

- For the contains extractor (string comparisons), $value is either 1 (True, the string matches) or 0 (zero, False)

![*](bullet_blue.jpg) <!-- image_ref -->

- For the regex extractor, $value is the extracted value

![*](bullet_blue.jpg) <!-- image_ref -->

- For the queries extractor, $value is the result of the query

![*](bullet_blue.jpg) <!-- image_ref -->

- $itest_value is a Tcl interpreter variable that stores the data that is extracted by the extractor. $itest_value is not thread safe. Because only one instance of the Tcl interpreter is used, if you use an analysis rule in asynchronous steps, then $itest_value can be overwritten by another thread.

![*](bullet_blue.jpg) <!-- image_ref -->

- $index is an iTest interpreter variable. When the extractor extracts multiple items and the processor is invoked for each item, then $index holds the index of each value. For example, you would use a value's index to chart each extracted value on a separate line or series.

![*](bullet_blue.jpg) <!-- image_ref -->

- $itest_index is a Tcl interpreter variable that stores the data that is extracted by the extractor. $itest_index is not thread safe. Because only one instance of the Tcl interpreter is used, if you use an analysis rule in asynchronous steps, then $itest_index can be overwritten by another thread.
