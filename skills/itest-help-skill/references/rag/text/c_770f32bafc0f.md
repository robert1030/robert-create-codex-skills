# Telnet Sessions > Session profile property settings for Telnet sessions > Telnet > Connect

- **Connect timeout**：Specify how long to wait (in seconds) for the session to start. Default: 30 seconds
- **Retry count**：Specify how often to retry the connection when the connection attempt times out. Default: 1
- **Negotiate Telnet options**：Cause the terminal application to negotiate Telnet options with the host. Default: checked
- **Ignore Telnet options in data stream**：Uncheck the box to parse and implement the bytes in the data stream that encode Telnet options. Check the box to ignore the data. If you check the box and also uncheck the Negotiate Telnet options property, then the Telnet session is a raw socket client. Default: unchecked
