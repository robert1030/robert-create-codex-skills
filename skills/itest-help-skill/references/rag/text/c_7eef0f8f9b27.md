# Test Cases > Test suites: Organizing tests for group execution > Setting and accessing variables in test case steps > Accessing variable values in a step

Steps can access variable values in either of the following ways:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Use an eval action with the get (local) or gget (global) command, for example,

![](images/test_cases_2.5.jpg) <!-- image_ref -->

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Use an eval action with variable syntax:

${varName} ( Tcl local)

(‘varName’) (Python local)

${/data/varName} (Tcl global)

(‘/data/varName’) (Python global)

![](images/test_cases_2.6.jpg) <!-- image_ref -->

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- To return data from a variable that holds the response to an earlier step, see response command: Accessing response data that is stored in a variable.
