# Response Maps: Returning Data from Responses > Response Map editor: Table Map page > Note This setting is allowed only if the start of data in the table is found using a banner (as described in The first row of data appears after a banner and also later in this topic). Locating Columns > 第1段

![](images/response_mapping_6.2.jpg) <!-- image_ref -->

On this page, you specify how to recognize a new column of data in the table. We’ll refer to this example table:

There are two methods for determining column boundaries:

![*](bullet_blue.jpg) <!-- image_ref -->

- Delimited: Use whitespace characters (tabs and/or spaces) or some other specified character (for example, commas) to delimit column boundaries

- **Whitespace**：(default) A new column starts upon encountering a space or tab character. Whitespace is the most flexible setting, as it accepts tabs or spaces for separating the data entries. Our example table seems to use whitespace.
- **Tab**：A new column starts upon encountering a tab character only. Note: If you specify Tab and the table actually uses a mixture of tabs and spaces as delimiters, then the mapper will map any space characters that appear between columns as a part of the token data — probably not what you want.
- **Comma/Colon**：A new column starts upon encountering a comma/colon character only.
- **Custom**：If you specify Custom, then specify the delimiter string in the Other delimiter text box.
- **Regex**：If you specify Regex, then specify regular expression delimiter string in the Other delimiter text box.

![*](bullet_blue.jpg) <!-- image_ref -->

- Positional: Apply strict column widths based on character counts (for example, the first column is 8 characters wide, the second column is 14 characters wide, and so on).

While you work on a Table response map that uses character counts to determine column boundaries (the Positional setting), the Response view displays column markers that indicate the end of each column of data. To change the location of a column boundary, drag the marker to place it after the last character in the column, as shown in the example:

![](images/response_mapping_4.3.jpg) <!-- image_ref -->

For our example table, it seems that we could use either method. Follow these suggestions:
