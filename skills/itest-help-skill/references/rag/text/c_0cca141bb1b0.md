# Test Reports > Sharing Test Reports > Configuring Velocity iTest to save test reports to an external database > To configure Velocity iTest to save reports to the external database > 第1段

Follow these instructions after your system administrator has configured a database server for use with Velocity iTest.

![*](bullet_blue.jpg) <!-- image_ref -->

1. Install Velocity iTest on a client computer.

1. 2 Start Velocity iTest and click Window > Preferences.

1. 3 On the Preferences page, in the iTest group, navigate to General > Test Reports > Test Report Database.

1. 4 Select Use an external database to store test reports and then specify the following settings (the information should be available from your system administrator).

> **Note：** Note By default iTest reports are saved to the embedded database.

You can configure the connection in one of the following ways:

![*](bullet_blue.jpg) <!-- image_ref -->

- For any database type other than ‘Other’:

Specify the Database type, hostname or IP address and IP port of the database server, the database/catalog name or SID and, if required, the User ID / Password credentials.

or

![*](bullet_blue.jpg) <!-- image_ref -->

- For a database type of Other:

Specify the Java class for the custom JDBC driver, JDBC connection string, and, if required, the User ID / Password credentials.

In any case, you must specify the User ID / Password credentials for the account

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

Disable field replacement (substitution) for the property. As described in RFC-2732 (http://www.ietf.org/rfc/rfc2732.txt), enclose the literal address in [ ] bracket characters. For example, represent 1080:0:0:0:8:800:200C:4171 as http://[1080:0:0:0:8:800:200C:4171]/index.html
