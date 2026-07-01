---
{
  "chunk_id": "mail_steps_adding__sending_an_email_message_manually_by_def_51967da0c98413d9",
  "source_file": "topics/mail_steps_adding.htm",
  "source_original_path": "topics/mail_steps_adding.htm",
  "toc_path": [
    "iTest Online Help",
    "Mail (SMTP) Sessions",
    "Adding Mail (SMTP) steps manually"
  ],
  "heading_path": [
    "Adding Mail (SMTP) steps manually",
    "Adding Mail (SMTP) steps manually",
    "Sending an email message manually by defining a new session profile and then starting it"
  ],
  "anchor": "1272193",
  "context_ids": [
    "mail_steps_adding"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "session_profile_concept.htm#1304370"
  ],
  "images": [
    "topics/images/mail_2.1.jpg"
  ],
  "content_hash": "51967da0c98413d9",
  "level": 2
}
---

# Adding Mail (SMTP) steps manually > Adding Mail (SMTP) steps manually > Sending an email message manually by defining a new session profile and then starting it

1. When you click Start on the New Session tab (Start page) of the session profile editor, an email message form opens. Fill in as many fields as needed. To actually send the message, you'll need to specify at least the To and From settings. For basic instructions on configuring a session, see Session profiles: Session configuration settings.

1. 2

1. Click Send to send the message. iTest now captures all Mail session settings as steps.

Typically, you'll save the Mail session as a procedure, as shown earlier in the example. When you add the procedure to a test case, you can edit the properties of the message. For example, you can use the Write action to place test results into the message body. You might also alter the to setting to send failure results to one email alias and pass results to another alias.

![screenshot](topics/images/mail_2.1.jpg) <!-- image_chunk: img_a84b7889b29df50c -->
