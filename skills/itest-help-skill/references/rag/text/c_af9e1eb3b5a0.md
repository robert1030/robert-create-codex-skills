# Test Cases > Library Template > Creating a template from existing test cases > Creating a Library template > 第1段

![*](bullet_blue.jpg) <!-- image_ref -->

1. Create a test case with procedures, and/or property settings commonly. See example shown below.

![](images/tc_templ_define_common_procdures.png) <!-- image_ref -->

1. 2 Select the test case in the Project Explorer, right-click and then select Generate Library Template.

The Select library template destination displays.

![](images/tc_templ_right-click-generate-library-template.png) <!-- image_ref -->

![*](bullet_blue.jpg) <!-- image_ref -->

1. Container: The default location is the same as the location of the test case. You may browse and navigate to a different existing folder.

![*](bullet_blue.jpg) <!-- image_ref -->

1. File name: Default file name is lib_template. If the file name exists, an error displays saying the file name already exists. Provide a different file name, if required and click OK to save the library template.

In the original testcase, iTest adds a link to the new test case. That is, on the original TestCase > General tab, adds the library template location and name as shown in the screenshot below. If the original testcase already had this property filled, the value will be overwritten.

These public procedure definitions are copied to the new testcase from the original testcase.

![*](bullet_blue.jpg) <!-- image_ref -->

- Procedure name

![*](bullet_blue.jpg) <!-- image_ref -->

- Argument list, the order of the arguments, and properties for each argument: Name, Mandatory flag, and Default value

![*](bullet_blue.jpg) <!-- image_ref -->

- Procedure response type and Sample

> **Note：** Note If original testcase was marked as a procedure library, the new testcase will also be marked as a procedure library.

Language of the testcase will be set to the default language selected in Windows > Preferences (as default when creating any new testcase).

XPath version of the newly created testcase will be set to 3.1 (as default when creating any new testcase).

Implementation

When you click Generate Library Template, a template is generated from the Testcase/QuickCall procedure library. The original test case will automatically have Library Template property (on Testcase > General tab) set to URL of the newly generated template. The original testcase is considered an implementation of the template. You can also manually set the Library Template URL to an existing template. The elements can be queried from the response structure of both template and the implementation of the template.
