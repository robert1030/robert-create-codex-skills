---
{
  "chunk_id": "sp_properties_chat__chat_session_profile_properties_4ca3e9df74b9508c",
  "source_file": "topics/sp_properties_chat.htm",
  "source_original_path": "topics/sp_properties_chat.htm",
  "toc_path": [
    "iTest Online Help",
    "Chat Sessions (XMPP chat)",
    "Session profile property settings for Chat (XMPP) sessions"
  ],
  "heading_path": [
    "Session profile property settings for Chat (XMPP) sessions",
    "Session profile property settings for Chat (XMPP) sessions",
    "Chat session profile properties"
  ],
  "anchor": "1396121",
  "context_ids": [
    "sp_properties_chat"
  ],
  "index_keywords": [
    "Chat session properties",
    "Chat sessions",
    "property settings"
  ],
  "index_keyword_paths": [
    "Chat session properties",
    "Chat sessions",
    "Chat sessions > property settings",
    "configuring > Chat sessions",
    "property settings > Chat sessions"
  ],
  "related_links": [
    "param_parameters_type_secret.htm#1569142",
    "preferences.03.htm#1162820",
    "preferences_itest.htm#"
  ],
  "images": [
    "topics/images/password_secretType.png"
  ],
  "content_hash": "4ca3e9df74b9508c",
  "level": 2
}
---

# Session profile property settings for Chat (XMPP) sessions > Session profile property settings for Chat (XMPP) sessions > Chat session profile properties

| To | Specify the address to connect to. |
| --- | --- |
| Use default XMPP connection | Check the box to specify that Velocity should act as the XMPP server. Default: checked |
| XMPP Server | Specify the XMPP server address: either the DNS name or IP address. |
| Port | Specify the port that the XMPP server should listen on. Default: 5222 |
| Login name / Password | Specify the username and password of the Chat account that will send your messages. Password: When you start typing into the Password field (e.g. SSH password, REST basic authentication password, JKS (Java Keytool Store) password), iTest displays a dialog asking you whether you wish to use a secret parameter for this field (that is, to use a secret parameter from the session profile, parameters file, or test case), and provides you with an opportunity to add a secret in either of these locations. Clicking yes displays the Insert parameter wizard. See Adding a parameter definition while inserting password Click No to type the password into the field, which iTest encrypts. You may select the checkbox Do not show this dialog again to ensure that the prompt to use parameter does not display. See also Preferences: Spirent > Editors, Chapter 39, “Configuring iTest Preferences”. Mask content: The Mask Content field appears below the Password field, which is selected by default for Secret parameter type, and you may uncheck this selection. When you uncheck, iTest displays a Clear field content? dialog with a warning message informing that the masked data will be lost and whether you would to unmask the field and clear the content. The dialog also allows you to set your preference to not display this dialog again. You may select the checkbox Do not ask again to make sure that the Clear filed content? dialog does not display again. Click Yes to save your selection and acknowledge unmasking and clearing the content and No to discard the clear field content operation. See also Preferences: Spirent > Editors, Chapter 39, “Configuring iTest Preferences”. |
|  | You may select the checkbox Do not ask again to make sure that the Clear filed content? dialog does not display again. |
|  | Click Yes to save your selection and acknowledge unmasking and clearing the content and No to discard the clear field content operation. |
| Resource | Specify the identifier for the Chat sender for the message. This enables you, for example, to specify a value of Home for messages that you send from your home computer and specify a Resource of Work so that you can send and receive messages using the same chat account in both locations. |

![screenshot](topics/images/password_secretType.png) <!-- image_chunk: img_414b59070b2ea79a -->
