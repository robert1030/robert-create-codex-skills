# Test Cases > Library Template > Validation of testcase against the associated template

iTest validates as follows to ensure that the test cases linked to the templates use the same set of procedures name, argument names (in their defined order), response type and sample data as those defined in the template.

> **Note：** Note You may define additional procedure name and relevant arguments and response type in the new test cases linked to an existing template.

![*](bullet_blue.jpg) <!-- image_ref -->

1. Procedure names: The new test case linked to the template cannot modify the name of the procedures inherited from the template. For example, changing procedure name, indicates an error on the General tab. Go to the General tab and notice an error displayed saying the Procedure defined in the library template is missing in the testcase (as shown below).

![](images/tc_templ_change_proc_name_in_newTC.png) <!-- image_ref -->

Procedure properties Headline, Author, Description, etc., are not validated against the template.

1. 2 Arguments names and order: The new testcase based on the template cannot have different argument names and order.

![*](bullet_blue.jpg) <!-- image_ref -->

1. The set of arguments defined for the procedures must be the same as in the template.

![*](bullet_blue.jpg) <!-- image_ref -->

1. The order of arguments defined must be the same as in the template.

![*](bullet_blue.jpg) <!-- image_ref -->

1. The option This Argument is required must be as defined in the template.

> **Note：** Note The default values and description of the arguments may be different than those defined in the template.

![](images/tc_templ_change_proc_ArgsNameOrder_in_newTC.png) <!-- image_ref -->

![*](bullet_blue.jpg) <!-- image_ref -->

1. Description and Default value: You may modify these values as required in the new testcase.

1. 3 Response: The Block response type and Sample data is validated to ensure that it is the same as the template definition. Modifying these definitions displays an error as shown below.

![](images/tc_templ_change_proc_ResponseType_in_newTC.png) <!-- image_ref -->

> **Note：** Note The QuickCall or TestCase that links to the generated template (Implementation) and template should have the same response JSON/YAML keys and the values can be different.
