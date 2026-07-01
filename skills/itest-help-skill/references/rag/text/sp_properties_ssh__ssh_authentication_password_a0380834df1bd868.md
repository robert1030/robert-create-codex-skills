---
{
  "chunk_id": "sp_properties_ssh__ssh_authentication_password_a0380834df1bd868",
  "source_file": "topics/sp_properties_ssh.htm",
  "source_original_path": "topics/sp_properties_ssh.htm",
  "toc_path": [
    "iTest Online Help",
    "SSH Sessions",
    "Session profile property settings for SSH sessions"
  ],
  "heading_path": [
    "Session profile property settings for SSH sessions",
    "Session profile property settings for SSH sessions",
    "Advanced Authentication",
    "SSH authentication: Password"
  ],
  "anchor": "1255931",
  "context_ids": [
    "sp_properties_ssh"
  ],
  "index_keywords": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "SSH sessions",
    "configuring",
    "session profile property settings for"
  ],
  "index_keyword_paths": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "SSH sessions > configuring",
    "SSH sessions > session profile property settings for",
    "configuring > SSH sessions",
    "session profile property settings > SSH sessions"
  ],
  "related_links": [
    "param_parameters_type_secret.htm#1569142",
    "preferences.03.htm#1162820",
    "preferences_itest.htm#"
  ],
  "images": [
    "topics/images/password_secretType.png"
  ],
  "content_hash": "a0380834df1bd868",
  "level": 3
}
---

# Session profile property settings for SSH sessions > Session profile property settings for SSH sessions > Advanced Authentication > SSH authentication: Password

| Password | Specify the password used to connect to the remote host. Password: When you start typing into the Password field (e.g. SSH password, REST basic authentication password, JKS (Java Keytool Store) password), iTest displays a dialog asking you whether you wish to use a secret parameter for this field (that is, to use a secret parameter from the session profile, parameters file, or test case), and provides you with an opportunity to add a secret in either of these locations. Clicking yes displays the Insert parameter wizard. See Adding a parameter definition while inserting password Click No to type the password into the field, which iTest encrypts. You may select the checkbox Do not show this dialog again to ensure that the prompt to use parameter does not display. See also Preferences: Spirent > Editors, Chapter 39, “Configuring iTest Preferences”. Mask content: The Mask Content field appears below the Password field, which is selected by default for Secret parameter type, and you may uncheck this selection. When you uncheck, iTest displays a Clear field content? dialog with a warning message informing that the masked data will be lost and whether you would to unmask the field and clear the content. The dialog also allows you to set your preference to not display this dialog again. You may select the checkbox Do not ask again to make sure that the Clear filed content? dialog does not display again. Click Yes to save your selection and acknowledge unmasking and clearing the content and No to discard the clear field content operation. See also Preferences: Spirent > Editors, Chapter 39, “Configuring iTest Preferences”. By default, the text is encrypted (masked) here and in all locations where it is used. |  | You may select the checkbox Do not ask again to make sure that the Clear filed content? dialog does not display again. |  | Click Yes to save your selection and acknowledge unmasking and clearing the content and No to discard the clear field content operation. |
| --- | --- | --- | --- | --- | --- |
|  | You may select the checkbox Do not ask again to make sure that the Clear filed content? dialog does not display again. |  |  |  |  |
|  | Click Yes to save your selection and acknowledge unmasking and clearing the content and No to discard the clear field content operation. |  |  |  |  |
| Use credentials file | If you configure the Password authentication type, then you have the option to configure iTest to go to a specified text file to obtain the latest correct credentials. Note The authentication file is not encrypted. Check the box to use the credentials that appear in the file that you specify in the Credentials file property. When the box is checked, the settings of the User and Password properties are ignored. | Note | The authentication file is not encrypted. |  |  |
| Note | The authentication file is not encrypted. |  |  |  |  |
| Credentials file | Specify the path and filename of the text file that holds the credentials to use to log in. <username>[space]<password> Note In the text file, if there is any blank or extra space before the credentials, iTest displays an error after starting the session. See the Use credentials file property. | Note | In the text file, if there is any blank or extra space before the credentials, iTest displays an error after starting the session. |  |  |
| Note | In the text file, if there is any blank or extra space before the credentials, iTest displays an error after starting the session. |  |  |  |  |

![screenshot](topics/images/password_secretType.png) <!-- image_chunk: img_414b59070b2ea79a -->
