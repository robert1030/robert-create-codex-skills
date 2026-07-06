# Spirent Avalanche sessions > Session profile property settings for Spirent Avalanche sessions > Session Properties > 第1段

The first two properties are associated with the option to execute the test defined in the Avalanche-generated test.tcl and config.tcl files. See Executing Avalanche-generated ‘Tcl test’ scripts directly (Pass‑Through Mode).

Note This is also the working folder for test Specifying cards, slots, port groups, and ports/virtual portst execution. All files that are generated during execution (for example, results) are stored in this folder.

- **Use Avalanche Tcl test files**：Check the box to execute the test defined in the Avalanche-generated test.tcl and config.tcl files. See Executing Avalanche-generated ‘Tcl test’ scripts directly (Pass‑Through Mode). If you check the box, then you must specify the path to the folder that holds the config.tcl and test.tcl files in the Tcl test folder property Uncheck the box to cause iTest to execute the test.tcl script and execute a default config.tcl script. When iTest processes test.tcl, several settings are parameterized, enabling you to configure them during the session using the Configure button. See Test Control section for details. Default: unchecked
- **Tcl test folder**：Used only if Use Avalanche Tcl test files is checked. Specify the path to the Tcl test folder that holds the Avalanche-generated test.tcl and config.tcl scripts. Default: [blank]

The following property settings are used only if Use Avalanche Tcl test files is unchecked. See Running an Avalanche test on a TestCenter device (Normal mode).

Note Be sure to review Specifying cards, slots, port groups, and ports/virtual ports before setting values.
