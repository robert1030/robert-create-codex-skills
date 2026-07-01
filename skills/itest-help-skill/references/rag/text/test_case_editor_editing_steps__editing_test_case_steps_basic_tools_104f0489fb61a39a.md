---
{
  "chunk_id": "test_case_editor_editing_steps__editing_test_case_steps_basic_tools_104f0489fb61a39a",
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
    "Editing test case steps: Basic tools"
  ],
  "anchor": "1284452",
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
    "test_case_editor_steps_page.htm#1284516",
    "tce_steps_page.htm#1819934"
  ],
  "images": [
    "topics/images/test_case_editor.1.jpg"
  ],
  "content_hash": "104f0489fb61a39a",
  "level": 1
}
---

# Editing test case steps: Basic tools > Editing test case steps: Basic tools

Use the Steps page on the Test Case editor to edit steps. (Click the Steps tab to open the Steps page.)

- Each step is identified by a unique Step ID number in the second column. You can set a preference to display or hide the IDs on the page. Click Window > Preferences. In the iTest group, go to Editors > Test Case Editor and specify the setting.

- When you select one or more steps on the Steps page, the Step Properties section enables you to view and edit property setting for the selected steps. In the example, the shutdown step is selected; in the Step Properties section, the General properties group is selected. Any changes to the property settings apply to the shutdown step. So, to edit a step, select it and modify its properties (in the Step Properties section of the page).

| Note: You may open the context specific information—Step Properties section in the Properties pane as follows. Right-click to display the menu and select “Show Properties View”. OR Click the ellipsis on the step command, where applicable. |
| --- |

- To edit multiple steps, select them and change a setting; the setting applies to all selected steps. The same applies to steps that are indented under another step (steps can even be indented under a comment) — any property settings that you make to the parent step apply to the children.)

- Undo/redo (Ctrl-Z, Ctrl-Y) (OPTION-Z, OPTION-Y on macOS) applies to any change, including table operations like moving steps.

- Steps can occur in any number of sessions as long as an open step appears as the first step for each session.

- Procedure names are case-sensitive. The procedures cleanup and Cleanup are different procedures.

- You can copy/paste commands from a text or word file into a test case. The steps are added as commands after the selected steps.

- Test case files use the .fftc filename extension

When there is a non-standard property setting or a problem with a step, a marker appears in the first column. See Markers for steps (step validation).

![screenshot](topics/images/test_case_editor.1.jpg) <!-- image_chunk: img_95cf4f031adc1681 -->
