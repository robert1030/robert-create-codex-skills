# Wizards and Dialog boxes > Tips and Tricks > 第5段

- To avoid unnecessary interruption while testing, after you have added all prompt definitions to a session profile or device definition, you can uncheck 'Learn prompts' in the 'Capture' properties group.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The response map chaining feature enables you to specify that, during the mapping process, any response that does not find an applicable map in the specified response map library (or all applicable maps fail) should also check for applicable maps in one or more other libraries.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- You can use the last page of the 'New Response Map' wizard to have iTest take a first try at automatically generating a map for a response. (Click the 'Create a New Response Map' button in the Response view.)

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- If you expect very large responses, allocate more memory to iTest. See the help topic on “Specifying how much memory to allocate to iTest”.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- While execution is paused, you can perform interactive actions in the session to view the results. If a step is useful, you might later add it to the test case. While execution is paused, the current step is marked in the Test Case editor with a yellow arrow.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The Test Reports view offers an option to display only the 'latest' or most recent report for every test case. You might use this option while iteratively developing and executing a test case. When you finish, pick the last execution of each new test case that you developed that day and report the results.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- When you close a session with an exit command, the 'close' step is captured and (if so configured) the session window remains open. (To configure the session window to remain open after you disconnect a session, set the following two 'Execution' preferences appropriately: 'When execution finishes, close all Sessions windows' and, 'Before executing, close all active and inactive session windows'.)

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- For an 'open' step in a test case, you have the option to override any of the property settings so that all steps in the session use the new property settings. Change any of the properties for the 'open' step that appears in the '<sessionType> Session Properties' section.
