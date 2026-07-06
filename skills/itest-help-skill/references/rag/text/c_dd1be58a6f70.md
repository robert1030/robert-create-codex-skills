# Parameters > Defining and managing parameters > Parameters merging logic in iTest test cases

The following examples describe the parameters merging logic in iTest test cases:

![*](bullet_blue.jpg) <!-- image_ref -->

1. If global parameter file has a parameter param1 with integer value, and test case defines a parameter with the same name, param1 with a string value, the integer value from the global parameter file takes precedence.

1. 2 If a source (e.g., testcase1.fftc) defines a parent parameter with child parameter, and a second source (e.g., testcase2.fftc) defines only a parent parameter with the same name, and if you wish to get the value of the parent, the merge results in the value of the child parameter. This is because a parent parameter cannot define values.

1. 3 When you call a procedure from a child test case defining its own parameters, from within a parent test case, the parameters from the child test are loaded to the heap memory of the parent test. That is, the children test case parameters remain accumulated in the heap memory.
