---
{
  "chunk_id": "session_profile_properties_serial__terminal_capture_fdedabec03af965e",
  "source_file": "topics/session_profile_properties_serial.htm",
  "source_original_path": "topics/session_profile_properties_serial.htm",
  "toc_path": [
    "iTest Online Help",
    "Serial Sessions",
    "Session profile property settings for Serial sessions"
  ],
  "heading_path": [
    "Session profile property settings for Serial sessions",
    "Session profile property settings for Serial sessions",
    "Terminal > Capture"
  ],
  "anchor": "1175616",
  "context_ids": [
    "session_profile_properties_serial"
  ],
  "index_keywords": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "Serial property settings",
    "Serial sessions",
    "configuring",
    "session profile property settings"
  ],
  "index_keyword_paths": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "Serial sessions > configuring",
    "Serial sessions > session profile property settings",
    "configuring > Serial sessions",
    "property settings > Serial sessions",
    "session profiles > Serial property settings"
  ],
  "related_links": [],
  "images": [
    "topics/images/serial.2.jpg"
  ],
  "content_hash": "fdedabec03af965e",
  "level": 2
}
---

# Session profile property settings for Serial sessions > Session profile property settings for Serial sessions > Terminal > Capture

| Perform capture cleanup | When you perform manual testing in CLI sessions, you frequently use meta-characters like backspace and up- and down-arrows to correct your typing. In a Capture report, such commands can be difficult to read and understand. If you check Perform capture cleanup, then iTest “cleans up” any keyboard shortcuts and removes meta-characters from the captured commands so that the resulting command text appears as if you typed it fully and correctly. See the Discard command completion steps property. Default: Checked A tab completion example appears after this table. iTest captured the show ip traffic command correctly, even though we actually typed show ip tr<tab>. iTest discarded the intermediate show ip tr<tab> form of the command. |
| --- | --- |
| Mask unechoed commands | Check Mask unechoed commands so that, before creating a Capture report, iTest masks all Command property text for which no echo was returned. Check the box to automatically mask passwords. Default: Checked |
| Remove echo from response | Check Remove echo from response to indicate that the device echoes characters typed at the command line. In this case, iTest ignores echoed characters so that the command text is not added to the actual response text. Default: Checked |
| Remove prompt from response | Check Remove prompt from response to save only the response from the session and not the prompt text. We recommend that you do not disable this setting except in rare circumstances. Default: Checked |
| Use prompts from the session for cleanup | Check the box to use the prompt definitions specified in the session profile document when cleaning up commands. Default: Checked |
| Discard command completion steps | To ensure that captured commands in the Capture view are easy to understand, iTest, by default, deletes the intermediate command completion text that was submitted while forming a command. A tab completion example appears after this table. iTest captured the show ip traffic command correctly, and discarded the intermediate show ip tr<tab> form of the command. See the Perform capture cleanup property. Default: Checked |
| Learn prompts | If the box is checked, then, when you close a session and iTest has detected a new prompt, the Update Session Profile wizard starts. You can specify particular prompts in the Terminal > Prompts properties. Default: Checked |
| Learn command completion characters | Learn the character code that the device interprets as command completion characters (that is, characters that cause the command interpreter to echo as much of the complete command text as it can). If the box is checked, then, when you close a session and iTest has detected a new command completion character, t the Update Session Profile wizard starts. The default completion character is tab. To specify particular characters, configure the Terminal > Capture > Command Completion property. Default: Checked |
| Learn break characters | Learn the character code that the device interprets as a break (so you can manually cancel an executing step). The learned break characters are added to the Command break characters property. If the box is checked, then, when you close a session and iTest has detected a new break character, the Update Session Profile wizard starts. Default: Checked. The default break character is Ctrl-C. Note To specify particular break characters manually, configure the Command break characters property (in Terminal > Capture > Break). |
| Note | To specify particular break characters manually, configure the Command break characters property (in Terminal > Capture > Break). |
| Remove line containing more prompt | Check the box so that, when capturing responses, iTest deletes the lines that include the more prompt. Default: Checked |

![screenshot](topics/images/serial.2.jpg) <!-- image_chunk: img_60ddb81e8130eb37 -->
