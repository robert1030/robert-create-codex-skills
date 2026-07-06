# Test Cases > Running child test cases > Executing a child test case: The ‘run’ action > How topologies are used when running child test cases

If a test case calls a procedure in a child test case (a child procedure), then the URI specified in the child test case is not used. Instead, the topologies specified in the calling test case is used.

If an open step in the child procedure refers to a device URI, then the URI will be replaced using the current topology that was loaded at start of execution.
