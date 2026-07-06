# Test Cases > Test suites: Organizing tests for group execution > Skipping Steps

While developing and troubleshooting a test case, it is often helpful to skip execution for particular steps (like steps that you know work or do not work or that take a long time to complete).

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Skipped steps are not executed and do not appear in reports.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- iTest ignores breakpoints on skipped steps — the steps are skipped without pausing execution

![*](bullet_blue.jpg) <!-- image_ref -->

- In the steps grid, skipped steps are dimmed (grayed-out). In the example, steps 3 and 4 are skipped.

![](images/test_cases_7.1.jpg) <!-- image_ref -->

> **Tip：** Tip Add a comment step and indent any number of related steps under the comment. You can then skip all of the steps by skipping only the comment step. In addition, you can collapse (fold) the comment step to temporarily hide the related steps. See Tips on working with test case steps.
