---
{
  "chunk_id": "mail_steps_adding__adding_mail_smtp_steps_manually_362ce1a356e09af2",
  "source_file": "topics/mail_steps_adding.htm",
  "source_original_path": "topics/mail_steps_adding.htm",
  "toc_path": [
    "iTest Online Help",
    "Mail (SMTP) Sessions",
    "Adding Mail (SMTP) steps manually"
  ],
  "heading_path": [
    "Adding Mail (SMTP) steps manually",
    "Adding Mail (SMTP) steps manually"
  ],
  "anchor": "1271493",
  "context_ids": [
    "mail_steps_adding"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "field_replacements_tasks.htm#",
    "#1400959"
  ],
  "images": [],
  "content_hash": "362ce1a356e09af2",
  "level": 1
}
---

# Adding Mail (SMTP) steps manually > Adding Mail (SMTP) steps manually

1. 1

1. Add a step and select the open action. In the Description cell, select application:com.fnfr.svt.applications.mail. Session IDs for Mail steps do not interact with Session IDs of other sessions in the test case.

> **Tip:** Tip Add new steps by pressing Ctrl+Enter. iTest adds Mail steps in the following order: from, to, subject, writeLine, send.

1. 2

1. In the Action cell, select a Mail action and, if needed, add information to the Description cell. You must supply values for the to and from email addresses. Where indicated, Field replacements are supported. See “Field Replacements”.

| Mail action | Description If applicable, text required in the Description cell |
| --- | --- |
| attach | Attach the file (from the local file system) that is specified in the Description cell. |
| bcc | “Blind copy” the message (the recipient specified in the to step does not see these addresses in the message) to the address specified in the Description cell. In the Description cell, specify an email alias or a semicolon-separated list of email addresses. Field replacements are supported. |
| cc | Copy the message to the address specified in the Description cell. In the Description cell, specify an email alias or a semicolon-separated list of email addresses of the recipients of the email message. Field replacements are supported. |
| from | Specifies the sender of the email message. Required for each mail session in a test case. In the Description cell, specify the email address of the sender. Field replacements are supported. |
| message | Adds content to the body of the email message. Type the message into the Description cell. To supply multiple lines of text, click Advanced for the Command property and type the text into the Command text box. Field replacements are supported. |
| open | Opens a new mail message for building and sending. Added automatically when you save a mail session as a procedure. (See the send action.) In the Description cell, select application://com.fnfr.svt.applications.mail. |
| reset | Clear the following fields in the email message that is currently being built: attach bcc cc from subject to |
| send | Added automatically when you save a mail session as a procedure. Sends the current email message. (See the open action.) |
| subject | Specify the text that should appear in the Subject line of the mail message. Type the text into the Description cell. Field replacements are supported. |
| to | Specifies the recipients of the email message. Required for each mail session in a test case. In the Description cell, specify an email alias or a semicolon-separated list of email addresses of the recipients of the email message. Field replacements are supported. |
| write | Appends the content that appears in the Description cell (the value of the Command property) to the body of the message and does not move to the next line in the message body. Because this action does not move to a new line, subsequent write or writeline actions are added directly to the end of the text. Type the message into the Description cell. You can use as many write and writeline actions as needed while building a message. Field replacements are supported. For example, use a response command in a field replacement to append the response for a step to the email message contents. To create multi-line text On the General properties page, click Details. Type the text into the Command text box. |
| writeline | Appends the content that appears in the Description cell (the value of the Command property) to the body of the message and then moves to the next line in the message body. Type the message into the Description cell. You can use as many write and writeline actions as needed while building a message. Field replacements are supported. For example, use a response command in a field replacement to append the response for a step to the email message contents. To create multi-line text On the General properties page, click Details. Type the text into the Command text box. |
| ContentType | Indicates the type of data to be included in the body of the mail. Mail session supports two types of data: text/plain, text/HTML Select text/HTML, the recipient of the message sees HTML message body. Select text/plain, the recipient of the message sees plain text message body. |
| insertImage | Adds image as specified in the description cell, to the message body. The images will be included as embedded/inline images within the message (text/HTML) content. Use the insertImage command to add image from your local system or your iTest project in test-case editor. From the message body dialog (see Send Email - Message body dialog): Right-click on the message body dialog, select the Insert Image menu option, and then select the required image. From the test-case editor: select the insertImage command dialog of write/writeLine steps. . |
|  | From the message body dialog (see Send Email - Message body dialog): Right-click on the message body dialog, select the Insert Image menu option, and then select the required image. |
|  | From the test-case editor: select the insertImage command dialog of write/writeLine steps. . |

1. 3

1. Add other steps to configure other aspects of the message, like the subject and message contents. The steps can occur in any order and can be interspersed with other test case steps. You can use any number of attach, write, and writeline steps.

1. 4

1. Add a send step at the appropriate location to send the current email message as configured up to that point.
