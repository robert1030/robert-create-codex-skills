---
{
  "chunk_id": "rme_table_page__key_c096acf71a812f46",
  "source_file": "topics/rme_table_page.htm",
  "source_original_path": "topics/rme_table_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response Map editor: Table Map page"
  ],
  "heading_path": [
    "Response Map editor: Table Map page",
    "Response Map editor: Table Map page",
    "Key"
  ],
  "anchor": "1125587",
  "context_ids": [
    "rme_table_page"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "response_map_secret_type.htm#1735972"
  ],
  "images": [
    "topics/images/response_mapping.8.jpg"
  ],
  "content_hash": "c096acf71a812f46",
  "level": 2
}
---

# Response Map editor: Table Map page > Response Map editor: Table Map page > Key

When you check the Key option and provide a Sample Key Value, iTest uses the value in the column to find particular rows in the table.

Check the Key checkbox and provide a Sample Key Value to use the value of the token as the key to identify the instance of a repeating block in the response that contains the value that you want to extract. iTest uses the Key token to auto-generate aliases for the other tokens in the block.

In this example, we defined PathCost as a key token:

1. 1

1. The PathCost token is the Key. Whenever a PathCost value exceeds 25, then the RoleByPathCost query returns the value in that row for the Role token.

1. 2

1. The PathCost token in this row exceeds 25, so the RoleByPathCost query returns the value in this row for the Role token: TRI.

| Key | Type or paste a sample value that is used to identify the token of interest. |
| --- | --- |
| Include the column in the Structured data | Available only when Key is not selected. |
| Secret: Hide the value in views and reports | Select Secret: Hide the values in views and reports to hide the custom queries defined as Secret. |
| Create a query for extracting all values appearing in this column | Select to automatically create a query for extracting all values appearing in this column. |
| Parse cell contents | Divide contents into separate tokens based on parsing rules. This setting enables you to extract multiple values from a single cell if the value cannot otherwise be recognized. |
| If cell is missing or empty | For empty cells, you can either insert a default values or send an error message to the Execution view and test report. If you select UseDefaultValue, then specify a Default value. If you select Error option, only the Step issues view and Error log view are affected and indicates an error (the Query view displays a blank). |
|  | If you select UseDefaultValue, then specify a Default value. |
|  | If you select Error option, only the Step issues view and Error log view are affected and indicates an error (the Query view displays a blank). |
| If cell has this value | Use this option to replace certain values with the value specified in Translate to. |
| When cell contents spill over | (Applies only if you have specified Positional — strict column widths based on character counts — to determine column boundaries. Steal: The right column uses the spillover data from the left column. Extend: The left column retains all data in the cell. |
| Auto populate empty fields | Select Auto-populate empty fields, empty cell will be populated with non empty values from the previous row (that is, from the row above the current row). |
| Custom queries | Allows you to create several simple keys (one field) and compound keys (from several fields). For example: If your table column has 4 keys: VLAN, IP_Address, MAC, flags You may create two keys as follows: Simple key with one filed: MAC Compound key with two fields: VLAN and IP_Address That is, to create queries as follows. //row[VLAN='{0}' and IP_Address='{1}']/MAC //row[VLAN='{0}' and IP_Address='{1}']/flags //row[MAC='{0}']/VLAN //row[MAC='{0}']/IP_Address //row[MAC='{0}']/flags Create Query List: Click Add. The label Indefinite Key appears in the Query column Click Indefinite Key and the Select key column lists the current keys (column names). Click on the required key in the Select key column and it appears in the Query column. To see how the Secret type appears on the Response, Structure, and Query views, see Response Map Editor: Secret Type. To see how this secret type is applied in REST interactive sessions, see Apply Custom Response Maps to interactive REST session responses, “REST sessions”. Click on another key in the Select key column to create a compound/combined key Note You may add multiple keys, delete, or move the keys up/down as required. |
|  | Click Add. The label Indefinite Key appears in the Query column |
|  | Click Indefinite Key and the Select key column lists the current keys (column names). |
|  | Click on the required key in the Select key column and it appears in the Query column. |
|  | Click on another key in the Select key column to create a compound/combined key |
| Note | You may add multiple keys, delete, or move the keys up/down as required. |
| Use the last column as a template for additional identical columns | Some tables have an indefinite number of columns and expand to the right as needed. For example, the response to a GetStats command can have as many columns as the number of ports in a multi-card device. To allow for this possibility, check The last column may repeat. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/response_mapping.8.jpg) <!-- image_chunk: img_5c12c4d5103cc8a8 -->
