# Spirent TestCenter sessions > Spirent TestCenter session profiles > Session profile property settings for Spirent TestCenter sessions > Spirent TestCenter properties > 第2段

- **Chassis IP**：Specify the IPv4 address or DNS hostname of the device.
- **Ports**：Specify a single port or list of ports for the session. See To specify a list of port locations. If no Configuration file is specified, then, when the session starts, one port is created for each location in the list. The ports are then connected to and reserved.
- **Configuration file**：Optional: Specify the configuration file (either XML or tcc format file) to use to configure the device when the session starts. The path is limited to 256 characters. You can generate a configuration file using the TestCenter configuration save command. When the session starts:
- **Force taking port ownership**：Upon connecting, take ownership so no other user can submit commands.
