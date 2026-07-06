# Python Sessions > Create a new Python session profile > Create and run a Python Session > 第2段

- **Path to interpreter**：Enter the path to the interpreter to be used for this particular session. If you do not specify a path to the interpreter, iTest uses the path specified in the preferences setting. See Preferences: Spirent > Python Interpreter.
- **Working directory**：Indicates the initial working directory to use for submitting commands when the Python session starts. Execution on iTestRT: If Working directory is not set and the session profile is in an external itar, then the current working directory will be set to the temp path for execution (where the exploded contents of downloaded projects exist). Execution on Velocity Agent: If Working directory is not set then the current working directory will be the temp path the agent uses for execution (where the exploded contents of downloaded projects exist).
- **Initialization script**：Enter a script that iTest will invoke automatically when launching the Python session. When you launch the session, the script (from initialization script) will run and display the script output.

![](images/py_initialization_script.png) <!-- image_ref -->

| 欄位1 | 欄位2 |
| --- | --- |
| Additional Modules | The directory path entered here is used to search and locate additional modules and importing modules. Add: Enter path and the Add button becomes available. Click Add to include path to the list above. Both absolute path and relative path is supported. Browse: Click Browse, navigate to the location that should be searched to import additional module,. and click OK to add the path to the list. Subsequent paths added will be appended to the list. You may edit the list of path Delete: Select the path and click delete to remove the path from the search list. Launch Python session and notice that both absolute path and relative paths are valid. Files will be Imported from both relative or absolute paths. |

![](images/py_additional_modules.png) <!-- image_ref -->

You may also define path(s) in the OS environment variable PYTHONPATH and iTest will include it in the module search list. Create PYTHONPATH environment variable in global variables.

PYTHONPATH set on the local environment identifies the folder where the additional modules are placed, so that iTest can include this path in the search list and import modules.

Large Responses

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->
