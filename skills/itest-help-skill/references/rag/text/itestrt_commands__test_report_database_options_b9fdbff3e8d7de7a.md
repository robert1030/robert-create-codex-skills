---
{
  "chunk_id": "itestrt_commands__test_report_database_options_b9fdbff3e8d7de7a",
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
    "Test report database options"
  ],
  "anchor": "1227731",
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
    "test_report_overview.htm#",
    "test_report_setting_preferences.htm#1388990"
  ],
  "images": [],
  "content_hash": "b9fdbff3e8d7de7a",
  "level": 2
}
---

# iTestRT command reference > iTestRT command reference > Test report database options

The Rest report database enable you to set up response compression and save test reports to a specified database (instead of the built-in iTest database). See “Test Reports”, Editors > Test Reports > Database.

Important Database settings that you make using iTestRT remain in use until you change them using iTestRT.

The long forms of option names begin with: com.fnfr.open.runtime.test.trdb

| --catalog name | Name of the database or catalog. |
| --- | --- |
| --configonly | Configure database and ignore test options. |
| --dbtype type | Database type. Allowed values: MySQL, SqlServer, Oracle, Sqlite, Postgresql, Derby, Other. If Other, you must specify a value for the driverclass argument (JDBC connection string and class). |
| --driverclass class | Java class name of the JDBC driver for the database. Used when dbtype is set to Other. |
| --disableResponseCompression | By default responses are compressed in test reports database. Use this option to indicate that the database should not be compressed. |
| --group tagText | Group tag to associate with the report. Note Not used in conjunction with the --comparereports option. |
| Note | Not used in conjunction with the --comparereports option. |
| --host tagText | Host tag to associate with the report. Note Not used in conjunction with the --comparereports option. |
| Note | Not used in conjunction with the --comparereports option. |
| --ipaddr IpAddress | IP address of the database server. |
| --port portNumber | TCP port of the database server. |
| --project tagText | Project tag to associate with the report. Note Not used in conjunction with the --comparereports option. |
| Note | Not used in conjunction with the --comparereports option. |
| --subgroup tagText | Subgroup tag to associate with the report. Note Not used in conjunction with the --comparereports option. |
| Note | Not used in conjunction with the --comparereports option. |
| --tag TagName=tagText | This option enables you to define and assign a value to a custom tag. Example Create a tag that holds the build number so that you compare test execution results between builds. For tests run against build 54321, use: --tag buildNumber=54321 For tests run against build 54322, use: --tag buildNumber=54322 Tip Use a custom tag to identify executions or groups of executions on the Velocity Test Execution page. |
| Tip | Use a custom tag to identify executions or groups of executions on the Velocity Test Execution page. |
| --trdb.password password | Password for logging in to the database server. |
| --trdb.user user | User ID for logging in to the database server. |
| --responseCompressionThreshold <size> | Allows you to make a test report database more compact. (Normally, test case responses occupy a lot of space in a test report database, internal or external). By default, the response compression is disable in iTestRT. Enter an integer value to indicate the size in bytes. Responses with size greater than the specified value (argument) will be compressed in the test reports database. Simple integer value is interpreted as size in bytes. You may also specify size in kilobytes or megabytes Example 100KB or "100 KB" or 5MB or "5 MB" Note The quotation marks usage helps avoid command line parsing error due to spaces. |
| Note | The quotation marks usage helps avoid command line parsing error due to spaces. |
| --uri URI | Connection URI to use to connect to the database. Note Use a single slash character after “file:” in the URI. For example: file:/C:/Workspace/my_project/<folder>/<filename>.<extension> Note |
| Note | Use a single slash character after “file:” in the URI. For example: |
| Note |  |
