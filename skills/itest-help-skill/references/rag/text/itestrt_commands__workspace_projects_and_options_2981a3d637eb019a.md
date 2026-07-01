---
{
  "chunk_id": "itestrt_commands__workspace_projects_and_options_2981a3d637eb019a",
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
    "Workspace, Projects and options"
  ],
  "anchor": "1258327",
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
    "#1333307",
    "#1255776"
  ],
  "images": [],
  "content_hash": "2981a3d637eb019a",
  "level": 2
}
---

# iTestRT command reference > iTestRT command reference > Workspace, Projects and options

The projects options support itar files that are specified at the command line. In addition, iTestRT --itar command supports executing test cases from iTest workspace when you specify Workspace as the itar path. This also enables execution of all test case commands in iTestRT within the workspace context and query any workspace related information (e.g., info workspacePath). However, it is not recommended to use the [info workspacePath] to determine if iTest is running in headless mode.

The long forms of option names begin with: com.fnfr.open.filesystem.itarproject.itestrtcmdline.

| --itar URI | Specifies the URI of the directory that contains the itar files. (one directory per --itar option) Note Use a single slash character after “file:” in the URI. For example: file:/C:/Workspace/my_project/<folder>/<filename>.<extension> | Note | Use a single slash character after “file:” in the URI. For example: |
| --- | --- | --- | --- |
| Note | Use a single slash character after “file:” in the URI. For example: |  |  |
| --itar command | Specify Workspace folder as itar path, to run any test case contained in the expanded project folder or a packed itar, using the --test option. Example Project Explorer RTWORKSPACE itar_test test_cases CustSessionTC misc_folder ... my_project test_cases testcase.fftc misc_folder ... Example 1: Run test case in folder “my_project” --itar c:\users\user_name\RTWORKSPACE --test project://my_project/test_cases/testcse.fftc --licenseserver itest-lic.mycompany.local Example 2 Run test case in folder “itar_test” --itar c:\users\user_name\RTWORKSPACE --test project://itar_test/test_cases/CustSessionTC.fftc --licenseserver itest-lic.mycompany.local Note If a Workspace contains 2 projects with the same name, a packed itar file and the other expanded project folder, then the test case contained in the expanded project folder will have higher priority for test execution. For example, if iTest workspace called RTWORKSPACE, contains 2 projects, itar_test .itar and itar_test, the expanded project folder, then the test case CustSessionTC.fftc, contained in the itar_test folder will have higher priority for test execution. | Note | If a Workspace contains 2 projects with the same name, a packed itar file and the other expanded project folder, then the test case contained in the expanded project folder will have higher priority for test execution. |
| Note | If a Workspace contains 2 projects with the same name, a packed itar file and the other expanded project folder, then the test case contained in the expanded project folder will have higher priority for test execution. |  |  |
| --paths | Lists the paths that are searched for itar files. |  |  |
| --projects.list | Lists projects that are available |  |  |
| --exportItar | Use --exportItar command to export iTest projects. The example command below shows the workspace to used to create iTAR file using the --itar command exporting it using the --exportItar option. --itar c:\users\user_name\RTWORKSPACE --licenseserver itest-lic.mycompany.local --exportItar An iTar is created for every project in your workspace and resources are also treated as a project. You may execute test case from these iTar files use the command shown below. See also --itar command. --itar c:\users\user_name\RTWORKSPACE --licenseserver itest-lic.mycompany.local --test project://itar_test/test_cases/my_testcase.fftc Note The --exportItar command only exports projects and it does not build or validate iTar files. | Note | The --exportItar command only exports projects and it does not build or validate iTar files. |
| Note | The --exportItar command only exports projects and it does not build or validate iTar files. |  |  |



To run iTestRT certificate validation

Execute iTestRT using the following arguments:

| --licenseServer | Required. See Checking out a runtime license. |
| --- | --- |
| velocityLogin | Log into the server using the specified username. |
| --velocityPassword password | The password for the specified user |
| --velocityServer URI | URL of an Velocity instance, for example, http://somehost:8080 To use a literal IPv6 address in a URL: Disable field replacement (substitution) for the property. As described in RFC-2732 (http://www.ietf.org/rfc/rfc2732.txt), enclose the literal address in [ ] bracket characters. For example, represent 1080:0:0:0:8:800:200C:4171 as http://[1080:0:0:0:8:800:200C:4171]/index.html Note Use a single slash character after “file:” in the URI. For example: file:/C:/Workspace/my_project/<folder>/<filename>.<extension> |
|  | Disable field replacement (substitution) for the property. |
|  | As described in RFC-2732 (http://www.ietf.org/rfc/rfc2732.txt), enclose the literal address in [ ] bracket characters. For example, represent 1080:0:0:0:8:800:200C:4171 as http://[1080:0:0:0:8:800:200C:4171]/index.html |
| Note | Use a single slash character after “file:” in the URI. For example: |
| Certificate Validation: Use velocityDisableSslValidation or velocitySslKeyStore parameter to disable or enable certificate validation. iTestRT opens WebSocket for connection and validates certificate located in Velocity. To connect to Velocity, download ssl.crt file from Velocity Configure page. Then it should be imported to KeyStore used for validation. Default java keystore is used. You may use your custom keystore by using it in the parameter '--velocitySslKeyStore'. You may also disable certificate validation (--velocityDisableSslValidation) If both parameters are absent in the command line, the certificate will be validated by using the default Java trust store or key store. Note To import a certificate to trust store, use the script: import_certificate.bat or import_certificate.sh. | Note |
| Note | To import a certificate to trust store, use the script: import_certificate.bat or import_certificate.sh. |
| --velocitySslKeyStore | The keystore file with an imported certificate. Note You may use keytool to import a certificate into keystore: For example: keytool -import -alias <unique_value> -file <path_to_certificate_file> -storepass <keystore_password> -keystore <path_to_keystore_file>. Password: Enter the password to access to keystore file. //keytool -storepass argument Algorithm: Enter the keystore file algorithm. For example: --velocitySslKeyStore client.jks;changeit;jks |
| Note |  |
|  | Password: Enter the password to access to keystore file. |
|  | Algorithm: Enter the keystore file algorithm. |
| --velocityDisableSslValidation | Use the --velocityDisableSslValidation parameter in the command line, iTestRT will trust any SSL server certificate (No Validation). |

The following table describes how iTestRT validates when some parameters are used in the command line:

| --velocityDisableSslValidation | --velocitySslKeyStore | Result |
| --- | --- | --- |
| No | No | SSL validation by using the default keystore provided in "jre" folder of iTestRT application |
| No | No | SSL validation by using custom keystore provided in velocityDisableSslValidation parameter |
| Yes | No | Error, iTestRT will be stopped. |
