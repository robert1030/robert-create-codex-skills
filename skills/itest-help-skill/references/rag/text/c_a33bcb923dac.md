# Python Sessions > Execute Python session Test Case

You may run the Python command steps captured to a Test Case as any the other test case. When the execution completed, the test report will be generated.

Open the test case, click Start Execution in New Window. iTest Python terminal session opens and starts executing the steps in the test case. When the execution completed, the test report will be generated.

![](images/py_run_rendered_TC.png) <!-- image_ref -->

If you have defined any Initialization script, iTest will invoke the Initialization script (in section Create and run a Python Session) automatically when launching the Python session.

> **Note：** Note If any exceptions occur due to the Initialization script execution, the open step fails and an error message displays.

Also, if you have specified Additional module paths, iTest will import the script from the absolutely path or the relative path as defined (Additional Modules in section Create and run a Python Session).

![](images/py_init_script_execution_import_script.png) <!-- image_ref -->

> **Note：** Note iTest also includes any/all paths specified in the PYTHONPATH environment variable in the module search path list.

When the Initialization script executes, the output from the script will be shown as part of Python session open step as shown below.

![](images/py_init_script_execution.png) <!-- image_ref -->
