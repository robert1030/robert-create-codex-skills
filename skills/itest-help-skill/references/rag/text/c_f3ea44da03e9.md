# Python Automation Library > Configure Listening Mode (Listen for incoming Python connections) > 第2段

- **Agent Mode**：Select to enable Agent Mode
- **Agent Connection Mode**：N/A in listening mode.
- **Listen for incoming Python connections**：This option enables the listening mode for incoming Python connections. iTest GUI will wait for client connections and does not connect to Velocity as an Agent. The Velocity Agent Mode is disabled when Listen for incoming Python connection is selected. iTest either connects to Velocity as an agent or acts as a Session Level Agent server. In Listen for incoming Python connection mode, the agent listens for Python connection (iTest GUI waits for connections) and the Python Automation Library connects to iTest GUI when available.
- **Step capture**：The Step capture option is available only when the Listen for incoming Python connections is selected.
- **Breakpoint at first step**：N/A in listening mode. See Configuring iTest GUI as an Agent (“Debug Velocity Drivers and Executions”).
- **Agent Name:**：Enter a name for the Agent.
- **Port**：Indicates the port used by the Agent during execution.
- **Step timeout (sec)**：N/A in listening mode. See Configuring iTest GUI as an Agent (“Debug Velocity Drivers and Executions”).
- **User feedback timeout (min)**：N/A in listening mode. See Configuring iTest GUI as an Agent (“Debug Velocity Drivers and Executions”).
- **Agent Capabilities and Restrictions**：N/A in listening Mode. See Configuring iTest GUI as an Agent (“Debug Velocity Drivers and Executions”).
- **Apply and Close**：Click to apply settings and connect as Session Level Control Agent and close the window. The Preferences window displays the connection state message depending on whether the Agent is connected or not as follows. When not connected: Agent is listening for incoming Python connection When connected: Agent is connected.
- **Restore Defaults Apply**：Restore default: Click to discard all the changes made and reset to the default values. Apply: Click to apply the changes made.

![](images/python_ALib_agent_preferences.png) <!-- image_ref -->

> **Note：** Note See “Configuring iTest Preferences” for general information on preference settings.
