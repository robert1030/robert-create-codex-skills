---
{
  "chunk_id": "commands_adding_to_steps__overview_inserting_a_command_as_a_field__37c5c7fc93bf6fbe",
  "source_file": "topics/commands_adding_to_steps.htm",
  "source_original_path": "topics/commands_adding_to_steps.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "iTest interpreter commands",
    "Adding iTest interpreter commands to steps"
  ],
  "heading_path": [
    "Adding iTest interpreter commands to steps",
    "Adding iTest interpreter commands to steps",
    "Overview: Inserting a command as a field replacement"
  ],
  "anchor": "1174775",
  "context_ids": [
    "commands_adding_to_steps"
  ],
  "index_keywords": [
    "inserting as field replacements",
    "inserting commands as",
    "inserting iTest commands into",
    "inserting into property settings",
    "inserting into steps"
  ],
  "index_keyword_paths": [
    "commands > inserting as field replacements",
    "commands > inserting into property settings",
    "commands > inserting into steps",
    "field replacements > inserting commands as",
    "steps > inserting iTest commands into"
  ],
  "related_links": [
    "insert_field_tool.htm#1120348",
    "field_replacements_tasks.htm#"
  ],
  "images": [
    "topics/images/commands_2.3.jpg",
    "topics/images/commands.4.jpg"
  ],
  "content_hash": "37c5c7fc93bf6fbe",
  "level": 2
}
---

# Adding iTest interpreter commands to steps > Adding iTest interpreter commands to steps > Overview: Inserting a command as a field replacement

You can insert any command as a field replacement into an existing step Description or into a property setting. At runtime, before the property or step is interpreted, iTest substitutes the returned value for the field replacement. The generic format for a field replacement is:

[commandName args] in Tcl or commandName('arg') in Python

You do not have to remember the field replacement syntax. Just right-click anywhere that you can add a field replacement and select Insert to insert a properly formatted field replacement with hints about argument usage.

In this example, we have added the first portion of a device’s interface ethernet command (it is not a iTest command, rather a CLI command to the device’s management interface).

The interface ethernet command requires a port number as the argument (for example, interface ethernet 9). We want the iTest step to determine the port number dynamically at runtime from a parameter that supplies the value. We will add the port argument to the command text as a iTest param command. During execution, the param command will be replaced by the port number.

So, we place the cursor after “ethernet”, right-click, select Insert, and then select Parameter. The Insert Field tool then helps us to select the particular parameter to use (we chose “port”) and then inserts a param command (within the [ and ] brackets of a field replacement). Now the command will execute as desired.

For more detailed instructions, see Inserting field replacements using the Insert Field tool. Field replacements are fully described in “Field Replacements”.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/commands_2.3.jpg) <!-- image_chunk: img_ccdce967c7fdf1b3 -->

![screenshot](topics/images/commands.4.jpg) <!-- image_chunk: img_4c88563957500f35 -->
