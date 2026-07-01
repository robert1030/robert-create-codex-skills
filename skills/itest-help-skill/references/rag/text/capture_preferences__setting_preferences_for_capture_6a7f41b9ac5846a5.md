---
{
  "chunk_id": "capture_preferences__setting_preferences_for_capture_6a7f41b9ac5846a5",
  "source_file": "topics/capture_preferences.htm",
  "source_original_path": "topics/capture_preferences.htm",
  "toc_path": [
    "iTest Online Help",
    "Capturing Manual (Interactive) Sessions",
    "Capture reports",
    "Setting preferences for capture"
  ],
  "heading_path": [
    "Setting preferences for capture",
    "Setting preferences for capture"
  ],
  "anchor": "1194840",
  "context_ids": [
    "capture_preferences"
  ],
  "index_keywords": [
    "capture",
    "preference settings"
  ],
  "index_keyword_paths": [
    "capture > preference settings",
    "preference settings > capture"
  ],
  "related_links": [
    "preferences_itest.htm#"
  ],
  "images": [],
  "content_hash": "6a7f41b9ac5846a5",
  "level": 1
}
---

# Setting preferences for capture > Setting preferences for capture

To view or edit preferences, click Window > Preferences. On the Preferences page, click Spirent > General > Capture.

> **Note:** Note The disk space and cache settings will take effect after you restart.

General information on setting and sharing preference settings appears in “Configuring iTest Preferences”.

Spirent > General > Capture

| Maximum disk space to allocate for storing captured sessions | The Capture process holds a large number of captured items, up to a specified limit. When the data exceeds the limit, iTest deletes a certain number of the oldest captured items to make room for new captured items. The default setting allows for most users' needs. Default: 1000 |
| --- | --- |
| Maximum number of captured steps cached in memory | The Capture process holds information on captured steps in memory, up to a specified limit. When the step count exceeds the limit, iTest deletes the oldest captured step to make room for a new captured step. The default setting allows for most users' needs. Default: 1000 |
| Suppress capture of sessions started via execution | Select one of these three options. Note Your selections will take effect when you click Apply (there is no need to restart iTest). Suppress: The selection ensures that Capture function is not performed during execution, including the manual steps when paused. |
| Suppress, if you perform steps interactively while execution is paused then capture: Capture view is populated with all steps you perform (manually) in interactive sessions. That is, no steps will be captured for session during execution, until at least one manual step is performed in the session: Captures nothing when no manual steps are performed Captures all/any manual steps performed in the session The session is also captured when you perform steps interactively while execution is paused. |  |
|  | Captures nothing when no manual steps are performed |
|  | Captures all/any manual steps performed in the session |
| Do not suppress: Capture all steps during execution, including the manual steps when paused. Captures all steps — whether performed by you in an interactive session or auto-executed by iTest — are captured and displayed in a session in the Capture view. |  |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
