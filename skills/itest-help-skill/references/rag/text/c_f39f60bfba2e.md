# Chat Sessions (XMPP chat) > Sending and receiving XMPP chat messages during test execution > Example uses

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- A network protocol test that runs configuration steps, drives traffic across the network, and then pauses execution and sends you a chat message. You then physically connect/disconnect cables and then send a chat message to the test. The test then continues to execute and verifies whether routing is configured correctly.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- After many steps in a complex automated network test case, the test pauses execution and sends you a chat message. While execution is paused, you investigate the state of the network by starting interactive Telnet and/or SSH sessions with particular devices. You then decide which path the rest of the test should use. Based on your findings, you send a chat message that supplies (pre-coded) information to the test case. Based on the information in the message, the test case continue execution down the path you specified.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- A complex test case typically runs smoothly, but in some rare conditions it runs into an error and fails unexpectedly. You add steps that pause execution when the failure occurs and that send you a chat message to notify you of the failure. You can then check the state of the network and the state of test execution. Once you determine what went wrong, you can send a chat message with pre-configured content to either cause execution to continue or terminate.
