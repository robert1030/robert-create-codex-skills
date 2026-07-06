# Debug Velocity Drivers and Executions > Configuring iTest GUI as an Agent > Configure Velocity preferences

Click Spirent > Velocity and configure the Velocity server FQDN and access details.

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

Automatically log me in: Select to ensure that iTest automatically logs you in when the correct server URL and login credentials are provided. Prompt me to login every time: Select to ensure that iTest prompts you to login to Velocity, at startup. Do not auto-login at startup: Select to ensure that iTest does not automatically log into Velocity at startup, even when the correct Velocity URL and login credentials are entered.

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

No validation: When selected iTest performs security validation using the default trust store, that is, the agent trusts any SSL server certificate. Validate certificate through PKIX: When selected, iTest performs security validation using your custom key store

| 欄位1 | 欄位2 |
| --- | --- |
| Server URL | Specify the FDQN of the host where Velocity is running. |
| User name and Password | Optional: Specify the default username and password used to log in when iTest starts. |
| Sync interval (sec) | Velocity periodically checks for changes on the Velocity server (topologies, resources, and reservations) to ensure that the data is always “in sync” with iTest. Specify the time interval between data refreshes. Default: 30 seconds |
| Login mode | Select to indicate the login mode to Velocity when iTest starts: |
| Certificate Validation | Indicates whether security validation algorithm applies to all agent/Velocity interactions using the default trust store or the custom key store. Select the required option: |
| File | Browse and select the custom key store file used for security validation. If the keystore file path is wrong, that is, no valid keystore file exists, iTest disables the Apply button. |
| Password | Enter the password to use the selected custom key store file. |
| Algorithm | Select the security validation algorithm from the dropdown list for the custom key store. |
