---
{
  "chunk_id": "test_case_editor_editing_steps__when_in_doubt_use_the_test_case_menu_or__d0c48873abc13700",
  "source_file": "topics/test_case_editor_editing_steps.htm",
  "source_original_path": "topics/test_case_editor_editing_steps.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "Overview",
    "Editing test case steps: Basic tools"
  ],
  "heading_path": [
    "Editing test case steps: Basic tools",
    "Editing test case steps: Basic tools",
    "When in doubt, use the Test Case menu or right-click"
  ],
  "anchor": "1820107",
  "context_ids": [
    "test_case_editor_editing_steps"
  ],
  "index_keywords": [
    "editing",
    "editing steps",
    "steps",
    "test cases"
  ],
  "index_keyword_paths": [
    "Test Case editor > editing steps",
    "editing > steps",
    "editing > test cases",
    "steps > editing",
    "test case steps > editing"
  ],
  "related_links": [
    "test_case_editor_steps_page.htm#1829061",
    "#2102914"
  ],
  "images": [
    "topics/images/right_click02.png",
    "topics/images/testcase_editor_python_info_command.png",
    "topics/images/tc_steps_hoverTDisplayCommandCode.png",
    "topics/images/tc_steps_rightClickMenuOptions.png",
    "topics/images/tc_steps_rightClickMenuOption-EditCommand.png"
  ],
  "content_hash": "d0c48873abc13700",
  "level": 2
}
---

# Editing test case steps: Basic tools > Editing test case steps: Basic tools > When in doubt, use the Test Case menu or right-click

Whenever the Test Case editor is selected, the Test Case menu appears in the menu bar. The options that appear in the menu vary depending on the editor page in use.

Most of iTest's editors and views include context (right-click) menus for common operations (most toolbar tools appear in the context menus). For example, in the Test Case editor, the menu that appears when you select the entire step differs from the menu that appears when you select the Action or the Description cell.

> **Note:** Note Depending on your selection, iTest highlights the entire step or the selected cell. See also Context (right-click) menu.

- To insert an item (for example, a variable in both Tcl and Python), select the item to replace or place the cursor at the appropriate location (e.g., the Description cell) and right-click. The following is an example of the right-click menu options in a Tcl test case.

- To insert ‘info’ commands (for both language=tcl and language=python), place your cursor in the Description cell of a test case step, right-click, select Insert > Information, and select the required command syntax. The example below shows Python information commands menu.

- Hover over the step description to view the entire contents of a multi-line code directly from the Steps > Description column of the TestCase Editor.

Hovering over the Step > Description column displays a popup with detailed information about that step and an Edit button to modify the step. If the content is exceeds the popup size, scrollbars appear automatically. The Popup appears only when you hover on step which has multi-line code.

Click Edit to display the Edit Command dialog and modify the step as required. See Edit Command Dialog below.

- You may also edit the contents of a multi-line code directly from the Steps > Description column of the TestCase editor. Right-click a cell (options: skip it, wrap it inside a loop or a comment, apply an analysis rule, edit a command, and so on), and select Edit Command.

The Edit Command dialog displays. Modify the step as required. See Edit Command Dialog below.

- Edit Command Dialog

The Edit Command Dialog displays when you:

- Click Edit on the popup displayed (when hovering over a multi-line command step)

or

- Right-click on the command step and select Edit Command option.

Edit and format code as required (single-line code and multi-lines code). The Edit Command dialog automatically resizes depending on the number of code lines. A horizontal and/or a vertical scroll bar appears as required.

Click OK to save your changes or Cancel to discard the changes.

![screenshot](topics/images/right_click02.png) <!-- image_chunk: img_2782d27c801d9015 -->

![screenshot](topics/images/testcase_editor_python_info_command.png) <!-- image_chunk: img_3cc712710ba45f3b -->

![screenshot](topics/images/tc_steps_hoverTDisplayCommandCode.png) <!-- image_chunk: img_7e0e3225d25b556d -->

![screenshot](topics/images/tc_steps_rightClickMenuOptions.png) <!-- image_chunk: img_8584819709841f9c -->

![screenshot](topics/images/tc_steps_rightClickMenuOption-EditCommand.png) <!-- image_chunk: img_acbc2ee81e02a617 -->
