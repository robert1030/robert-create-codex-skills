---
{
  "chunk_id": "write_mail__intro_5c745c4ddb1339ca",
  "source_file": "topics/popups/write_mail.html",
  "source_original_path": "topics/popups/write_mail.html",
  "toc_path": null,
  "heading_path": [
    "write_mail.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/mail_steps_adding.html",
    "help::/com.fnfr.svt.help/topics/field_replacement_response.html"
  ],
  "images": [],
  "content_hash": "5c745c4ddb1339ca",
  "level": 0
}
---

# write_mail.html

Appends the content that appears in the Description cell (the value of the Command property) to the body of the message. Because this action does not move to a new line, subsequent write or writeLine actions are added directly to the end of the text.

Type the message into the Description cell. To supply multiple lines of text, click the Advanced button for the Command property and type the text into the Command text box.

You can use as many write and writeLine actions as needed while building a message.

Field replacements are supported. For example, use a response command in a field replacement to append the response for a step to the email message contents.

For details, see the online help: Sending email messages during test execution.

Also: Using the response command in a field replacement.
