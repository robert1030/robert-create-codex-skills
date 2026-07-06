# Parameters > Using Parameters in Properties or Steps > Inserting a parameter into a property or test case step

This topic describes the use of the Insert Parameter dialog box to insert a param or profile command into a test case step or property (that is, any field that supports field replacements).

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- You can insert a param command or a profile command into the field.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- You can create a new parameter in the test case and then insert a param command that uses the new parameter (but you cannot set advanced properties for the new parameter).

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- You cannot edit existing parameters using the Insert Parameter dialog box. Instead, use the Parameters page to set the value and advanced properties of a parameter. Parameters can be defined in the current test case, or in a different test case that loaded as a result of a foreign procedure, or in the session profile associated with the step. For instructions on defining parameters, see Working with parameters: The Parameters page.

> **Important：** Important If the session defined in the Open step uses secret parameters, the test case Open step output will be masked (as it is not possible to determine the content of Open step welcome message).
