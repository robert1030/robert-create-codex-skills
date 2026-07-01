---
{
  "chunk_id": "test_case_editor_find_replace_tce_dialog__finding_and_replacing_text_in_test_case__b2a5729f77ae8704",
  "source_file": "topics/test_case_editor_find_replace_tce_dialog.htm",
  "source_original_path": "topics/test_case_editor_find_replace_tce_dialog.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "Overview",
    "Finding and replacing text in test case steps"
  ],
  "heading_path": [
    "Finding and replacing text in test case steps",
    "Finding and replacing text in test case steps"
  ],
  "anchor": "1288849",
  "context_ids": [
    " test_case_editor_find_replace_tce_dialog"
  ],
  "index_keywords": [
    "editing",
    "in test case steps",
    "test case steps"
  ],
  "index_keyword_paths": [
    "editing > test case steps",
    "find and replace > in test case steps",
    "steps > editing",
    "test case steps > editing"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "b2a5729f77ae8704",
  "level": 1
}
---

# Finding and replacing text in test case steps > Finding and replacing text in test case steps

On the Test Case editor Steps page, select Edit > Find/Replace (keyboard shortcut Ctrl+F) (OPTION-F on macOS) to search for and replace specific text in the Action, Session, or Description cells.

- You can specify which columns to include or exclude from the find process.

- The find/replace process finds text in any line of multi-line commands. For multi-line commands, the Command dialog box opens during the find/replace process, and the process will not continue until the dialog box is closed. Replace All does not require that the dialog box opens.

- The replace functionality is undo‑able.

| Find | Specify the text to find. |
| --- | --- |
| Replace With | Specify the text that should replace the text in the Find field. The text is replaced when you click Replace/Find, Replace, or Replace All. |
| Direction | Specify whether to search Forward or Backward from the cursor position. See the Wrap search option. |
| Scope | All: Search all properties in all steps in the test case. Selected Items: Search all properties in the selected test case steps. Note If you select a step that is collapsed (other steps are nested under the step, but are currently folded away), then only the selected step and not the nested steps are searched. To include the nested steps in the search, click Expand All before performing the Find process. |
| Note | If you select a step that is collapsed (other steps are nested under the step, but are currently folded away), then only the selected step and not the nested steps are searched. To include the nested steps in the search, click Expand All before performing the Find process. |
| Options | Case-sensitive: Matches must use the identical case as the text in the Find field. Wrap search: This option ensures that the entire test case document is searched in the case that you start a search in the “middle”. When the find/replace process reaches the end of the document (Direction property = Forward) or the beginning of the document (Direction property = Backward), the search continues. Whole word: Matches must be the text in the Find field surrounded by whitespace. Regular expression: Interpret the text in the Find field as a regex. |
| Include Properties | Check an item to perform the find process in the selected column of cells. Each match may include all or a portion of the text in the cell. Matches may not span property (cell) boundaries, with the following exception: The Description field is not actually a property but is sometimes a collection of property settings. (For example, for CLI session types, Description displays the content of the Command property. For Web, Swing, and Flex sessions, it displays the Target, followed by the Command.) For the find/replace process, Description is considered to be a property, so all affected properties are searched/replaced as is appropriate. If a step's Description is not editable then the Description cell will not be consider for that step. |
| Find | Find the next instance of the text specified in the Find field. |
| Replace/Find | Replace the currently selected text with the text specified in the Replace With field and then select the next instance of the text that you specified in the Find field. |
| Replace | Replace the currently selected text with the text specified in the Replace With field. |
| Replace All | Replace all instances of the text specified in the Find field with the text specified in the Replace With field. Replace All supports multi-line commands. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
