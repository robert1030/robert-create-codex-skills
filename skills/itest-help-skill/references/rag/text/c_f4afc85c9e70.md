# Parameters > Merging parameter definitions from multiple sources > Parameter definitions handling at runtime > Parameter definitions handling when using TCL interpreter

If a test case parameter definitions include duplicate nodes (same node names as defined in a parameter file), the parameters are concatenated to form a list when executing the test case.

Example 1: Parameter definition in the Test Case Editor > Parameters tab and a parameters file (.fftp) which is set as a global parameter file.

![](images/param_DuplicateRootDefinitions.png) <!-- image_ref -->

Example 2: Parameter values are concatenated whenever duplicate nodes are present in parameters definition (Test Case Editor > Parameters tab and a parameter file).

![](images/param_PythonTclConcatenatedDuplicateRoots.png) <!-- image_ref -->
