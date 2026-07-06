# Test Cases > Running child test cases > Executing a child test case: The ‘run’ action > Display two tables: unexpected followed by all tests

![](images/test_cases.6.jpg) <!-- image_ref -->

1. 6 Parameters: Specify the sources for parameter settings that the child test case should use during execution. In the default configuration, only parameters associated with the test case and no others are used.

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

Use specified parameter file: If you want to use a parameter file, then you must specify the file in the Parameter file property. Use parameter file from parent. Use the parameter file specified for the parent test case

Note This option is not recommended because it can cause duplicate parameters to be created. In addition, the snapshot may include parameters from other child test cases.

- **Parameter file to use**：This property determines the source of the parameter file. Default: Use specified parameter file
- **Parameter file**：Optional This property is used when you select Use specified parameter file for the Parameter file to use property. Specify the parameter file to use while executing the child test case. If blank, then no parameter file is used. Default: [blank]
- **Include parameters that were individually passed to parent test case**：Check the box to cause the child test case to use parameter values as specified in the parent test case. This includes Advanced Merging property settings. Default: unchecked
- **Parameters**：Use the specified parameter values while executing the child test case. Parameters that you specify here take precedence over the parameters from any other source. Type only one name=value pair per line. Specify each parameter setting as <name>=<value>, for example, port=3.
- **Initialize using a snapshot of current parameters**：Check the box to cause the child test case to use parameter values as currently in use. This includes Advanced Merging property settings. Default: unchecked
