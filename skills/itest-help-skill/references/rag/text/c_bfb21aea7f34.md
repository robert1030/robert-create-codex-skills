# Actions > Actions for CLI session types > The ‘eval’ action: Evaluate an iTest interpreter command > The ‘run’ action: Execute the specified test case

A run step executes the specified test case (the child test case — sometimes called a foreign or an external test case) and optionally passes parameter values.

See Executing a child test case: The ‘run’ action.

> **Note：** Note If a call step in a child test case B (begun by a run step in a grandparent test case A) calls grandchild test case C: The called test case C will use the shared session from test case A in its open step if the Session ID in C is same as the Session ID in A. If you do not want to use the shared session, then change the Session ID in C to be different from the Session ID in A.
