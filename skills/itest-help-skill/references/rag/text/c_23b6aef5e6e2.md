# Analysis Rules: Validating Responses > The structure of an analysis rule > The extractor

The extractor is the first line in the rule — it specifies how to extract (return) a value from the response and what to extract.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- How to extract the value appears in the Action cell. In the example, we use a regex (regular expression) extractor to extract the value. Alternatively, you can use the query extractor or the contains extractor that extracts the text string that you specify. Some extractor types can return multiple values.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- What to extract appears in the Description cell. In the example, it is the regular expression that defines the text to extract from the response.

Limitations

The following limitations apply for the data extracted for each execution:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Total elements stored: A maximum of 128 extracted data items per execution.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Bytes stored: A maximum of 128 characters of any tag or value. Any tag or value that exceeds 128 characters will be truncated.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Array elements stored: Any extracted data item whose value is an array that exceeds 128 items will be rejected (discarded).
