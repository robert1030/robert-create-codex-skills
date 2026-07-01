---
{
  "chunk_id": "session_profile_properties_mail__mail_session_profile_properties_2a230e661cfc6980",
  "source_file": "topics/session_profile_properties_mail.htm",
  "source_original_path": "topics/session_profile_properties_mail.htm",
  "toc_path": [
    "iTest Online Help",
    "Mail (SMTP) Sessions",
    "Session profile property settings for Mail (SMTP) sessions"
  ],
  "heading_path": [
    "Session profile property settings for Mail (SMTP) sessions",
    "Session profile property settings for Mail (SMTP) sessions",
    "Mail session profile properties"
  ],
  "anchor": "1278611",
  "context_ids": [
    "session_profile_properties_mail"
  ],
  "index_keywords": [
    "Mail session properties",
    "Mail sessions"
  ],
  "index_keyword_paths": [
    "Mail session properties",
    "property settings > Mail sessions"
  ],
  "related_links": [
    "param_parameters_type_secret.htm#1569142",
    "preferences.03.htm#1162820",
    "preferences_itest.htm#"
  ],
  "images": [
    "topics/images/password_secretType.png"
  ],
  "content_hash": "2a230e661cfc6980",
  "level": 2
}
---

# Session profile property settings for Mail (SMTP) sessions > Session profile property settings for Mail (SMTP) sessions > Mail session profile properties

| SMTP Server | Check with your system administrator for your SMTP server address. iPv4: Enter either the Host name or IP address. iPV6: To use IPv6 with a session, use the following syntax: Without substitution: [<IPv6>] With substitution: ['\[']::<IPv6>['\]'] Python: eval IPv6="http://[::1]:8080/dashboard/" TCL: eval set IPv6 "http://\[::1\]:8080/dashboard/" |  | Without substitution: [<IPv6>] |  | With substitution: ['\[']::<IPv6>['\]'] |
| --- | --- | --- | --- | --- | --- |
|  | Without substitution: [<IPv6>] |  |  |  |  |
|  | With substitution: ['\[']::<IPv6>['\]'] |  |  |  |  |
| SMTP port | Check with your system administrator for the port for the SMTP Server. The standard SMTP port and default setting is 25. |  |  |  |  |
| User name / Password | Specify the username and password of the email account that will send the messages. Password: When you start typing into the Password field (e.g. SSH password, REST basic authentication password, JKS (Java Keytool Store) password), iTest displays a dialog asking you whether you wish to use a secret parameter for this field (that is, to use a secret parameter from the session profile, parameters file, or test case), and provides you with an opportunity to add a secret in either of these locations. Clicking yes displays the Insert parameter wizard. See Adding a parameter definition while inserting password Click No to type the password into the field, which iTest encrypts. You may select the checkbox Do not show this dialog again to ensure that the prompt to use parameter does not display. See also Preferences: Spirent > Editors, Chapter 39, “Configuring iTest Preferences”. Mask content: The Mask Content field appears below the Password field, which is selected by default for Secret parameter type, and you may uncheck this selection. When you uncheck, iTest displays a Clear field content? dialog with a warning message informing that the masked data will be lost and whether you would to unmask the field and clear the content. The dialog also allows you to set your preference to not display this dialog again. You may select the checkbox Do not ask again to make sure that the Clear filed content? dialog does not display again. Click Yes to save your selection and acknowledge unmasking and clearing the content and No to discard the clear field content operation. See also Preferences: Spirent > Editors, Chapter 39, “Configuring iTest Preferences”. |  | You may select the checkbox Do not ask again to make sure that the Clear filed content? dialog does not display again. |  | Click Yes to save your selection and acknowledge unmasking and clearing the content and No to discard the clear field content operation. |
|  | You may select the checkbox Do not ask again to make sure that the Clear filed content? dialog does not display again. |  |  |  |  |
|  | Click Yes to save your selection and acknowledge unmasking and clearing the content and No to discard the clear field content operation. |  |  |  |  |
| Default ‘From.' email address | Specify the email address that should appear as the email sender for the message. |  |  |  |  |
| Use SSL to connect to mail server | Check with your system administrator to see if SSL is required when connecting with the server. Check the box to use SSL. |  |  |  |  |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/password_secretType.png) <!-- image_chunk: img_414b59070b2ea79a -->
