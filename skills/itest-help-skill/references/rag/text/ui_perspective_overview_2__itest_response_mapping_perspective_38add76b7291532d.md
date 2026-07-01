---
{
  "chunk_id": "ui_perspective_overview_2__itest_response_mapping_perspective_38add76b7291532d",
  "source_file": "topics/ui_perspective_overview_2.htm",
  "source_original_path": "topics/ui_perspective_overview_2.htm",
  "toc_path": [
    "iTest Online Help",
    "About the iTest Window",
    "Overviews of the default iTest perspectives"
  ],
  "heading_path": [
    "Overviews of the default iTest perspectives",
    "Overviews of the default iTest perspectives",
    "iTest Response Mapping perspective"
  ],
  "anchor": "1449924",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "38add76b7291532d",
  "level": 2
}
---

# Overviews of the default iTest perspectives > Overviews of the default iTest perspectives > iTest Response Mapping perspective

You'll use the iTest Response Mapping perspective while creating and editing response maps using the Response Map editor and its associated views.

The Project Explorer displays all projects, libraries, folders, and files in your workspace.

The Response view displays the command and response for the currently selected captured item or test case step. (You can select captured items in the Capture view or Capture Report editor. You can select test case steps in the Test Report editor.) The view makes it easy to review responses and to copy part or all of a response for pasting into other documents.

Step Issues view: While you work on a response map, the Step Issues view shows Errors, Warnings, and info messages associated with queries on the response in the Response view. The Step Issues view lists and describes unexpected items in the current sample, enabling you to “test drive” responses to determine whether named tokens (queries) work as you expect.

Problems view: iTest performs validation on your changes to documents. When you take action that has the potential to cause problems (for example, during execution), iTest opens the Problems view and posts a message into the view.

The Error Log view displays exceptions. The view comes to the front when an exception occurs. When working with Spirent Customer support, you can export and then email the contents of the log to help to resolve the issue.

Queries view: When iTest searches a response for a value that a test case step has requested, it uses an XPath query to search for the specified value in an XML-format structured data representation of the response text. XPath is the foundation on which response mapping is built.

The Queries view lists the XPath queries and their results for the response that is displayed in the Response view. (Queries can be defined in a response map or in local analysis rules. In addition, iTest auto-generates queries for structured responses like Web, SNMP, traffic generator devices, and XML.)

Structure view displays a structured XML representation of every response. Use the Structure view to view the structured part of the response.
