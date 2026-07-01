---
{
  "chunk_id": "procedure_call_wizard__to_add_a_call_step_b36bb14e7787c63f",
  "source_file": "topics/procedure_call_wizard.htm",
  "source_original_path": "topics/procedure_call_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "Creating a ‘call’ step using the Procedure Call wizard"
  ],
  "heading_path": [
    "Creating a ‘call’ step using the Procedure Call wizard",
    "Creating a ‘call’ step using the Procedure Call wizard",
    "To add a call step"
  ],
  "anchor": "1439808",
  "context_ids": [
    "procedure_call_wizard"
  ],
  "index_keywords": [
    "Procedure Call",
    "Procedure Call wizard",
    "adding to a procedure call"
  ],
  "index_keyword_paths": [
    "Procedure Call wizard",
    "arguments > adding to a procedure call",
    "wizards > Procedure Call"
  ],
  "related_links": [
    "procedures_call_proc_add_args.htm#1279291",
    "action_call.htm#1384995"
  ],
  "images": [
    "topics/images/procedures.2.jpg",
    "topics/images/procedures.3.jpg"
  ],
  "content_hash": "b36bb14e7787c63f",
  "level": 2
}
---

# Creating a ‘call’ step using the Procedure Call wizard > Creating a ‘call’ step using the Procedure Call wizard > To add a call step

Start the Procedure Call wizard using one of the following methods:

1. Select the step just before where the call step should go.

1. 2

1. Now, do one of the following:

- In the toolbar, select the arrow on the Insert button and select Insert Procedure Call Using Wizard

- Right‑click the step and select Insert > Insert Procedure Call Using Wizard

- In the Test Case menu, select Insert > Insert Procedure Call Using Wizard

- Add a step with an Action of call. Optional: If you know the name of the procedure to call, you can specify its name in the Description cell (as described in Step 2: Specify the procedure to call). As a result, the wizard page will be “filled in” with information about the procedure. Click in the Description cell to start the Procedure Call wizard.

Now, work in the Procedure Call wizard

1. 3

1. In the Test Case box, select the test case (procedure library) that contains the procedure.

1. 4

1. In the Procedure box, select the procedure.

1. 5

1. Now you can view and edit argument settings.

As you work, you will notice that the Command text box is updated to reflect your changes. The text in the Command text box is usually exactly what you need, but if necessary, you can edit the text directly (for example, to add numbered arguments).

> **Note:** Note The text in the Command Text box follows the normal convention for procedure calls; an argument that uses its default value does not appear. When the call step executes, however, the default value will be passed to the procedure in the normal way.

- When you select an argument, the Description box displays the argument name and other property settings for the argument. If the person who defined the argument set the appropriate values, then this information should help you to understand the argument and its usage.

- The Arguments table lists all named arguments. An argument’s default value (if defined) appears in the Value cell.

- To change a value, click in the Value cell and type the new value.

- To reset a particular argument to its default value, change the Use Default setting to Yes.

- To set each argument to its default value, click Reset All to Default Values.

- The icon appears in the title of the Arguments table and in the first column for any required argument that has no value.

- The wizard does not add numbered arguments. You can type numbered argument values into the Command Text box after all of the named arguments. For details on specifying argument values, see About arguments in procedure calls.

> **Tip:** Tip By default, procedure arguments support runtime substitution of field replacements. To disable substitution for an argument value, wrap the value inside { and } brackets. As a result, the argument text will be passed exactly as it appears and no substitution will occur.

1. 6

1. When you finish defining the procedure call, click OK. iTest places the text from the Command Text box into the Description cell for the call step.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![inline_icon](topics/images/procedures.2.jpg) <!-- image_chunk: img_20ee4b2ad30c315b -->

![screenshot](topics/images/procedures.3.jpg) <!-- image_chunk: img_29d0bda7cd326bdb -->
