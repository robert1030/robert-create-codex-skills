---
{
  "chunk_id": "session_profile_update_wizard__using_the_update_session_profile_wizard_ae462d416feb6656",
  "source_file": "topics/session_profile_update_wizard.htm",
  "source_original_path": "topics/session_profile_update_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Profiles",
    "Using the ‘Update Session Profile’ wizard"
  ],
  "heading_path": [
    "Using the ‘Update Session Profile’ wizard",
    "Using the ‘Update Session Profile’ wizard"
  ],
  "anchor": "1294433",
  "context_ids": [
    "session_profile_update_wizard"
  ],
  "index_keywords": [
    "Update Session Profile wizard"
  ],
  "index_keyword_paths": [
    "Update Session Profile wizard"
  ],
  "related_links": [
    "prompts.1.htm#1100299",
    "prompts.5.htm#1272830"
  ],
  "images": [
    "topics/images/update-sp_wiz_cmd_promt_page.png"
  ],
  "content_hash": "ae462d416feb6656",
  "level": 1
}
---

# Using the ‘Update Session Profile’ wizard > Using the ‘Update Session Profile’ wizard

While working in a session, you might encounter a prompt with a format that you have never seen before. You will probably recognize that the text is a prompt and continue with your work.

When iTest executes the session, however, it may have trouble recognizing the text as a prompt because the text does not match any of the prompt definitions in the session profile. Execution might be disrupted or the text might incorrectly be interpreted as part of the command. Similar issues arise with command completion characters and command break characters.

To avoid issues like this, iTest monitors captured responses to determine whether any new prompts or special characters appeared. If so, then after the session ends, iTest starts the Update Session Profile Device wizard to enable you to add the prompts and characters as configured properties in session profiles of your choice. As a result, future executions run correctly.

For an overview on how iTest recognizes prompts, see Overview: Prompts in iTest.

Step 1

Specify the session profiles or topologies to update

On the Session Profile or Topology page, specify the session profiles or topologies to update with the new property settings and then click Next. You can update a session defined on a topology and can also update:

- The session profile associated with the session that just ended

- If the session profile associated with the session that just ended inherits settings for another profile, then you can update any or all of the profiles in the inheritance chain

Specify which of the text strings are actually prompts

1. On the wizard’s Command Prompts page, iTest lists the possible prompts and you select the ones that actually are prompts.

- The Type drop-down list indicates the kind of prompt: Normal, Wildcard, or Regex. Default value is Normal.

- The Content value is the text that iTest noticed on the command line. You may edit the prompt content and allows an empty value.

- The Name field allows you to input the name of the prompt.

- This is mandatory, if empty, a warning message displays saying that the name must be specified.

- By default, the name will be auto-generated as follows: prompt + number.

- Prompt names are unique. When you enter the prompt name, if the checkbox is checked, iTest validates to ensure the name is unique. If this name is not unique, a warning message displays: Duplicate name exists.

The Next and Finish buttons will be disabled until a unique name is entered.

- The More next command field allows you to input text for more next command prompts This field value is optional.

- If the filed value is empty, this prompt is not a more prompt

- If the field value NOT empty, this prompt will be treated as a more... prompt and the text will be considered as more next command.

Later, when you have finished running the wizard, you can edit these and other properties to customize the prompt definition. For instructions, see Editing prompt definitions.

1. 2

1. Optional: The When using this session profile or topology device, do not automatically learn new prompts option tells iTest that, for future test runs, do not start the wizard to present any prospective prompts. Instead, treat all text as a response and use the Completion settings to determine when the step is finished executing.

Identify new command completion characters

When you perform manual testing, you frequently use characters like tab to auto-complete partially typed commands. To enable iTest to capture the completed form of commands and discard the incomplete form, it must know all command completion characters that you might use while executing test cases.

The wizard’s Command Completion Characters page is populated when iTest has noticed command completion characters that have not yet been configured.

Identify new command break characters

Most devices interpret certain characters to mean “break execution”. For example, Ctrl-C is a commonly used break character.

The wizard’s Command Break Characters page is populated when iTest has noticed break characters that have not yet been configured.

Finish

The Finish page gives you an opportunity to review what you have done before committing the changes.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/update-sp_wiz_cmd_promt_page.png) <!-- image_chunk: img_3196f6313ca4d262 -->
