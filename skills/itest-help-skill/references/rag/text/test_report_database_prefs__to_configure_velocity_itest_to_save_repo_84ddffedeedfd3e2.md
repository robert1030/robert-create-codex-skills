---
{
  "chunk_id": "test_report_database_prefs__to_configure_velocity_itest_to_save_repo_84ddffedeedfd3e2",
  "source_file": "topics/test_report_database_prefs.htm",
  "source_original_path": "topics/test_report_database_prefs.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Reports",
    "Sharing Test Reports",
    "Configuring Velocity iTest to save test reports to an external database"
  ],
  "heading_path": [
    "Configuring Velocity iTest to save test reports to an external database",
    "Configuring Velocity iTest to save test reports to an external database",
    "To configure Velocity iTest to save reports to the external database"
  ],
  "anchor": "1429310",
  "context_ids": [
    "test_report_database_prefs"
  ],
  "index_keywords": [
    "saving test reports to a database",
    "saving to a database"
  ],
  "index_keyword_paths": [
    "saving test reports to a database",
    "test reports > saving to a database"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "84ddffedeedfd3e2",
  "level": 2
}
---

# Configuring Velocity iTest to save test reports to an external database > Configuring Velocity iTest to save test reports to an external database > To configure Velocity iTest to save reports to the external database

Follow these instructions after your system administrator has configured a database server for use with Velocity iTest.

1. Install Velocity iTest on a client computer.

1. 2

1. Start Velocity iTest and click Window > Preferences.

1. 3

1. On the Preferences page, in the iTest group, navigate to General > Test Reports > Test Report Database.

1. 4

1. Select Use an external database to store test reports and then specify the following settings (the information should be available from your system administrator).

> **Note:** Note By default iTest reports are saved to the embedded database.

You can configure the connection in one of the following ways:

- For any database type other than ‘Other’:

Specify the Database type, hostname or IP address and IP port of the database server, the database/catalog name or SID and, if required, the User ID / Password credentials.

or

- For a database type of Other:

Specify the Java class for the custom JDBC driver, JDBC connection string, and, if required, the User ID / Password credentials.

In any case, you must specify the User ID / Password credentials for the account

| Database type | Specify the type of database server Default: MySQL |
| --- | --- |
| Database server address / Hostname | Specify the hostname or IP address of the database server. Default: localhost |
| Database server port number | Specify the IP port of the database server. If you specify a value for Database type, then you can leave this property blank to use the default port for the specified database type. Default: 5340 |
| Database/Catalog name/SID | Optional. Specify the database/catalog name or SID. To connect to Oracle Database Express Edition, set the SID as xe. Default: reports |
| User ID | Optional. Specify the username used to connect to the database server. |
| Password | Optional. Specify the password for the User ID account. |
| JDBC connection string | Optional. Enter the URL of the JDBC connection. For example, jdbc:mysql://[host][:port]/[database] See the topic on “Adding a custom third-party JDBC driver to iTest” in the iTest Installation Guide. To use a literal IPv6 address in a URL: Disable field replacement (substitution) for the property. As described in RFC-2732 (http://www.ietf.org/rfc/rfc2732.txt), enclose the literal address in [ ] bracket characters. For example, represent 1080:0:0:0:8:800:200C:4171 as http://[1080:0:0:0:8:800:200C:4171]/index.html |
|  | Disable field replacement (substitution) for the property. |
|  | As described in RFC-2732 (http://www.ietf.org/rfc/rfc2732.txt), enclose the literal address in [ ] bracket characters. For example, represent 1080:0:0:0:8:800:200C:4171 as http://[1080:0:0:0:8:800:200C:4171]/index.html |
| Driver class | Optional. Specify the Java class for the custom JDBC driver. For example, com.mysql.jdbc.Driver See the topic on “Adding a custom third-party JDBC driver to iTest” in the Velocity iTest Installation Guide. |

Important Click Test Connection to confirm the settings.

1. 5

1. To save and apply the settings, click OK and then exit and restart Velocity iTest.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
