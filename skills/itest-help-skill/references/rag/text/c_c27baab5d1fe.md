# Response Maps: Returning Data from Responses > Mapping JSON responses

iTest understands JSON structured data, maps a JSON response without requiring a response map. The structured data root for JSON responses is: mapped/Json/

A simple JSON object {name:"value1"} is structured: mapped/Json/name

A simple JSON array ["value1", "value2"] is structured: mapped/Json/item[]

The iTest JSON mapper is more tolerant than the JSON specification.

> **Note：** Note ​Empty ("") JSON object name will be replaced with the special word, "iTestEmptyXmlKeyName" in structured response.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- An extra comma (,) may appear just before the closing bracket.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The null value will be inserted when there is, (comma) elision.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Strings may be quoted with ' (single quote).

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Strings are not required to be quoted under these conditions.

If they do not:

![*](bullet_blue.jpg) <!-- image_ref -->

- begin with a quote or single quote, do not contain leading or trailing spaces

![*](bullet_blue.jpg) <!-- image_ref -->

- contain any of these characters: { } [ ] / \ : , = ; #

![*](bullet_blue.jpg) <!-- image_ref -->

- look like numbers and if they are not the reserved words true, false, or null.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Values can be separated by ; (semicolon) as well as by a , (comma).

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Numbers may have the 0- (octal) or 0x- (hex) prefix.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Comments written in the slash-slash, slash-star, and hash conventions are ignored.
