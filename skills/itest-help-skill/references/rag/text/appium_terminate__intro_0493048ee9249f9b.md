---
{
  "chunk_id": "appium_terminate__intro_0493048ee9249f9b",
  "source_file": "popups/appium_terminate.html",
  "source_original_path": "popups/appium_terminate.html",
  "toc_path": null,
  "heading_path": [
    "appium_terminate.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/appium_action_commands.html"
  ],
  "images": [],
  "content_hash": "0493048ee9249f9b",
  "level": 0
}
---

# appium_terminate.html

Terminates the specified application (currently running) on the device under test. If the specified application is not installed an error displays. If the application is not running then nothing is done.

| Command | None |
| --- | --- |
| Step Properties | Application ID (string, required): Id of an installed application. Response: True if the application was successfully terminated, otherwise false |
| Example | driver.terminate_app{'com.apple.shortcuts'} |

This command uses Terminate App Appium API.

See also the online help topic: Appium action commands.
