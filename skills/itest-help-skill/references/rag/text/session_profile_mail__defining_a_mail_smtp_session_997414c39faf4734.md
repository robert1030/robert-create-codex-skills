---
{
  "chunk_id": "session_profile_mail__defining_a_mail_smtp_session_997414c39faf4734",
  "source_file": "topics/session_profile_mail.htm",
  "source_original_path": "topics/session_profile_mail.htm",
  "toc_path": [
    "iTest Online Help",
    "Mail (SMTP) Sessions",
    "Defining a Mail (SMTP) session"
  ],
  "heading_path": [
    "Defining a Mail (SMTP) session",
    "Defining a Mail (SMTP) session"
  ],
  "anchor": "1156629",
  "context_ids": [
    "session_profile_mail"
  ],
  "index_keywords": [
    "defining",
    "sending from test case"
  ],
  "index_keyword_paths": [
    "email messages > defining",
    "email messages > sending from test case"
  ],
  "related_links": [],
  "images": [
    "topics/images/session_editor_mail.png",
    "topics/images/message_content_captured.png",
    "topics/images/mail_2.3.jpg"
  ],
  "content_hash": "997414c39faf4734",
  "level": 1
}
---

# Defining a Mail (SMTP) session > Defining a Mail (SMTP) session

Mail sessions differ from typical sessions with devices. The reason for creating a Mail session is to enable your test cases to send email that can include test case response data and pass/fail results. When you start a Mail “session”, you are really preparing an email message that you can copy into a test case as a procedure. You can then add Mail write, writeline, and message steps that add response data to the message. A send step then sends the email. This topic provides instructions on configuring the session profile file that you use to start a session.

1. Here's an example Mail (SMTP) Session window. Prepare the email message as test cases should send it.

You can add plain text here, but once this message is added to a test case as a set of Mail session steps, you can use field replacements to insert test data into the Subject or Message, add a file as an attachment, or even change the mail sender (From) or recipient (To).

> **Note:** Note It is recommended to use hostname (and not IPv6) in From (mail sender) and To (recipient).

1. 2

1. When you click Send, two things happen:

- The SMTP server sends the email

- iTest captures the contents of the message as a group of Mail session steps.

You can now save the steps into a test case.

| ; |
| --- |

Here's is the Mail procedure that results:

Here are the Mail session steps. Each part of the message is a separate Mail action.

To add response data collected during execution to the message, you'll add write, writeline, and message actions.

The send step sends the message.

As with any test case step, you can modify the properties as needed.

For example, you would add field replacements here to include response data in the message body.

Click Details for multi-line contents.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/session_editor_mail.png) <!-- image_chunk: img_96a9b84e71bc7c9c -->

![screenshot](topics/images/message_content_captured.png) <!-- image_chunk: img_8d134f00731bcb70 -->

![screenshot](topics/images/mail_2.3.jpg) <!-- image_chunk: img_d836ad081fbb0a67 -->
