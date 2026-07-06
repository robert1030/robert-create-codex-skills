# HTTP Sessions > Session profile property settings for HTTP sessions > HTTP > Advanced Properties > 第1段

For a session that cannot determine MIME type and character encoding from POSTs, you can use the following properties to specify the settings. You can also specify HTTP header values.

Note This setting is used to tell the server the MIME type of the data. iTest does not format the data according to the MIME type that you specify. You are responsible to format the data properly.

- **MIME type**：Optional. Specify the MIME type information (for the posted content) to send when POSTing content to a server. This information becomes part of the HTTP Content-Type header field for any POST or GET operation. Here is example content for the field: Content-Type: application/x-www-form-urlencoded; charset=ISO-8859-4 Default: application/x-www-form-urlencoded
- **Charset**：Optional. Specify the character set information (for the posted content) to send when POSTing content to a server. This information becomes part of the HTTP Content-Type header field for any POST or GET operation. Here is example content for the field: Content-Type: application/x-www-form-urlencoded; charset=ISO-8859-4 Default : UTF-8. If UTF-8 is unavailable, then the default for the current locale is used.
- **Header**：Optional. Specify HTTP header values, one per line, using<header>:<spaceCharacter><value> format. The specified values override default values ordinarily supplied by iTest. For example, with each request, iTest specifies the "User-agent" as "User-Agent: Java/1.6.0_13". You might specify a different user agent using: User-agent: User-Agent: Java/1.6.0_14

Large Response

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

Truncate responses above given number of line. Enable execution message upon truncation Enable execution message upon truncation Write response to disk upon truncation (for Command prompt, Bash, SSH, Serial, and Telnet sessions)

Note This option is available only for: Command prompt, Bash, SSH, Serial, and Telnet sessions
