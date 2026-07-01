---
{
  "chunk_id": "param_parameters_type_secret__about_the_parameter_type_secret_0ed7e857a88d1e92",
  "source_file": "topics/param_parameters_type_secret.htm",
  "source_original_path": "topics/param_parameters_type_secret.htm",
  "toc_path": [
    "iTest Online Help",
    "Parameters",
    "Defining and managing parameters",
    "About the Parameter Type ‘Secret’"
  ],
  "heading_path": [
    "About the Parameter Type ‘Secret’",
    "About the Parameter Type ‘Secret’"
  ],
  "anchor": "1554375",
  "context_ids": [
    "param_parameters_type_secret"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "parameters.03.htm#1466510",
    "insert_parameter_dialog.htm#1135987",
    "arules_processor_properties.htm#1186331",
    "#1569142",
    "preferences.03.htm#1162820",
    "preferences_itest.htm#",
    "capture_and_include_secret_type_in_tc_step.htm#1487238",
    "response_map_secret_type.htm#1735972",
    "response_map_secret_type.htm#1128727",
    "rme_table_page.htm#1129584",
    "arules_processor_properties.htm#1641520",
    "views_cached_secrets.htm#1638058",
    "itestrt_commands.htm#1133277",
    "itestrt_commands.htm#1227483",
    "data_view.htm#1206665",
    "arw_rule_type_selection_page.htm#1207393",
    "arw_select_from_response_page.htm#1208352",
    "pal_preferences_session_level_control_agent.htm#1444627",
    "quickcalls_execute_quickcall_wizard.htm#1477504"
  ],
  "images": [
    "topics/images/password_secretType.png",
    "topics/images/parameters_3.2.jpg",
    "topics/images/param_session_run_add_Ip_attribute_value.png",
    "topics/images/param_secretHandlingAtRuntime.png",
    "topics/images/param_secretHandlingAtRuntime-whenCanceledPreviously.png"
  ],
  "content_hash": "0ed7e857a88d1e92",
  "level": 1
}
---

# About the Parameter Type ‘Secret’ > About the Parameter Type ‘Secret’

The parameter type Secret (in addition to Text, Boolean, Integer, Double, and Custom), when selected, does not allow you to define value in the Parameters tab (or file) and automatically displays value as masked during usage. The following lists the behavior of the parameter type Secret during definition in test case, execution, response view, and reports.

- Define parameters in the parameter file as described in Defining a parameter.

- Insert parameter in test case steps as described in Inserting a parameter into a property or test case step.

If the step command contains a Secret parameter type, its response will not be a secret. The response of that command will be shown as clear text in both the Response View and in the generated reports.

- Define rules for storing the parameter value as a secret (Analysis Rules > Store processor allows you to store a parameter value as a secret). See Analysis rules: Properties of the processor.

- Entering Secret type in Session Profile

| Password: When you start typing into the Password field (e.g. SSH password, REST basic authentication password, JKS (Java Keytool Store) password), iTest displays a dialog asking you whether you wish to use a secret parameter for this field (that is, to use a secret parameter from the session profile, parameters file, or test case), and provides you with an opportunity to add a secret in either of these locations. Clicking yes displays the Insert parameter wizard. See Adding a parameter definition while inserting password Click No to type the password into the field, which iTest encrypts. You may select the checkbox Do not show this dialog again to ensure that the prompt to use parameter does not display. See also Preferences: Spirent > Editors, Chapter 39, “Configuring iTest Preferences”. Mask content: The Mask Content field appears below the Password field, which is selected by default for Secret parameter type, and you may uncheck this selection. When you uncheck, iTest displays a Clear field content? dialog with a warning message informing that the masked data will be lost and whether you would to unmask the field and clear the content. The dialog also allows you to set your preference to not display this dialog again. You may select the checkbox Do not ask again to make sure that the Clear filed content? dialog does not display again. Click Yes to save your selection and acknowledge unmasking and clearing the content and No to discard the clear field content operation. See also Preferences: Spirent > Editors, Chapter 39, “Configuring iTest Preferences”. |  | You may select the checkbox Do not ask again to make sure that the Clear filed content? dialog does not display again. |  | Click Yes to save your selection and acknowledge unmasking and clearing the content and No to discard the clear field content operation. |
| --- | --- | --- | --- | --- |
|  | You may select the checkbox Do not ask again to make sure that the Clear filed content? dialog does not display again. |  |  |  |
|  | Click Yes to save your selection and acknowledge unmasking and clearing the content and No to discard the clear field content operation. |  |  |  |

Adding a parameter definition while inserting password

While inserting a parameter into a session profile, you may create a new parameter or insert parameter defined on the Session >Attributes tab or from a parameter file, e.g., [profile ('.', 'ssh_password')]. The following dialog appears when you click Yes on the Use a secret parameter for this field? dialog.

- Select the Parameter source, Global Parameters file or in the Session (Attributes tab), as required. Select the Secret parameter if the one automatically selected and displayed is not the one you required.

- You may click Add to enter a new parameter name (if required), which will be added on the Session > Attributes tab.

- Click Insert and iTest includes the Field Replacement syntax in the password filed.

When you start an interactive session, iTest displays dialog to prompt for secret attribute value and use the passed value.

On the Session Profile window, you may also define a secret attribute value to open the session on the Session Profile Attribute page, for example [profile ('.', 'ip')].

When you start an interactive session, iTest displays dialog to prompt for secret attribute value and use the passed value.

> **Note:** Note Window appears only if the session attribute is used to open the session. The Window does not appear if you have defined a session attribute that is not used in session properties.

For example:

> **Note:** Note Values defined in the Session Profile Attributes are not merged with the test case and global parameter.

- Secret Types in iTest Terminal sessions and captures

When running a terminal session, if secrets are detected (e.g., when you type a string that is not echoed in a terminal session, or prompted for a password), the following rule applies.

iTest does not write the Secret type parameter into the capture Database (even as an encrypted string). When you convert the session capture into a test case, a parameter secret type will be automatically generated and inserted into the test case step (instead of a secret value). The step command will reference the “parameter” command. See Captured Secret type in the Test Case step.

- Response map editor displays relevant secrets type keys and their values (secret values are masked) in the response, queries, and structure views. See Response Map Editor: Secret Type.

See Response map secret type definitions in Response Map editor: Queries page and Response Map editor: Table Map page.

In test case steps, if you selected the File to write response to and selected to hide value of the parameter type Secret (see Analysis rules: Properties of the processor, section Store processor) the data is not masked and stored as clear text in the response file.

When secrets are specified in a response map, iTest will not change the contents of a step's response (secret values are displayed as clear text).

- Handling Secret type values in during Test execution

At runtime, when the iTest GUI merges all parameters (from parameter file and test case), iTest will prompt you for the values of all Secret type parameters in the Value cell as shown below.

The secrets value are prompted for each parameter (in the parameter file and test case). The secrets value you entered are cached and enables you to run multiple tests in the same iTest session and maintain independent per-file secrets. Hence, cached secrets will not be prompted upon subsequent execution within the same iTest session.

You may remove any and all cached secrets while in an iTest session. See Cached Secrets View.

If you click Cancel, the session starts and iTest prompts you to enter a value only for the Secret type parameter defined in the Test Case.

> **Note:** Note The Test Case man fail if you have Secret type parameter defined in the parameter file as well.

Important If the test case step command contains a Secret parameter type, its response will not be a secret. The response of that command will be shown as clear text in both the Response View and in the generated reports.

- iTestRT: Secret handling during execution

To use the parameter Type Secret, define it with the --param parameter=secret value

iTestRT will not request the secret value at runtime. If you do not define the secret parameter at runtime, the test case will fail and display a message as follows: "Failed: Testcase requires secret value %{value} to be passed for proper execution".

See iTestRT command reference, Section Test Execution options.

- Displaying Secret Values in iTest.

- Secrets sent as input (command steps) are not masked in reports. For example, report display with the value of Secret parameter type in clear text.

- Secrets are not echoed on the session window at runtime (for example, in terminal sessions)

- At runtime, the Data view displays masked Secret type values.

Data view appears when you add a brake point (to see a value of a secret parameter you may insert a brake point after the command). See Data view.

- When executing a local test case, the value of the Secret type are masked by default and this value cannot be unmasked.

Important If the test case step command contains a Secret parameter type, its response will not be a secret. The response of that command will be shown as clear text in both the Response View and in the generated reports.

- Secret parameter type value entered during iTest execution appears as clear text in the iTest log file.

> **Note:** Note When running an execution as an iTest agent (either Velocity agent or Python SLC agent), the masked values of the Secret type cannot be unmasked.

- Analysis Rules (limitation in 8.3)

When a test case uses secret values:

- Adding analysis rules allows you to displays a message saying that the value contains a secret value instead of showing the Analysis Rule Wizard: Rule page (See Analysis Rule Wizard: Rule page).

- Adding a Query/XPath will also not be possible on the Analysis Rule Wizard: Extractor page (See Analysis Rule Wizard: Extract page).

- Executing QuickCalls with secret type parameter

When Python SLC connected to iTest GUI and try access QuickCalls with secret values will trigger iTest GUI to show dialog to enter this secret values.

Executing QuickCalls that required secret value when iTest GUI is configured in listening mode (see Configure Listening Mode (Listen for incoming Python connections)), a dialog displays for entering the secret value. However, no output will be sent to the SLC library as response for any QuickCalls use secret value. See Executing QuickCalls with secret type parameter.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/password_secretType.png) <!-- image_chunk: img_414b59070b2ea79a -->

![screenshot](topics/images/parameters_3.2.jpg) <!-- image_chunk: img_aabeb1e07fb8d25a -->

![screenshot](topics/images/param_session_run_add_Ip_attribute_value.png) <!-- image_chunk: img_f53bc8a8916cdaa9 -->

![screenshot](topics/images/param_secretHandlingAtRuntime.png) <!-- image_chunk: img_300a8a8304c0cce9 -->

![screenshot](topics/images/param_secretHandlingAtRuntime-whenCanceledPreviously.png) <!-- image_chunk: img_dd6910fa8903264d -->
