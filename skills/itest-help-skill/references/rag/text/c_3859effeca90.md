# iTest Runtime: iTestRT > iTestRT command reference > Test Execution options > Execution options > 第1段

You must specify all test execution options before the associated --test URI option.

> **Note：** Note For each test execution option (except --quiet): When multiple instances of the option appear before a particular instance of --test, then only the last instance is used. In this example, b.log will be used for job1 execution and c.log will be used for job2 execution:

```
itestrt --licenseServer lshost.acme.com:-1 --log file:/C:/a.log --log file:/C:/b.log --test file:/C:/job1.ffjd --log file:/C:/c.log --test file:/C:/job2.ffjd
```

The long forms of option names begin with: com.fnfr.open.runtime.executionengine

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

Note If you specify both --param and --paramfile in a iTestRT command, then values that you specify using the --param argument take precedence over the values in the parameter file. To use the parameter Type Secret, define it with the --param parameter=secret value

Note Use a single slash character after “file:” in the URI. For example:

Note If you specify both --param and --paramfile in a iTestRT command, then values that you specify using the --param argument take precedence over the values in the parameter file.

Note Use a single slash character after “file:” in the URI. For example:

Note

Note Use a single slash character after “file:” in the URI. For example:

Note

Note Use a single slash character after “file:” in the URI. For example:

Note
