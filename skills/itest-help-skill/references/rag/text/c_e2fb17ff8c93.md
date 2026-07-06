# Session Profiles > Session profiles: Session configuration settings > Reference session profiles

You will use a reference session profile to store the common configuration settings for a class of similar devices. When you base profile B, for example, on reference profile A, then profile B inherits all of its property settings from profile A. You can then make minor changes to profile B and it is ready to use.

For example, all RX5000 routers share most settings but each has a unique IP address. You create a single reference session profile that you can use to start a session with any RX5000. Whenever you need to configure a session connection with any RX5000 device, you can use the reference session profile as the starting point and then modify the IP address and perhaps some other settings and be ready to go.

> **Important：** Important It will save you a lot of time to use a reference session profile as the template when you add a new session profile configuration. You invest the time in maintaining the reference session profile with appropriate settings and (most importantly) the definitions of prompts that the session can return. Then, to add the new profile, you identify the reference profile, make a few minor changes, save it with a new name, and you are ready to go.
