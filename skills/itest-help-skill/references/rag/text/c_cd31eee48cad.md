# Capturing Manual (Interactive) Sessions > Overview: Creating a test case by capturing interactive sessions > About capturing and defining prompts

We humans know that the text "C:\>" represents a prompt, but how does iTest know that both C:\Temp> and C:> are acceptable prompts? iTest works with prompts in the same way as we humans do: it looks for particular text strings followed by a few milliseconds of idle time on the session channel.

Spirent has predefined some of the most common prompts, however, you might have to define the list of custom prompts for a particular session profile or device. See “Prompts (in CLI sessions)” for instructions.
