# Parameters > Defining and managing parameters > About the Parameter Type ‘Secret’ > 第5段

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Analysis Rules (limitation in 8.3)

When a test case uses secret values:

![*](bullet_blue.jpg) <!-- image_ref -->

- Adding analysis rules allows you to displays a message saying that the value contains a secret value instead of showing the Analysis Rule Wizard: Rule page (See Analysis Rule Wizard: Rule page).

![*](bullet_blue.jpg) <!-- image_ref -->

- Adding a Query/XPath will also not be possible on the Analysis Rule Wizard: Extractor page (See Analysis Rule Wizard: Extract page).

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Executing QuickCalls with secret type parameter

When Python SLC connected to iTest GUI and try access QuickCalls with secret values will trigger iTest GUI to show dialog to enter this secret values.

Executing QuickCalls that required secret value when iTest GUI is configured in listening mode (see Configure Listening Mode (Listen for incoming Python connections)), a dialog displays for entering the secret value. However, no output will be sent to the SLC library as response for any QuickCalls use secret value. See Executing QuickCalls with secret type parameter.
