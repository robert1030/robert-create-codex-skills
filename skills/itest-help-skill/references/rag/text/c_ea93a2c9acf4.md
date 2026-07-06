# Session Profiles > Using the ‘Update Session Profile’ wizard > 第2段

- This is mandatory, if empty, a warning message displays saying that the name must be specified.

![*](bullet_blue.jpg) <!-- image_ref -->

- By default, the name will be auto-generated as follows: prompt + number.

![*](bullet_blue.jpg) <!-- image_ref -->

- Prompt names are unique. When you enter the prompt name, if the checkbox is checked, iTest validates to ensure the name is unique. If this name is not unique, a warning message displays: Duplicate name exists.

The Next and Finish buttons will be disabled until a unique name is entered.

![*](bullet_blue.jpg) <!-- image_ref -->

- The More next command field allows you to input text for more next command prompts This field value is optional.

![*](bullet_blue.jpg) <!-- image_ref -->

- If the filed value is empty, this prompt is not a more prompt

![*](bullet_blue.jpg) <!-- image_ref -->

- If the field value NOT empty, this prompt will be treated as a more... prompt and the text will be considered as more next command.

Later, when you have finished running the wizard, you can edit these and other properties to customize the prompt definition. For instructions, see Editing prompt definitions.

1. 2 Optional: The When using this session profile or topology device, do not automatically learn new prompts option tells iTest that, for future test runs, do not start the wizard to present any prospective prompts. Instead, treat all text as a response and use the Completion settings to determine when the step is finished executing.

![*](bullet_blue.jpg) <!-- image_ref -->

Identify new command completion characters

When you perform manual testing, you frequently use characters like tab to auto-complete partially typed commands. To enable iTest to capture the completed form of commands and discard the incomplete form, it must know all command completion characters that you might use while executing test cases.

The wizard’s Command Completion Characters page is populated when iTest has noticed command completion characters that have not yet been configured.

![*](bullet_blue.jpg) <!-- image_ref -->

Identify new command break characters

Most devices interpret certain characters to mean “break execution”. For example, Ctrl-C is a commonly used break character.

The wizard’s Command Break Characters page is populated when iTest has noticed break characters that have not yet been configured.

![*](bullet_blue.jpg) <!-- image_ref -->

Finish
