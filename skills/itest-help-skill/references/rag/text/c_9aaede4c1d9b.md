# TL1 Sessions > Configuring sessions and test case steps for TL1 devices > For Hybrid interfaces, follow this procedure:



Configure the testbed device or session profile

You will typically work on an Telnet, Serial, or SSH testbed device or session profile.

1. 1 Set the Style property (Terminal > Style) to TL1.

1. 2 On the Terminal > Replay > Step Defaults > Completion page, set the Completion criteria property to TL1 End of Message.



Configure the test case

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- For steps that do not return TL1-format responses: Change the completion rule to Prompt matches AND device has not sent data during the Idle channel interval (the setting causes iTest to wait for a prompt in the response to the step).

> **Note：** Note If you see that you would change most steps in the test case to Prompt matches AND device has not sent data during the Idle channel interval, you might be better off changing the session profile default to Prompt matches AND device has not sent data during the Idle channel interval and changing the steps that have TL1 message bodies so that their completion rule is TL1 End of Message.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- For steps that have both a TL1 message body and a prompt: Leave the session profile completion rule unchanged (TL1 End of Message). In addition, as long as you have prompts defined in your session profile, iTest will check that the TL1 message is complete and that there is a prompt match.
