---
{
  "chunk_id": "quickcalls_execute_quickcall_wizard__executing_a_quickcall_during_an_interact_1bf03f2e323e3b49",
  "source_file": "topics/quickcalls_execute_quickcall_wizard.htm",
  "source_original_path": "topics/quickcalls_execute_quickcall_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "QuickCalls: Defining and using a library of custom actions",
    "Executing a QuickCall during a manual (interactive) session",
    "Executing a QuickCall during an interactive session"
  ],
  "heading_path": [
    "Executing a QuickCall during an interactive session",
    "Executing a QuickCall during an interactive session"
  ],
  "anchor": "1404132",
  "context_ids": [
    "quickcalls_execute_quickcall_wizard"
  ],
  "index_keywords": [
    "adding to a procedure call",
    "changing argument values",
    "specifying in session actions"
  ],
  "index_keyword_paths": [
    "arguments > adding to a procedure call",
    "arguments > specifying in session actions",
    "session actions > changing argument values"
  ],
  "related_links": [
    "quickcalls_arguments_in_quickcall_steps.htm#1403617"
  ],
  "images": [
    "topics/images/quickcalls.01.jpg",
    "topics/images/quickcalls_2.02.jpg",
    "topics/images/quickcalls_2.03.jpg",
    "topics/images/quickcalls_2.04.jpg",
    "topics/images/quickcalls_2.05.jpg",
    "topics/images/quickcalls_2.06.jpg",
    "topics/images/quickcalls_2.07.jpg",
    "topics/images/quickcalls_2.09.jpg"
  ],
  "content_hash": "1bf03f2e323e3b49",
  "level": 1
}
---

# Executing a QuickCall during an interactive session > Executing a QuickCall during an interactive session

During an interactive session, iTest executes each step in the QuickCall as if you had typed each command yourself. So, with a single click (typically), you can interactively perform a complex initialization or clean-up routine or submit a long sequence of steps that must happen together.

When you execute a QuickCall, iTest captures the action in the Capture view.



To execute a QuickCall during a manual session

1. You can either click or click the down-arrow on the button.

- Click to open the Execute a QuickCall wizard (described in the next step).

- Click the down-arrow to select a QuickCall from a drop-down list.

> **Tip:** Tip Ctrl+Shift+Q is the same as clicking .

1. 2

1. Now:

- If the selected QuickCall does not use named arguments, iTest immediately executes the steps in the QuickCall. (This is the default behavior — you can set a iTest preference that causes iTest to display the Execute a QuickCall wizard [described next].)

- If the QuickCall uses named arguments or if you clicked , iTest opens the Execute a QuickCall wizard to enable you to view named arguments and to modify argument values as needed. The result of your work in the wizard will be to execute the QuickCall using the argument values you specify.

> **Tip:** Tips The Execute a QuickCall wizard is optimized for keystroke‑only use so that manual testers need never use the mouse while performing a QuickCall.You can use the wizard to execute QuickCalls in any active session, not just the session that you used to start the wizard.

1. 3

1. Now you can view and edit argument settings.

As you work, you will notice that the Command text box is updated to reflect your changes. The text in the Command text box is usually exactly what you need, but if necessary, you can edit the text directly (for example, to modify an argument value or to add numbered arguments).

> **Note:** Note The text in the Command Text box follows the normal convention for procedure calls; an argument that uses its default value does not appear. When the call step executes, however, the default value will be passed to the QuickCall in the normal way.

- When you select an argument, the Description box displays the argument name and other property settings for the argument. If the person who defined the argument set the appropriate values, then this information should help you to understand the argument and its usage.

- The Arguments table lists all named arguments. An argument’s default value (if defined) appears in the Value cell.

- To change a value, click in the Value cell and type the new value.

- To reset a particular argument to its default value, change the Use Default setting to Yes.

- To set each argument to its default value, click Reset All to Default Values.

- The icon appears in the title of the Arguments table and in the first column for any required argument that currently has no value.

- The wizard does not add numbered arguments. You can type numbered argument values into the Command Text box after all of the named arguments. For details on specifying argument values, see About arguments in QuickCall steps.

> **Tip:** Tip By default, arguments support runtime substitution of field replacement text. To disable substitution for an argument value, wrap the value inside { and } brackets. As a result, the argument text will be passed exactly as it appears and no substitution will occur.

1. 4

1. When you finish working in the wizard, click OK. iTest executes the QuickCall using the argument values that you specified.



To insert comments or ‘sleep’ steps while capturing manual tests

While working in an interactive session that you plan to save as an automated test case, you can type a comment—the text will later appear in the captured test case as a comment step.

In the same way, you can insert a sleep step at the appropriate location in the resulting test case.

To insert a comment or sleep step, click the down-arrow in the QuickCall menu and select the appropriate action.

![unknown](topics/images/quickcalls.01.jpg) <!-- image_chunk: img_2606c056de6a6db1 -->

![inline_icon](topics/images/quickcalls_2.02.jpg) <!-- image_chunk: img_eed1211fcc419801 -->

![unknown](topics/images/quickcalls_2.03.jpg) <!-- image_chunk: img_c5933101f6664629 -->

![inline_icon](topics/images/quickcalls_2.04.jpg) <!-- image_chunk: img_445df559925f3225 -->

![unknown](topics/images/quickcalls_2.05.jpg) <!-- image_chunk: img_ce4baa00c3c9803f -->

![unknown](topics/images/quickcalls_2.06.jpg) <!-- image_chunk: img_e856e46c76a417de -->

![screenshot](topics/images/quickcalls_2.07.jpg) <!-- image_chunk: img_ff93628e38230ddb -->

![inline_icon](topics/images/quickcalls_2.09.jpg) <!-- image_chunk: img_c2128623e2c0a5eb -->
