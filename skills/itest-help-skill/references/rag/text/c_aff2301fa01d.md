# Spirent TestCenter REST sessions > Spirent TestCenter REST session profiles > Session profile property settings for Spirent TestCenter REST sessions > Spirent TestCenter REST session properties > 第1段

![](images/stc_rest_itestSession.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

When checked: Creates a new session on STC lab server and replaces an existing session, if any.

![*](bullet_black_small.png) <!-- image_ref -->

when unchecked: Use the currently running LabServer session for the iTest STC REST session

Note Works in conjunction with the Terminate session on

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

Owner ID is mapped to the User Name in STC Lab Manager Session name is mapped to the Test Map in STC Lab Manager

Note If you do not specify a Chassis IP value, then you can use //chassis/slot/port notation in the Ports property to refer to ports on multiple chassis.

Note iTest assigns ports in the listed order. For example, "1:9,1:8" assigns Port 9 first and "1:8,1:9" assigns port 8 first. If you are loading a configuration file and port order is important, you must specify ports in the same order as in the configuration file. Note In addition to supporting 10G, 40G, and 100G traffic and port settings, iTest supports you to view and configure 10G, 40G, 100G port settings in TestCenter.console. iTest also supports viewing and displaying of IEEE802.11 port type.

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->
