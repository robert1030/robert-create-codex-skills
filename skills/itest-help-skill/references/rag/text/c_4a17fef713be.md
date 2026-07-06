# File sessions > Session profile property settings for File sessions > Note write mode is not supported for zip, jar, tar, tgz, or tbz2 file types. write mode is not supported when the URI uses HTTP, HTTPS, or SFTP. File > Authentication > 第1段

- **Username**：Optional. Specify the username used to connect to access the file.
- **Password**：Optional. Specify the password. The text is masked here and in all locations where it is used.
- **Key**：
- **Passphrase**：

File > Large Response

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

Truncate responses above given number of line. Enable execution message upon truncation Enable execution message upon truncation Write response to disk upon truncation (for Command prompt, Bash, SSH, Serial, and Telnet sessions)

Note This option is available only for: Command prompt, Bash, SSH, Serial, and Telnet sessions

- **Enable large response truncation**：Select these options to manage large session responses. When not selected, all the options below are not available for selection When selected, after executing a test, the Execution view a warning message displays, for example: The response is truncated. See itest-response_YYYYMMDD-HHMMSS(t1)(step-2) in tmp dir. 2 2 main t1 terminal new_testcase.fftc
- **Truncate response above the given number of lines**：Enter the number of lines to truncate. For example, 10. When you execute a test with this option, you may verify the response in the Response view, which displays 10 lines of response along with the message (for example): ### Response has been truncated. See itest-response_YYYYMMDD-HHMMSS(t1)(step-2) in tmp dir ###
- **Enable execution message upon truncation**：Select to view/verify the message in Execution
- **Write response to disk upon truncation**：Select to save response to disk. When this option is not selected and you execute a test, you may notice that no response file is generated. That is, no files of the format (in the %temp% folder) after execution of commands: itest-response_YYYYMMDD-HHMMSS(session-profile)XXXXXXXXXXXXXXXX.txt

Terminal
