---
{
  "chunk_id": "itestrt_commands__execution_options_0751ef73aefdd535",
  "source_file": "topics/itestrt_commands.htm",
  "source_original_path": "topics/itestrt_commands.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Runtime: iTestRT",
    "iTestRT command reference"
  ],
  "heading_path": [
    "iTestRT command reference",
    "iTestRT command reference",
    "Test Execution options",
    "Execution options"
  ],
  "anchor": "1255922",
  "context_ids": [
    "itestrt_commands"
  ],
  "index_keywords": [
    "command reference",
    "iTestRT",
    "iTestRT command reference"
  ],
  "index_keyword_paths": [
    "command reference > iTestRT",
    "iTest Runtime > iTestRT command reference",
    "iTestRT > command reference"
  ],
  "related_links": [
    "#1255776",
    "parameters_editor.htm#1323716",
    "parameters_page.htm#1135242"
  ],
  "images": [],
  "content_hash": "0751ef73aefdd535",
  "level": 3
}
---

# iTestRT command reference > iTestRT command reference > Test Execution options > Execution options

You must specify all test execution options before the associated --test URI option.

> **Note:** Note For each test execution option (except --quiet): When multiple instances of the option appear before a particular instance of --test, then only the last instance is used. In this example, b.log will be used for job1 execution and c.log will be used for job2 execution:

itestrt --licenseServer lshost.acme.com:-1 --log file:/C:/a.log --log file:/C:/b.log --test file:/C:/job1.ffjd --log file:/C:/c.log --test file:/C:/job2.ffjd

The long forms of option names begin with: com.fnfr.open.runtime.executionengine

| --licenseServer | Required. See Checking out a runtime license. |
| --- | --- |
| --duration duration | Time period required for the reservation |
| --fip | Optional. Force Indeterminate result to return a Pass (0) return code. The default return code for an Indeterminate result (due to absence of an analysis rule) is Fail (1). If you specify the -fip option, then an Indeterminate result will instead return a Pass return code (0) |
| --param parameter=value | Optional. Specifies a parameter value for the test to override a parameter value. Repeat the –-param option as often as needed to specify multiple parameter values. Note If you specify both --param and --paramfile in a iTestRT command, then values that you specify using the --param argument take precedence over the values in the parameter file. To use the parameter Type Secret, define it with the --param parameter=secret value iTestRT will not request the secret value at runtime. If you do not define the secret parameter at runtime, the test ase will fail and display a message as follows: ke "Failed: Testcase require secret value %{value} to be passed for proper execution". |
| Note |  |
|  | If you specify both --param and --paramfile in a iTestRT command, then values that you specify using the --param argument take precedence over the values in the parameter file. |
|  | To use the parameter Type Secret, define it with the --param parameter=secret value |
| --paramfile URI | Optional. During execution, use the parameters (and, if included, additional parameter files) specified in the parameter file identified by the URI. iTestRT also supports using query language within parameters, which are resolved to the specified resource property value when running the test case. See Parameter files and Working with parameters: The Parameters page for details of using the iTest user interface for creating a parameter file and also using the Property Query Language syntax. Note Use a single slash character after “file:” in the URI. For example: file:/C:/Workspace/my_project/<folder>/<filename>.<extension> For example: --velocityServer https://<host>/velocity --velocityLogin <login> --velocityPassword <password> --itar <location> --paramfile project://DynamicParameters/DynamicParameters.ffpt --test project://DynamicParameters/DynamicParametersPC.fftc Note If you specify both --param and --paramfile in a iTestRT command, then values that you specify using the --param argument take precedence over the values in the parameter file. |
| Note | Use a single slash character after “file:” in the URI. For example: |
| Note | If you specify both --param and --paramfile in a iTestRT command, then values that you specify using the --param argument take precedence over the values in the parameter file. |
| --reportallsteps | Include all executed steps in test reports (ignore the Include this step and its children in test reports property setting for the step). |
| --test URI | Specifies the URI of the test case or test suite to be executed. Note Use a single slash character after “file:” in the URI. For example: file:/C:/Workspace/my_project/<folder>/<filename>.<extension> Note |
| Note | Use a single slash character after “file:” in the URI. For example: |
| Note |  |
| --test.logfile URI | Optional. Specifies the URI of an output log file that will collect execution information. Note Use a single slash character after “file:” in the URI. For example: file:/C:/Workspace/my_project/<folder>/<filename>.<extension> Note |
| Note | Use a single slash character after “file:” in the URI. For example: |
| Note |  |
| --test.quiet | Optional. Suppress output during execution. |
| --testbed URI | Optional. Specifies the URI of the testbed or topology to use for execution. Note Use a single slash character after “file:” in the URI. For example: file:/C:/Workspace/my_project/<folder>/<filename>.<extension> Note |
| Note | Use a single slash character after “file:” in the URI. For example: |
| Note |  |
| --timeout seconds | Optional. Execution timeout for the test specified by the --test option. |
