# Session Profiles > Defining a session profile (configuring the session settings) > To define a session profile > 第3段

- With substitution: ['\[']::<IPv6>['\]'] Python: eval IPv6="http://[::1]:8080/dashboard/" TCL: eval set IPv6 "http://\[::1\]:8080/dashboard/"

Each session type has different required settings. The property settings associated with each session type are described in the chapter for the particular session type in a section titled “Session profile property settings for <session type> sessions”.

![*](bullet_blue.jpg) <!-- image_ref -->

- Required property settings are marked with the * character.

![*](bullet_blue.jpg) <!-- image_ref -->

- A blue text box indicates that the setting is being inherited from the session profile that the current session profile is based upon. If you are creating a session profile “from scratch”, then the settings are inherited from the iTest default session profile. See Property values: Inheriting settings.

![*](bullet_blue.jpg) <!-- image_ref -->

![](images/session_profiles.4.jpg) <!-- image_ref -->

- The indicates that you can use field replacements in the text of the property setting. See Field replacements: Substituting values into properties and commands.

![*](bullet_blue.jpg) <!-- image_ref -->

By default, iTest auto-validates property values as you set them. The validation process adds a marker to the property setting when there is a problem with a setting. Hold the cursor over the marker to read the details. If, instead, you configure iTest to perform validation only when you request it, then settings are not validated and no markers appear for invalid property settings. See Validation of steps and property settings.

![](images/session_profiles.5.jpg) <!-- image_ref -->

1. 4 You have the option to specify additional session properties like screen color, timeouts, non-standard prompts, and so on. Click to open the Session Properties page. you will find details on property settings for each session type in the appropriate chapter.

1. 5 Optional. Language: Select the language that will be used to create the session profile.

Click the Settings tab. On the Settings page, use the default language displayed (as set in Preferences: Spirent > General > General preference settings, Chapter , “Configuring iTest Preferences”) or select a different language from the list.

When you select Language as Python, you may export the entire iTest test case (FFTC) to a Python script.
