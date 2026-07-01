---
{
  "chunk_id": "ui_itest_window_layout__development_perspective_21b7300cfb90d1ce",
  "source_file": "topics/ui_itest_window_layout.htm",
  "source_original_path": "topics/ui_itest_window_layout.htm",
  "toc_path": [
    "iTest Online Help",
    "About the iTest Window",
    "How iTest perspectives are organized"
  ],
  "heading_path": [
    "How iTest perspectives are organized",
    "How iTest perspectives are organized",
    "Development perspective"
  ],
  "anchor": "1579759",
  "context_ids": [
    "ui_itest_window_layout"
  ],
  "index_keywords": [
    "iTest",
    "window organization"
  ],
  "index_keyword_paths": [
    "iTest > window organization",
    "window layout > iTest"
  ],
  "related_links": [
    "json_preferences_pretty_print.htm#1335837",
    "json_editor_overview.htm#",
    "builder.5.htm#1103394"
  ],
  "images": [
    "topics/images/itest_layout_overview_label.png"
  ],
  "content_hash": "21b7300cfb90d1ce",
  "level": 4
}
---

# How iTest perspectives are organized > How iTest perspectives are organized > Development perspective

Perspective controls. This group of buttons controls the current perspective, the collection and arrangement of views and editors. We’re viewing the iTest Development perspective. To switch to the iTest Expert perspective, click the iTest Expert button — a new arrangement of editors and views replaces the current arrangement. The buttons that appear here are names of perspectives that you have used. Click to switch to any other perspective.

You can customize perspectives to suit your needs by moving, resizing, and opening or closing views and editors (don’t forget to save your changes if you like them).

Main menu and toolbar. The menu and toolbar can change based on the current perspective or editor.

Editor. You work on any iTest document in an editor. In the example, we opened the 2000framesThroughSwitch test case document in the Test Case editor. In this editor, each line represents a step in the test. There are editors for topologies, for session profiles that define connection settings with devices, and for other types of iTest documents.

In an editor, you can type directly into text fields, select items from drop-down lists, and right-click to open a context menu of actions. The toolbar at the top of the editor enables you to take action on the currently selected item (in the example, we might add a step after the selected step, apply a breakpoint, skip the selected step, cut/copy/paste, and so on).

Pages that make up the editors. Editors can include several special-purpose pages that you open by clicking the tabs at the bottom. In the example, we clicked the Steps tab to work on the Steps page of the Test Case editor.

View. This is the Response view. Views display information on the document that you are editing and provide other supporting information.

In the example, we selected step 5 (the show interfaces command) on the Steps page of the Test Case editor. The Response view then immediately updated itself to display the command and the response to the command (from the most recent execution of the test case). iTest has used queries to return values of interest from the response (the values that match queries are surrounded by boxes, the value 0 that was verified by an “analysis rule” is highlighted in green).

On the Response tab/section, the default display format is auto-detected as Text, JSON, or YAML form.

- If JSON syntax is detected, iTest displays text formatted as JSON pretty-print.

If JSON format is not detected, the data will be displayed as TEXT and will interpret/present the data accordingly.

- iTest automatically detects YAML syntax and format, if response was mapped as YAML.

Response view shows YAML response text (not formatted as pretty-print).

Click Text/JSON/YAML options from the dropdown list on the Response Window to toggle the response view display as JSON Pretty-Print or Text or YAML.

> **Note:** Note When iTest auto-detects JSON format, or select the JSON option to display the content, the pretty print format is assigned as per your settings (see Setting preferences for JSON Pretty Print in “JSON Editor”).

- In the example, the Response and Images views are stacked. To bring a view to the front, click its tab.

- To display a view that does not currently appear, click Show View and select the view.

- Most views provide toolbars and context (right-click) menus for actions on selected items.

- Press F1 or click for Online help on the current view or editor.

The Project Explorer view enables you to view and manage all documents that you create using iTest. We opened the 2000framesThroughSwitch test case by double-clicking it. Right-click to open a context menu of actions like Rename/Move/Copy/Paste/Delete/View Properties. The Favorites view (directly above the Project Explorer in the example) provides quick access to documents that you work with most often.

Important Typically, one iTest resource (the name for a iTest file) depends upon one or more other iTest resources. For example, a test case might depend on a topology, response maps in a response map library, session profiles, and so on. As a result, when you Rename, Move, or Delete a iTest resource, multiple files will typically be affected. For details on how you can best rename, move, or delete a resource, see Updating project dependencies.

> **Tip:** Tip Double-click a tab to maximize a view or editor. Double-click it again to minimize.

![screenshot](topics/images/itest_layout_overview_label.png) <!-- image_chunk: img_95507565641fd803 -->
