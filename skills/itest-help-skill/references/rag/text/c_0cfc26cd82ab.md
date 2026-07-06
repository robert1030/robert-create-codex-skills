# Test Reports > Test reports overview > Controlling which executed steps appear in test reports > Execution issues

If a child step of any step that is configured not to appear in reports has an execution issue, then, in the list of execution messages in the Execution view, the issue’s icon appears next to the message for its nearest ancestor. The step index for the issue is associated with the child step that had the issue, so you can double-click the issue to open the Test Case editor to the child step that had the issue.



To specify that a step should not appear in test reports

![*](bullet_blue.jpg) <!-- image_ref -->

1. In the Test Report editor, select the step or steps.

1. 2 In the General properties group, uncheck Include this step and its children in test reports.



To override the “no-report” setting: To specify that all steps should appear in test reports, regardless of the settings for the individual steps

You might want to include all steps in test reports, even though individual steps might be configured not to appear. Follow this procedure:

1. 1 Click Window > Preferences.

1. 2 On the Preferences page, in the Spirent group, navigate to General > Execution.

1. 3 Check Include all steps in test reports (ignore the setting for the step).



To override the “no-report” setting in iTestRT

iTestRT uses Boolean arguments to specify that all steps should appear in test reports, regardless of the settings for the individual steps:

iTestRT: --reportallsteps
