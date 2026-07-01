---
{
  "chunk_id": "session_profile_popmail__defining_a_mail_pop3_session_9f6e5310e0f8a7cb",
  "source_file": "topics/session_profile_popmail.htm",
  "source_original_path": "topics/session_profile_popmail.htm",
  "toc_path": [
    "iTest Online Help",
    "Mail (POP3) Sessions",
    "Defining a Mail (POP3) session"
  ],
  "heading_path": [
    "Defining a Mail (POP3) session",
    "Defining a Mail (POP3) session"
  ],
  "anchor": "1156629",
  "context_ids": [
    "session_profile_popmail"
  ],
  "index_keywords": [
    "defining (POP3)",
    "receiving (POP3 messages) from test case"
  ],
  "index_keyword_paths": [
    "email messages > defining (POP3)",
    "email messages > receiving (POP3 messages) from test case"
  ],
  "related_links": [],
  "images": [
    "topics/images/session_editor_pop3_mail.png",
    "topics/images/popmail_2.2.jpg",
    "topics/images/pop3_console_commands_captured.png",
    "topics/images/pop3_mail_procedure_labeled.png",
    "topics/images/pop3_mail_procedure_response_structure.png"
  ],
  "content_hash": "9f6e5310e0f8a7cb",
  "level": 1
}
---

# Defining a Mail (POP3) session > Defining a Mail (POP3) session

Mail (POP3) sessions differ from typical sessions with devices. The reason for creating a Mail (POP3) session is to enable your test cases to receive email that can include test case response data and pass/fail results. When you start a Mail (POP3) “session”, you are specifying a POP3 email server and email address from where you can retrieve emails, copy email attachments to your work space. You can then add Mail GetStatus, RetrieveMessages, and GetAttachments steps. GetStatus retrieves the mail-box status and the number of emails in the mail-box. A RetrieveMessages step retrieves an email from the POP3 server. This topic provides instructions on configuring the session profile file that you use to start a session.

Here's an example Mail (POP3) Session window. Click Start and the PopMail Console opens.

> **Note:** Note

- Mail (POP3) port 110 is commonly used to connect without SSL and TLS options (default settings)

- Mail (POP3) port 995 is commonly used to connect with SSL option

- Mail (POP3) port 110 is commonly used to connect with TLS option

Perform the required task using the commands as required, as shown below. See also Mail (POP3) Session Commands for details.

iTest captures the tasks you performed (commands you used) as a group of Mail (POP3) session steps. You can now save the steps into a test case.

| ; |
| --- |

Here's is the Mail procedure that results:

Here are the Mail (POP3) session steps. Each part of the message is a separate Mail action command.

To add response data collected during execution to the message, add GetStatus, Fetch, RetrieveMessage, GetAttachments message command actions.

As with any test case step, you can modify the properties as needed.

For example, you would add field replacements here to include response data in the message body.

Click Details and add multi-line contents.

Based on the step response, you can add the analysis rule for any step in iTest. For example, after capturing mail session commands and running the test case, you may add analysis rule for any command, for example, RetrieveMessage.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/session_editor_pop3_mail.png) <!-- image_chunk: img_13dd3cd54f920437 -->

![screenshot](topics/images/popmail_2.2.jpg) <!-- image_chunk: img_b53446b1d7de6cc3 -->

![screenshot](topics/images/pop3_console_commands_captured.png) <!-- image_chunk: img_5c1f4a5d29ed86c5 -->

![screenshot](topics/images/pop3_mail_procedure_labeled.png) <!-- image_chunk: img_983c86f7b70e1a9d -->

![screenshot](topics/images/pop3_mail_procedure_response_structure.png) <!-- image_chunk: img_86b5878049475b3a -->
