---
{
  "chunk_id": "procedures_call_proc_add_args__foreign_procedure_4c52da8a3d2870fa",
  "source_file": "topics/procedures_call_proc_add_args.htm",
  "source_original_path": "topics/procedures_call_proc_add_args.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "Creating a procedure ‘call’ step using in-line editing"
  ],
  "heading_path": [
    "Creating a procedure ‘call’ step using in-line editing",
    "Creating a procedure ‘call’ step using in-line editing",
    "To call a procedure",
    "Foreign procedure:"
  ],
  "anchor": "1285237",
  "context_ids": [
    "procedures_call_proc_add_args"
  ],
  "index_keywords": [
    "adding to a procedure call"
  ],
  "index_keyword_paths": [
    "arguments > adding to a procedure call"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "4c52da8a3d2870fa",
  "level": 4
}
---

# Creating a procedure ‘call’ step using in-line editing > Creating a procedure ‘call’ step using in-line editing > To call a procedure > Foreign procedure:

1. In the Description cell, open the drop-down list and double-click the procedure library. The list displays local procedures by name and procedure libraries as URIs followed by a ? character.

1. 2

1. Now you select a particular procedure from the library, as follows:

- Press Ctrl+Space. iTest displays a drop-down list of the procedures defined in the procedure library.

> **Note:** Note Only the procedures specified as “callable” appear in the list (that is, procedures with the Include this procedure when listing callable procedures property checked).

- When you select a procedure, another popup displays the properties for the procedure. Double-click the procedure. It is appended to the URI of the procedure library.

> **Note:** Note When editing a test case, if you enable the "Perform command, variable, and backslash substitution" behavior on a call step (by clicking the checkbox in the step property), iTest displays a warning message as follws and requires you to acknowledge what you are doing.

Call steps already perform command, variable, and backslash substitutions. Enabling this may result in unexpected double substitution and should be avoided in most cases. However, to call a procedure with arguments through substitution, this option would need to be enabled.



Step 3: Specify arguments

If the procedure uses arguments, follow these steps to add them:

> **Note:** Note There is no need to specify arguments that have defined default values. If you do not add the argument to the command line, then iTest executes the procedure using the specified Default value for the argument.

1. Type a space to separate the argument from the procedure name.

1. 2

1. Type a hyphen “-” to display the list of named arguments. When you select an argument, then another popup displays the argument name and the other property settings from the Arguments property page (if the properties are set).

1. 3

1. Double-click an argument to add it to the command for the procedure call. To add a value for the argument, type a space followed by the value. You can use field replacements in arguments.

1. 4

1. Add all required arguments in this way. Separate all arguments and values using a single space.



Step 4: Finish

After you finish editing the command text in the Description cell (adding the procedure name and any arguments) and exit the cell, the full URI to the procedure library will no longer appear — only the test case name, a ? character, and the procedure name plus arguments remain. This makes it easier to read and understand the step.

Tcl example:

project://my_project/test_cases/my_lib.fftc?login

will change to

my_lib?login

Python example:

project://my_project/test_cases/my_lib.fftc?login

will change to

my_lib#login

To change the behavior to always display the full URI, specify the preference setting as follows: Click Window > Preferences. On the Preferences page, click Spirent > Editors > Test Case Editor > EXEC steps. Check Display the full URIs for foreign procedure calls.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
