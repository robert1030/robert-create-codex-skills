# Parameters > Defining and managing parameters > About the Parameter Type ‘Secret’ > 第1段

The parameter type Secret (in addition to Text, Boolean, Integer, Double, and Custom), when selected, does not allow you to define value in the Parameters tab (or file) and automatically displays value as masked during usage. The following lists the behavior of the parameter type Secret during definition in test case, execution, response view, and reports.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Define parameters in the parameter file as described in Defining a parameter.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Insert parameter in test case steps as described in Inserting a parameter into a property or test case step.

If the step command contains a Secret parameter type, its response will not be a secret. The response of that command will be shown as clear text in both the Response View and in the generated reports.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Define rules for storing the parameter value as a secret (Analysis Rules > Store processor allows you to store a parameter value as a secret). See Analysis rules: Properties of the processor.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Entering Secret type in Session Profile

![](images/password_secretType.png) <!-- image_ref -->

Password: When you start typing into the Password field (e.g. SSH password, REST basic authentication password, JKS (Java Keytool Store) password), iTest displays a dialog asking you whether you wish to use a secret parameter for this field (that is, to use a secret parameter from the session profile, parameters file, or test case), and provides you with an opportunity to add a secret in either of these locations.

Clicking yes displays the Insert parameter wizard. See Adding a parameter definition while inserting password

Click No to type the password into the field, which iTest encrypts.

You may select the checkbox Do not show this dialog again to ensure that the prompt to use parameter does not display. See also Preferences: Spirent > Editors, Chapter 39, “Configuring iTest Preferences”.

Mask content: The Mask Content field appears below the Password field, which is selected by default for Secret parameter type, and you may uncheck this selection.
