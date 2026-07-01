---
{
  "chunk_id": "tips_and_tricks__tips_and_tricks_060729da68063e89",
  "source_file": "topics/tips_and_tricks.htm",
  "source_original_path": "topics/tips_and_tricks.htm",
  "toc_path": [
    "iTest Online Help",
    "Wizards and Dialog boxes",
    "Tips and Tricks"
  ],
  "heading_path": [
    "Tips and Tricks",
    "Tips and Tricks"
  ],
  "anchor": "1155363",
  "context_ids": [
    "tips_and_tricks"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "060729da68063e89",
  "level": 1
}
---

# Tips and Tricks > Tips and Tricks

- The Spirent Community offers valuable information for new users and experts alike. Discussion forums, video tutorials, and example projects.

- For richer documentation on the progress of execution, check the box for 'Generate an execution message for each comment step that is executed' (on the 'General' page of the Test Case editor)

- If you have developed the perfect layout for your perspective, make it your personal custom perspective by clicking 'Window > Save Perspective As'

- You can drop single (or multiple) steps from the Capture view into your test case

- Every view and editor has 'Minimize' and 'Maximize' buttons in the upper right. When minimized, sizing tools appear in the upper left.

- After you create a rule using the analysis rule wizard, you can edit it as needed — right-click the rule and select 'Edit Analysis Rule'

- Use Ctrl+3 to open any view or perspective by typing its name

- Indent steps under Comment steps to organize your test case into functional modules — the comment text is the title of the module. You can click the 'Collapse All' button to work on one module at a time.

- Use $value in field replacements in analysis rule messages to display the value being validated

- If you can’t find a particular view, try clicking the 'Reset Layout' button

- Use the Capture Comments view to document your work as you capture (anything you type gets added as a Comment step in the test case).

- Comment text can include field replacements. This is an easy way to send data to the Execution view.

- Double-click a tab to maximize a view or editor. Double-click it again to minimize it.

- To improve performance, iTest does not map all items in very long responses. If you notice that the “blue boxes” do not appear in the later text of a response, you can increase the setting so that iTest evaluates more queries. Click 'Window > Preferences'. In the 'iTest' group, go to 'Response Mapping' and increase the 'Maximum number of queries to evaluate' setting.

- For a single item in the Capture view, Shift-drop the item into an active session window of the appropriate session type. iTest pastes the command into the session window, but does not execute it. This option enables you to edit the command before submitting it.

- Place a QuickCall library in the same folder as the session profile that it is associated with and with the same filename. For example, router3A.ffsp and router3A.fftc

- While working on QuickCall definitions on the Test Case editor 'Steps' page, click the Collapse All button to view only the QuickCall names and not the individual steps. You can then work on a single QuickCall definition without the clutter.

- Ctrl+Shift+Q is the same as clicking the QuickCall button, and the 'Execute a QuickCall' wizard is optimized for keystroke‑only use so that manual testers need never use the mouse while performing a QuickCall.

- By default, arguments support runtime substitution of field replacement text. To disable substitution for an argument value, wrap the value inside { and } brackets. As a result, the argument text will be passed exactly as it appears and no substitution will occur.

- When iTest executes a QuickCall, the Query view lists the QuickCall library where the QuickCall is defined.

- Here is an easy way to add a 'run' step: While editing a test case, right-click the child test case in the Favorites view and select 'Insert step to run this test case'. The run step is added after the selected step.

- Add a 'comment' step and indent any number of related steps under the comment. You can then skip all of the steps by skipping only the comment step. In addition, you can collapse (fold) the comment step to temporarily hide the related steps to reduce clutter while editing.

- To view the description of any action, add a step and begin to type the action into the 'Action' cell. As you type, iTest displays a list of actions. When you select an action, iTest displays a brief description with a link to more complete help.

- You should know about a powerful alternative to procedures: The iTest QuickCall feature makes it easy to add custom actions to the built-in iTest actions (e.g., 'getTable' in SNMP sessions). You can use QuickCalls both during interactive (manual) testing and in test case steps.

- Comment steps are a great way to outline or pseudo-code a test case before adding actual steps. To add comments quickly, select a Comment step and then press Ctrl-Enter. Once your outline is complete, you can go back and insert commands.

- Use a Mail session and a 'response' field replacement to write the response to the 'summarize' action into the body of an email message

- You can use 'readFile' action to obtain text data and then use analysis rules for the step to save appropriate data items into variables for use later in the test case (using get, ${varName}, gget, or ${/data/varName}, as appropriate). In the text of the file, you might use delimiter characters (for example, commas or colons) to delimit data values to make extraction easier in the analysis rule.

- You can type escape sequences for non-printing characters directly into any command or property text.

- In any field that supports field replacements (including test case commands), the fastest way to insert a 'param' command is to right-click where the command should appear and then select 'Insert Parameter'.

- In any field that supports field replacements, the fastest way to insert a query on a stored response is to right-click where the query should go and select 'Insert > Query on Stored Response'.

- You can associate a response map with a procedure so that the response returned by the procedure will automatically have “blue boxes” — structured queries — available on the corresponding call step.

- On the Test Case editor 'Steps' page, click the 'Collapse All' button to remove clutter by displaying only the procedure names and not the individual steps.

- A 'write' step adds text into the response of a 'call' step. In a called procedure, you can use 'write' steps to include response text from multiple steps in the called procedure (as a multi-line string). The text that appears in the 'Description' cell of the 'write' step is appended to the response.

- You can use a 'return' step in the main procedure to exit a test case. Because you do not typically want to return every time the test case runs, you'll probably include the return step within an 'if' construct.

- A simple and powerful way to manually execute a series of CLI commands is to save the command text in a text file (for example, a Notepad text file). Copy the commands and then paste them into an active session window. The commands execute immediately.

- You have the option to save only selected sections of any report when you export it. See the help topic on “Customizing the content of a test report”.

- In iTest editors, Undo/redo (Ctrl-Z, Ctrl-Y) applies to any change.

- Use the iTestRT reporting plug-ins to publish reports in various ways.

- You can store a value from the response to a step (say, step 12). In a later step (say, step 19), you can add an analysis rule about a token in step 19 and compare its value to the value of the token extracted in step 12. So, for step 19, you can create an assertion like: $value = $tokenStep12 * 2

- To avoid unnecessary interruption while testing, after you have added all prompt definitions to a session profile or device definition, you can uncheck 'Learn prompts' in the 'Capture' properties group.

- The response map chaining feature enables you to specify that, during the mapping process, any response that does not find an applicable map in the specified response map library (or all applicable maps fail) should also check for applicable maps in one or more other libraries.

- You can use the last page of the 'New Response Map' wizard to have iTest take a first try at automatically generating a map for a response. (Click the 'Create a New Response Map' button in the Response view.)

- If you expect very large responses, allocate more memory to iTest. See the help topic on “Specifying how much memory to allocate to iTest”.

- While execution is paused, you can perform interactive actions in the session to view the results. If a step is useful, you might later add it to the test case. While execution is paused, the current step is marked in the Test Case editor with a yellow arrow.

- The Test Reports view offers an option to display only the 'latest' or most recent report for every test case. You might use this option while iteratively developing and executing a test case. When you finish, pick the last execution of each new test case that you developed that day and report the results.

- When you close a session with an exit command, the 'close' step is captured and (if so configured) the session window remains open. (To configure the session window to remain open after you disconnect a session, set the following two 'Execution' preferences appropriately: 'When execution finishes, close all Sessions windows' and, 'Before executing, close all active and inactive session windows'.)

- For an 'open' step in a test case, you have the option to override any of the property settings so that all steps in the session use the new property settings. Change any of the properties for the 'open' step that appears in the '<sessionType> Session Properties' section.

- Command Prompt : If an application does not run in a Command Prompt session, try running it on a Linux computer and using a Telnet session to test it.

- For Database sessions: If you are creating a step that you will eventually put into a loop, fetch records one-at-a-time. A record will be returned each time the loop encounters the step

- SNMP: To ensure good performance, add only the MIBs that you expect to use for testing.

- SNMP: On the 'Preferences' page, you can configure iTest to open the SNMP Traps view when a trap is received.

- SNMP: Clicking a node in the component tree is equivalent to populating the address bar (based on the tree node) and clicking 'Go'. The Application Under Test goes to the specified component.

- SNMP: Double-clicking a node in the component tree is equivalent to populating the address bar and then clicking 'Describe'.

- Use the text box at the top of the Structure view to test XPath expressions.

- Web: You can capture a snapshot of a Web page and the XML representation of the HTML code of the page. This feature is useful both for documenting the test case and for identifying targets when creating form maps. See the help topic on the Snapshot button.

- To locate a file or other resource quickly, press CTRL+SHIFT+R and begin typing the name

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
