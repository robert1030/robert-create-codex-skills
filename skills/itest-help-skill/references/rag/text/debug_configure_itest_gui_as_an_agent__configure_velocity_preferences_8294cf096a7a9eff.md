---
{
  "chunk_id": "debug_configure_itest_gui_as_an_agent__configure_velocity_preferences_8294cf096a7a9eff",
  "source_file": "topics/debug_configure_itest_gui_as_an_agent.htm",
  "source_original_path": "topics/debug_configure_itest_gui_as_an_agent.htm",
  "toc_path": [
    "iTest Online Help",
    "Debug Velocity Drivers and Executions",
    "Configuring iTest GUI as an Agent"
  ],
  "heading_path": [
    "Configuring iTest GUI as an Agent",
    "Configuring iTest GUI as an Agent",
    "Configure Velocity preferences"
  ],
  "anchor": "1447450",
  "context_ids": [
    "debug_configure_itest_gui_as_an_agent"
  ],
  "index_keywords": [
    "Agent",
    "preference settings"
  ],
  "index_keyword_paths": [
    "Agent > preference settings",
    "preference settings > Agent"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "8294cf096a7a9eff",
  "level": 2
}
---

# Configuring iTest GUI as an Agent > Configuring iTest GUI as an Agent > Configure Velocity preferences

Click Spirent > Velocity and configure the Velocity server FQDN and access details.

| Server URL | Specify the FDQN of the host where Velocity is running. |
| --- | --- |
| User name and Password | Optional: Specify the default username and password used to log in when iTest starts. |
| Sync interval (sec) | Velocity periodically checks for changes on the Velocity server (topologies, resources, and reservations) to ensure that the data is always “in sync” with iTest. Specify the time interval between data refreshes. Default: 30 seconds |
| Login mode | Select to indicate the login mode to Velocity when iTest starts: Automatically log me in: Select to ensure that iTest automatically logs you in when the correct server URL and login credentials are provided. Prompt me to login every time: Select to ensure that iTest prompts you to login to Velocity, at startup. Do not auto-login at startup: Select to ensure that iTest does not automatically log into Velocity at startup, even when the correct Velocity URL and login credentials are entered. |
|  | Automatically log me in: Select to ensure that iTest automatically logs you in when the correct server URL and login credentials are provided. |
|  | Prompt me to login every time: Select to ensure that iTest prompts you to login to Velocity, at startup. |
|  | Do not auto-login at startup: Select to ensure that iTest does not automatically log into Velocity at startup, even when the correct Velocity URL and login credentials are entered. |
| Certificate Validation | Indicates whether security validation algorithm applies to all agent/Velocity interactions using the default trust store or the custom key store. Select the required option: No validation: When selected iTest performs security validation using the default trust store, that is, the agent trusts any SSL server certificate. Validate certificate through PKIX: When selected, iTest performs security validation using your custom key store |
|  | No validation: When selected iTest performs security validation using the default trust store, that is, the agent trusts any SSL server certificate. |
|  | Validate certificate through PKIX: When selected, iTest performs security validation using your custom key store |
| File | Browse and select the custom key store file used for security validation. If the keystore file path is wrong, that is, no valid keystore file exists, iTest disables the Apply button. |
| Password | Enter the password to use the selected custom key store file. |
| Algorithm | Select the security validation algorithm from the dropdown list for the custom key store. |
