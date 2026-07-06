# Test Case Editor > General page on the Test Case Editor > Test Case editor: General page > Test Suite Reporting > 第1段

This group of properties configures reporting for test cases that are parent test cases that execute child test cases using EXEC.run steps. A test case that is made up of only run steps is called a test suite.

Because the default settings result in normal reporting for test cases that are not test suites, you do not have to change any of these settings for test cases that do not run other test cases. By default, the response to an EXEC summarize step includes the results only of the individual child test cases but not the test suites that executed them. This avoids double-counting of successes or failures.

You can specify the following reporting settings:

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

If this test case does not run child test cases (it contains no EXEC run steps), then display the results of this test case If this test case runs child test cases (it contains one or more EXEC run steps), then do not display the results of this test case

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

If this test case does not execute child test cases (it contains no EXEC run steps), then include this test case's execution messages If this test case has one or more child test cases (it contains one or more EXEC run steps), then do not include this test case's execution messages.
