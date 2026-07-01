---
{
  "chunk_id": "tce_steps_page__test_case_editor_steps_page_1d3ee7d12a997a2e",
  "source_file": "topics/tce_steps_page.htm",
  "source_original_path": "topics/tce_steps_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "Steps page on the Test Case Editor",
    "Test Case editor: Steps page"
  ],
  "heading_path": [
    "Test Case editor: Steps page",
    "Test Case editor: Steps page"
  ],
  "anchor": "1176496",
  "context_ids": [
    "tce_steps_page"
  ],
  "index_keywords": [
    "Python Action syntax, warnings",
    "Steps page",
    "Test Case editor",
    "editing"
  ],
  "index_keyword_paths": [
    "Python Action syntax, warnings",
    "Steps page",
    "Steps page > Test Case editor",
    "Test Case editor > Steps page",
    "step properties > editing",
    "steps > editing"
  ],
  "related_links": [
    "test_case_editor_steps_page.htm#1284516",
    "test_case_editor_steps_page.htm#1284656"
  ],
  "images": [
    "topics/images/test_case_editor_2.01.jpg"
  ],
  "content_hash": "1d3ee7d12a997a2e",
  "level": 1
}
---

# Test Case editor: Steps page > Test Case editor: Steps page

Important If file system APIs are used to create, delete, or update files within a TestCase, then all subsequent steps in that TestCase must continue using file system APIs—even if the file resides in a project imported into the workspace. Workspace-level APIs (i.e., those using the project:// schema) are not applicable in this scenario, as they do not immediately reflect file system changes.

On the Steps page, you review, add, and modify steps.

1. 1

1. Step 10 is selected, so you can perform the following:

- Edit its property settings in the Step Properties section at the bottom (#4 — click the arrow to open the section)

| Note: You may open the context specific information—Step Properties section in the Properties pane as follows. Right-click to display the menu and select “Show Properties View”. OR Click the ellipsis on the step command, where applicable. |
| --- |

- Change the value in the Action, Session, or Description cell in the grid

- Modify it using a toolbar button (described in Test Case editor toolbar) or right-click menu item

1. 2

1. Selected steps (like step 10), comments, and procedures are highlighted. Skipped steps (like step 7) are marked with a hashed background.

1. 3

1. If a step has a non-default property setting (like step 10), is breakpointed, or is invalid in some way, then an icon appears in the first column of the Steps grid to identify the issue. Hold the cursor over the icon to view the details.

The circle indicates that step 11 is breakpointed. The icon for step 10 indicates that the step has a non-default property setting (start the step in a new thread — asynch).

1. 4

1. Down here in the Step Properties section, properties for the step are grouped by function. We clicked General to open the General properties page (to the right).

| Note: You may open the context specific information—Step Properties section in the Properties pane as follows. Right-click to display the menu and select “Show Properties View”. OR Click the ellipsis on the step command, where applicable. |
| --- |

1. 5

1. We're viewing the Steps page of the Test Case editor.

1. 6

1. To specify the operation of a selected step, edit the property settings here.

The Action property (both here and in the Action cell in the steps grid) is populated with actions that are appropriate for the step's session type.

The Command property holds the text of the command.

Required property settings are marked with the * character.

A blue field indicates that setting is being inherited (see the topic on properties inheriting settings).

The indicates that you can use field replacements in the property setting.

1. 7

1. Click Details to define multi-line commands.

![screenshot](topics/images/test_case_editor_2.01.jpg) <!-- image_chunk: img_8efeb1be30102897 -->
