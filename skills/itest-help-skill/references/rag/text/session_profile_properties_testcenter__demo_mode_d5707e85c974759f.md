---
{
  "chunk_id": "session_profile_properties_testcenter__demo_mode_d5707e85c974759f",
  "source_file": "topics/session_profile_properties_testcenter.htm",
  "source_original_path": "topics/session_profile_properties_testcenter.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter sessions",
    "Spirent TestCenter session profiles",
    "Session profile property settings for Spirent TestCenter sessions"
  ],
  "heading_path": [
    "Session profile property settings for Spirent TestCenter sessions",
    "Session profile property settings for Spirent TestCenter sessions",
    "Demo Mode"
  ],
  "anchor": "1321864",
  "context_ids": [
    "session_profile_properties_testcenter"
  ],
  "index_keywords": [
    "Spirent TestCenter GUI sessions",
    "session profile property settings"
  ],
  "index_keyword_paths": [
    "Spirent TestCenter GUI > session profile property settings",
    "session profile property settings > Spirent TestCenter GUI sessions"
  ],
  "related_links": [
    "#1317028"
  ],
  "images": [],
  "content_hash": "d5707e85c974759f",
  "level": 2
}
---

# Session profile property settings for Spirent TestCenter sessions > Session profile property settings for Spirent TestCenter sessions > Demo Mode

| Run session in demo mode | If unchecked (default), TestCenter sessions on iTest run normally, sending commands to the device and collecting data. If checked, iTest runs the session against prepared data, enabling you to view results as if it were being returned by a device. The intent is that you can run a session to learn more about how TestCenter sessions operate without having to install or run any Spirent software. Important If you specify demo mode, then you must specify a value for each of the required properties in the Spirent TestCenter group, as described in Spirent TestCenter properties. (Any settings will do — iTest does not use the values. The values are required only to satisfy the iTest validation checks.) Supported statistics Only the following statistics are supported in Demo mode. Trying to demo any other Statistics will result in an exception. AnalyzerPortResults GeneratorPortResults RxPortPairResults TxPortPairResults RxStreamSummaryResults RxStreamBlockResults TxStreamBlockResults TxTrafficGroupResults RxTrafficGroupResults TxStreamResults Default: unchecked | Important |  |
| --- | --- | --- | --- |
| Important |  |  |  |
