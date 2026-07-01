---
{
  "chunk_id": "action_message__the_message_action_add_a_severity_type_a_a966300c29eaca1f",
  "source_file": "topics/action_message.htm",
  "source_original_path": "topics/action_message.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Actions for CLI session types",
    "The ‘message’ action: Add a severity type and message type"
  ],
  "heading_path": [
    "The ‘message’ action: Add a severity type and message type",
    "The ‘message’ action: Add a severity type and message type"
  ],
  "anchor": "1696651",
  "context_ids": [
    "action_message"
  ],
  "index_keywords": [
    "adding to test cases",
    "message",
    "message action"
  ],
  "index_keyword_paths": [
    "actions > message",
    "message action",
    "messages > adding to test cases"
  ],
  "related_links": [
    "#1696840"
  ],
  "images": [
    "topics/images/exec_message.png"
  ],
  "content_hash": "a966300c29eaca1f",
  "level": 1
}
---

# The ‘message’ action: Add a severity type and message type > The ‘message’ action: Add a severity type and message type

For the message action, iTest interprets the text in the associated Description field as a message with severity type to the user. At runtime, all messages in the test case appear as execution issue messages in the Execution view and test report.

The message actions supports severity levels: OK, Error, Information, and Warning. You may either enter the severity type and message manually or select from Step Properties > EXEC message Properties > Message Step Properties page (see the screenshot “Action ‘message’” below).

- Severity: Drop-down list options: OK, Error, Information (default), and Warning

- Message: Enter the message to be displayed in the Execution view and test report.

> **Note:** Note The Message field on Step Properties > EXEC message Properties > Message Step Properties page supports field substitution.

The severity option and the message specified on the Step Properties > EXEC message Properties > Message Step Properties page are synchronized with the description contents and vice versa.

| Action ‘message’ |
| --- |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/exec_message.png) <!-- image_chunk: img_47876673b31fe2e3 -->
