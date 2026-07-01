---
{
  "chunk_id": "stc_rest_session_profile_properties__more_158e8d5bcf5a41a7",
  "source_file": "topics/stc_rest_session_profile_properties.htm",
  "source_original_path": "topics/stc_rest_session_profile_properties.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter REST sessions",
    "Spirent TestCenter REST session profiles",
    "Session profile property settings for Spirent TestCenter REST sessions"
  ],
  "heading_path": [
    "Session profile property settings for Spirent TestCenter REST sessions",
    "Session profile property settings for Spirent TestCenter REST sessions",
    "More"
  ],
  "anchor": "1425586",
  "context_ids": [
    "stc_rest_session_profile_properties"
  ],
  "index_keywords": [
    "Spirent TestCenter GUI sessions",
    "session profile property settings"
  ],
  "index_keyword_paths": [
    "Spirent TestCenter GUI > session profile property settings",
    "session profile property settings > Spirent TestCenter GUI sessions"
  ],
  "related_links": [
    "#1317028",
    "field_replacements_tasks.htm#",
    "param_parameters_type_secret.htm#1569142",
    "preferences.03.htm#1162820",
    "preferences_itest.htm#",
    "#1442408",
    "testcenter_session_editor_concept.htm#",
    "session_profile_properties_testcenter.htm#1321865"
  ],
  "images": [
    "topics/images/stc_REST_AION_Auth.png",
    "topics/images/password_secretType.png"
  ],
  "content_hash": "158e8d5bcf5a41a7",
  "level": 2
}
---

# Session profile property settings for Spirent TestCenter REST sessions > Session profile property settings for Spirent TestCenter REST sessions > More

Click More... complete these relevant information.

- Spirent TestCenter REST: Same information described in Spirent TestCenter REST session properties.

- AION Authentication

| Use AION License | Default: Disabled If disabled (unchecked), Spirent TestCenter will use the chassis-based licensing instead. The AION authentication fields are not available for your input. When enabled, the Spirent TestCenter uses AION licensing for any features used within the test session. |
| --- | --- |
| Server | Mandatory. Enter a valid AION server address. Note Field substitution is supported. See “Field Replacements” |
| Note | Field substitution is supported. See “Field Replacements” |
| Username | Mandatory. AION login ID of the user. Note Field substitution is supported. See “Field Replacements” |
| Note | Field substitution is supported. See “Field Replacements” |
| Password | Mandatory. AION password. Password: When you start typing into the Password field (e.g. SSH password, REST basic authentication password, JKS (Java Keytool Store) password), iTest displays a dialog asking you whether you wish to use a secret parameter for this field (that is, to use a secret parameter from the session profile, parameters file, or test case), and provides you with an opportunity to add a secret in either of these locations. Clicking yes displays the Insert parameter wizard. See Adding a parameter definition while inserting password Click No to type the password into the field, which iTest encrypts. You may select the checkbox Do not show this dialog again to ensure that the prompt to use parameter does not display. See also Preferences: Spirent > Editors, Chapter 39, “Configuring iTest Preferences”. Mask content: The Mask Content field appears below the Password field, which is selected by default for Secret parameter type, and you may uncheck this selection. When you uncheck, iTest displays a Clear field content? dialog with a warning message informing that the masked data will be lost and whether you would to unmask the field and clear the content. The dialog also allows you to set your preference to not display this dialog again. You may select the checkbox Do not ask again to make sure that the Clear filed content? dialog does not display again. Click Yes to save your selection and acknowledge unmasking and clearing the content and No to discard the clear field content operation. See also Preferences: Spirent > Editors, Chapter 39, “Configuring iTest Preferences”. |
|  | You may select the checkbox Do not ask again to make sure that the Clear filed content? dialog does not display again. |
|  | Click Yes to save your selection and acknowledge unmasking and clearing the content and No to discard the clear field content operation. |
| Sign out on disconnect | Default: disabled. When enabled you are logged out from using AION authentication when you close an iTest STC REST session. Note You cannot sign in or sign out of AION licensing server when ports are reserved. See AION Authentication and iTest executions. |
| Note | You cannot sign in or sign out of AION licensing server when ports are reserved. See AION Authentication and iTest executions. |

- To complete relevant information, see also the sections listed in “Spirent TestCenter sessions”.

Port Steps, Generator Steps, Custom 16-bit Filter Steps, Stream Block Steps

![screenshot](topics/images/stc_REST_AION_Auth.png) <!-- image_chunk: img_647a1a7066129cb8 -->

![screenshot](topics/images/password_secretType.png) <!-- image_chunk: img_414b59070b2ea79a -->
