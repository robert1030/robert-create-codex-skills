# Form Maps > Form Map editor: Targets page

If you use the New Form Map wizard to generate a form map, then the wizard identifies targets on the page and auto-adds them to the form map definition. Let's take a look at the Targets page.

![](images/forms_target_generated_from_sample.png) <!-- image_ref -->

![*](bullet_blue.jpg) <!-- image_ref -->

1. To generate the list of targets on the web page, click the Generate from samples link. iTest identifies many of the targets on all of the samples, lists them here, and suggests a commonsense name for each target.

We scrolled through the list and selected the Advanced Search target.

1. 2 To improve on the suggested target names, select the target in the list and then edit the name as needed.

1. 3 Here's the actual query that finds the target during execution. Because the target has a “friendly” Target name (or alias), the test case developer does not need to work with the query.

1. 4 Use this section to define arguments for targets that take arguments.

> **Tip：** Tip The list of targets that test case developers see while adding (for example) a Web click or setText action, is the list as you see it on the Targets page. To make it easier for them to select targets, move the most popular targets to the top of the list. Let's use the Move Up button to move link_Advanced_Search to the top of the list.

If the web page has more than one form (for example, it has different contents, depending on device configuration) and you used the Samples page to add a new page map to the form map definition, then you can use the Targets page to auto-add the targets from the new sample.
