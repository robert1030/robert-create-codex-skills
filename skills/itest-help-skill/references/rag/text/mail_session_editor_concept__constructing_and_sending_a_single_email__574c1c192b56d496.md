---
{
  "chunk_id": "mail_session_editor_concept__constructing_and_sending_a_single_email__574c1c192b56d496",
  "source_file": "topics/mail_session_editor_concept.htm",
  "source_original_path": "topics/mail_session_editor_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Mail (SMTP) Sessions",
    "Sending email messages during test execution"
  ],
  "heading_path": [
    "Sending email messages during test execution",
    "Sending email messages during test execution",
    "Constructing and sending a single email message"
  ],
  "anchor": "1271477",
  "context_ids": [
    "mail_session_editor_concept"
  ],
  "index_keywords": [
    "Mail action",
    "sending during test execution",
    "sending email messages during",
    "sending email messages during test execution"
  ],
  "index_keyword_paths": [
    "attach > Mail action",
    "bcc > Mail action",
    "cc > Mail action",
    "email messages > sending during test execution",
    "execution > sending email messages during",
    "from > Mail action",
    "message > Mail action",
    "open > Mail action",
    "reset > Mail action",
    "send > Mail action",
    "sending email messages during test execution",
    "subject > Mail action",
    "to > Mail action",
    "write > Mail action",
    "writeline > Mail action"
  ],
  "related_links": [
    "session_profile_mail.htm#1156629"
  ],
  "images": [
    "topics/images/mail_procedure_label.png"
  ],
  "content_hash": "574c1c192b56d496",
  "level": 2
}
---

# Sending email messages during test execution > Sending email messages during test execution > Constructing and sending a single email message

The easiest way to add an email to a test case is to save a captured Mail session as a procedure in the test case. You can then edit the Mail session steps as described in the following sections (for example, to insert test data or attach files). See Defining a Mail (SMTP) session.

Here’s an example Mail procedure that results from saving a captured Mail session as a procedure:

Here are the Mail session steps. Each part of the message is a separate Mail action.

To add response data collected during execution to the message, you'll add write, writeline, and message actions.

The send step sends the message.

As with any test case step, you can modify the properties as needed.

For example, you would add field replacements here to include response data in the message body.

1. 1

1. Click Advanced for multi-line contents.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/mail_procedure_label.png) <!-- image_chunk: img_16a72923df7e3768 -->
