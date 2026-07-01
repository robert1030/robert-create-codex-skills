---
{
  "chunk_id": "mail_session_editor_concept__sending_email_messages_during_test_execu_a0b46b2c037f1895",
  "source_file": "topics/mail_session_editor_concept.htm",
  "source_original_path": "topics/mail_session_editor_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Mail (SMTP) Sessions",
    "Sending email messages during test execution"
  ],
  "heading_path": [
    "Sending email messages during test execution",
    "Sending email messages during test execution"
  ],
  "anchor": "1400717",
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
  "related_links": [],
  "images": [],
  "content_hash": "a0b46b2c037f1895",
  "level": 1
}
---

# Sending email messages during test execution > Sending email messages during test execution

You can add steps that construct and send email messages as plain text or HTML text with embedded images during execution. A test case can construct and send as many email messages as are needed. The message body can contain both fixed text and test response and result data (detailed instructions follow).

- You can append content to the body of the message over the course of as many steps as needed.

- You can use field replacements to place response content and parameter values into the subject or message.

- When building multiple separate email messages, use the Session ID value to associate Mail steps with each other as needed. Session IDs for Mail steps are not associated with device Session IDs.

- Mail steps do not generate responses.

- Mail steps that generate errors cause test case failure.
