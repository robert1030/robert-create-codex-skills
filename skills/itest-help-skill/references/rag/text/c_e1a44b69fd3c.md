# Response Maps: Returning Data from Responses > Overview: Creating a response map > Watch the video > Limitations of the Auto-mapping feature

![*](bullet_blue.jpg) <!-- image_ref -->

- Auto-mapping does not find tables where the row count is less than or equal to 2.

![*](bullet_blue.jpg) <!-- image_ref -->

- Auto-mapping does not process responses larger than 250 lines.

![*](bullet_blue.jpg) <!-- image_ref -->

- Auto-mapping can become confused by table rows that wrap onto a newline. This is a tricky problem to map manually as well. We recommend that you increase the terminal width so that response does not wrap on a new line.

An alternative is to create a new response map from scratch. You select File > New > iTest > Response Map from the main menu. This will create a new response map file at the location you request but will not populate it in any way.



Step 4: Choose mapping technology

iTest response maps can use different mapping technologies to return structured data from the unstructured textual response. There are three types of mapping currently supported: pattern-based, table-based, and block-based. Each of these technologies is optimized for different types of responses. You can combine these if your response contains different portions that are best mapped with different technologies.
