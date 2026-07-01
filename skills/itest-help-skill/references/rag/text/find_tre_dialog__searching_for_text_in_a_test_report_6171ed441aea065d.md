---
{
  "chunk_id": "find_tre_dialog__searching_for_text_in_a_test_report_6171ed441aea065d",
  "source_file": "topics/find_tre_dialog.htm",
  "source_original_path": "topics/find_tre_dialog.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Reports",
    "Test reports overview",
    "Searching for text in a test report"
  ],
  "heading_path": [
    "Searching for text in a test report",
    "Searching for text in a test report"
  ],
  "anchor": "1438388",
  "context_ids": [
    "find_tre_dialog"
  ],
  "index_keywords": [
    "finding text in",
    "in Response view",
    "in test report steps"
  ],
  "index_keyword_paths": [
    "find > in Response view",
    "find > in test report steps",
    "test reports > finding text in"
  ],
  "related_links": [],
  "images": [
    "topics/images/test_reports_3.1.jpg"
  ],
  "content_hash": "6171ed441aea065d",
  "level": 1
}
---

# Searching for text in a test report > Searching for text in a test report

While viewing a test report, use the Test Report Find dialog box (Ctrl-F or Edit > Find) to find text in the report and in the views that provide information about test results: Response view, Step Issues view, and Structure view.

- You can specify which columns of the report to include or exclude from the Find process. In addition, you can include or exclude particular views.

- When a match is found in the report steps, the matching text is highlighted.

- When found in the Response view, the view is displayed and the matching text is highlighted.

- When found in the Structure view or Steps Issues view, the view is displayed and the row is highlighted.

- The status bar provides information about what was found.

- Because test reports are read-only, Replace operations are not supported.

| Find | Specify the text to find. You can provide specialized text — see the Options properties. |
| --- | --- |
| Replace With | Because test reports are read-only, Replace operations are not supported. |
| Direction | Specify whether to search Forward or Backward from the cursor position. See the Wrap search option. Forward searches always begin at the beginning of the Executed Steps section of the report. Note You cannot search backward when a single step is selected. |
| Note | You cannot search backward when a single step is selected. |
| Scope | All steps: Search all rows in the report. Selected step: Search all properties and views for the selected step and its child steps only. |
| Options | Case-sensitive: Matches must use the identical case as the text in the Find field. Does not apply if you check the Regular expression checkbox. Whole word: Matches must be the text in the Find field surrounded by whitespace. Does not apply if you check the Regular expression checkbox. Regular expression: Interpret the text in the Find field as a regex. Wrap search: This option ensures that all specified items are searched in the case that you start a search in the “middle”. When the Find process reaches the end of the document (Direction property = Forward) or the beginning of the document (Direction property = Backward), the search continues. |
| Include Properties | Check an item to perform the Find process in the selected column of cells. Default: Action, Session, and Description. Each match may include all or a portion of the text in the cell. The Find process can find text in only the first line of multi-line commands (that is, text cannot be found in the body of a multi-line command). Matches may not span property (cell) boundaries, with the following exception: The Description field is not actually a property but is sometimes a collection of property settings. (For example, for CLI session types, Description displays the content of the Command property.) For the Find process, Description is considered to be a single property, so all affected properties settings are searched. |
|  | Each match may include all or a portion of the text in the cell. |
|  | The Find process can find text in only the first line of multi-line commands (that is, text cannot be found in the body of a multi-line command). |
|  | Matches may not span property (cell) boundaries, with the following exception: |
| Include Views | Check a view to perform the Find process in the view. Default: Response view |

![screenshot](topics/images/test_reports_3.1.jpg) <!-- image_chunk: img_5e33a8d3f10f1b4d -->
