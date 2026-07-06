# HTTP Sessions > Session profile property settings for HTTP sessions > HTTP

![](images/password_secretType.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

You may select the checkbox Do not ask again to make sure that the Clear filed content? dialog does not display again. Click Yes to save your selection and acknowledge unmasking and clearing the content and No to discard the clear field content operation.

- **Base URL**：Optional: Specify a URL to use for all HTTP commands
- **Authentication method**：Auto: Determine automatically whether to use Basic authentication or no authentication. Basic: Use the specified User ID / Password credentials for HTTP basic access authentication. Password: When you start typing into the Password field (e.g. SSH password, REST basic authentication password, JKS (Java Keytool Store) password), iTest displays a dialog asking you whether you wish to use a secret parameter for this field (that is, to use a secret parameter from the session profile, parameters file, or test case), and provides you with an opportunity to add a secret in either of these locations. Clicking yes displays the Insert parameter wizard. See Adding a parameter definition while inserting password Click No to type the password into the field, which iTest encrypts. You may select the checkbox Do not show this dialog again to ensure that the prompt to use parameter does not display. See also Preferences: Spirent > Editors, Chapter 39, “Configuring iTest Preferences”. Mask content: The Mask Content field appears below the Password field, which is selected by default for Secret parameter type, and you may uncheck this selection. When you uncheck, iTest displays a Clear field content? dialog with a warning message informing that the masked data will be lost and whether you would to unmask the field and clear the content. The dialog also allows you to set your preference to not display this dialog again. See also Preferences: Spirent > Editors, Chapter 39, “Configuring iTest Preferences”. None: Do not perform authentication.
- **User ID / Password**：Used when Authentication method is set to Basic or Auto. If the session will access a secure site, then provide the credentials that iTest should submit to gain access.
