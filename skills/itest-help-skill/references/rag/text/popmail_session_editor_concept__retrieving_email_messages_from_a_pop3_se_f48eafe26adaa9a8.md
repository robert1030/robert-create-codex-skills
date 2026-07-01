---
{
  "chunk_id": "popmail_session_editor_concept__retrieving_email_messages_from_a_pop3_se_f48eafe26adaa9a8",
  "source_file": "topics/popmail_session_editor_concept.htm",
  "source_original_path": "topics/popmail_session_editor_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Mail (POP3) Sessions",
    "Receiving email messages during test execution"
  ],
  "heading_path": [
    "Receiving email messages during test execution",
    "Receiving email messages during test execution",
    "Retrieving email messages from a POP3 Server"
  ],
  "anchor": "1405437",
  "context_ids": [
    "popmail_session_editor_concept"
  ],
  "index_keywords": [
    "Mail action",
    "receiving during test execution",
    "receiving email messages (pop3) during",
    "receiving email messages (pop3)during test execution"
  ],
  "index_keyword_paths": [
    "attach > Mail action",
    "email messages(pop3) > receiving during test execution",
    "execution > receiving email messages (pop3) during",
    "receiving email messages (pop3)during test execution"
  ],
  "related_links": [
    "session_profile_popmail.htm#1156629"
  ],
  "images": [
    "topics/images/popmail.4.jpg",
    "topics/images/pop3_mail_procedure_labeled.png"
  ],
  "content_hash": "f48eafe26adaa9a8",
  "level": 2
}
---

# Receiving email messages during test execution > Receiving email messages during test execution > Retrieving email messages from a POP3 Server

The easiest way to steps to retrieve messages and/or images to a test case is to save a captured Mail (POP3) session as a procedure in the test case. You can then edit the Mail (POP3) session steps as described in the following sections (for example, to retrieve mails messages or attached files). See Defining a Mail (POP3) session.

Here’s an example Mail procedure that results from saving a captured Mail session as a procedure:

Here are the Mail session steps. Each commands is a separate command action.

To add response action performed during execution, you'll add GetStatus, RetrieveMessage, and GetAttachments actions.

As with any test case step, you can modify the properties as needed.

For example, you would add field replacements here to include response data in the message body.

Click Details for multi-line contents.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![inline_icon](topics/images/popmail.4.jpg) <!-- image_chunk: img_89e8b33cd3172caf -->

![screenshot](topics/images/pop3_mail_procedure_labeled.png) <!-- image_chunk: img_983c86f7b70e1a9d -->
