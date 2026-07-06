# Spirent TestCenter REST sessions > Spirent TestCenter REST session profiles > Session profile property settings for Spirent TestCenter REST sessions > Spirent TestCenter REST session properties > 第3段

- **STC URL**：(Mandatory): Enter the correct STC Lab server URL (e.g: http://192.168.51.64/stcapi/) or the stcweb app URL. (http://localhost:8888/stcapi).
- **Create or Replace session on connect**：A message displays if the session already exists. If no session is currently running, an error message displays. disconnect setting.
- **Terminate session on disconnect**：If checked, then end the LabServer session when iTest disconnects from LabServer. If unchecked, then do not end the LabServer session. Works in conjunction with the Create new session on connect setting.
- **Session name**：Session name must be unique as it is used to create session name in the STC Lab server. Note If the Session name and Owner ID are not unique, that is, if the session name already exists, the session will fail when iTest tries to create a session. The iTest STC REST session profile maps the Owner ID and Session name to the STC Lab Manager to create a new Test Session as follows.
- **Owner ID**：Owner ID must be unique and is associated with the User Name in STC Lab server. See also the “Note” above.
- **Chassis IP**：Specify the IPv4 address or DNS hostname of the device.
- **Ports**：Specify a single port or list of ports for the session. See To specify a list of port locations. If no Configuration file is specified, then, when the session starts, one port is created for each location in the list. The ports are then connected to and reserved.
- **Configuration file**：Optional: Specify the configuration file (either XML or tcc format file) to use to configure the device when the session starts. The path is limited to 256 characters. You can generate a configuration file using the TestCenter configuration save command. When the session starts:
- **Command Set**：(Mandatory) Select the STC command set to be used from the list. The selected version of iTest STC session commands will be loaded when the session starts or a testcase runs.
- **Force taking port ownership**：Upon connecting, take ownership so no other user can submit commands.
- **Connect to port when session starts**：When selected, the session connects to the port automatically when the session starts.
- **Subscribe to results from configuration file**：When selected, you receive a notification of the results of running the configuration file. See Configuration file above.
- **Verify port status before reserve**：If selected, iTest will check port status before reserving the ports. If the ports are unavailable, an error displays.
