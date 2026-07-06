# Test Case Editor > Steps page on the Test Case Editor > Test Case editor: Steps page > Validation of steps and property settings

By default, iTest auto-validates property values as you set them. Validation determines whether there is a problem with a step and whether any property settings are invalid or non-default.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- In the Test Case editor, the validation process marks a step with an icon in the first column:

![](images/test_case_editor_2.09.jpg) <!-- image_ref -->

For Python test cases, step Action with syntax errors display a warning when creating tests. This is to help you address the errors right away instead of finding them at runtime.

![](images/tce_python_step_warning_message.png) <!-- image_ref -->

![*](bullet_blue.jpg) <!-- image_ref -->

- Warning icon appears in TestCase Editor for steps with invalid syntax.

![*](bullet_blue.jpg) <!-- image_ref -->

- Hover over the warning icon to display a warning message.

![*](bullet_blue.jpg) <!-- image_ref -->

- The warning message also appears in the Problems view.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

![](images/test_case_editor_2.11.jpg) <!-- image_ref -->

- In the Session Profile editor, the validation process marks a problematic property value with an error marker and identifies a non-default property setting by changing the property value field from blue (default) to white (non-default).

You have the option to configure iTest to not perform validation — steps are not auto-validated and no markers appear for invalid or non-default property settings.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

![](images/test_case_editor_2.12.jpg) <!-- image_ref -->

- If auto-validation is disabled, you can perform validation on‑demand in the Test Case editor — click Validate

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- You cannot perform on‑demand validation in the Session Profile editor.

You control the option using the Perform step validation only when requested property on the Spirent > Editors > Test Case Editor preferences page. See Properties in: Spirent > Editors > Test Case Editor.
