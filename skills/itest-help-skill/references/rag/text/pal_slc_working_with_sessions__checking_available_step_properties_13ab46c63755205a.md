---
{
  "chunk_id": "pal_slc_working_with_sessions__checking_available_step_properties_13ab46c63755205a",
  "source_file": "topics/pal_slc_working_with_sessions.htm",
  "source_original_path": "topics/pal_slc_working_with_sessions.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Session Level Control Library",
    "Working with Sessions"
  ],
  "heading_path": [
    "Working with Sessions",
    "Working with Sessions",
    "Invoking Actions on Session",
    "Checking available step properties"
  ],
  "anchor": "1453553",
  "context_ids": [
    "pal_slc_working_with_sessions"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "13ab46c63755205a",
  "level": 3
}
---

# Working with Sessions > Working with Sessions > Invoking Actions on Session > Checking available step properties

You may query a session for step properties command after the session is opened.

Any of these properties may be passed to the Steps properties. iTest maps the python script to text representation of .fftc files.

> **Note:** Note The following is an example query and the output differs for every iTest session.

# open session, specifying additional session properties

>>> s2.session_properties()

List of session properties: com.fnfr.itest.applications.webservices.restful

"url": "http://spirent.com" # string value

"acceptAllCookies": "false" # boolean value

"autoRedirect": "true" # boolean value

"authentication.authenticationType": "None" enum value one of [None, Basic, Secure]

"authentication.user": "" # string value

"authentication.password": "" # string value

"authentication.keyStoreFile": "" # string value

"authentication.passphrase": "" # string value

"authentication.acceptAllCertificates": "false" # boolean value

#... And other properties.

# query for step properties.

>>> s2.step_properties('GET')

List of session properties: com.fnfr.itest.applications.webservices.restful

"guid": "9284bfbe-9dc5-443c-b4f0-f5af4af87dca" # string value

"action": "GET" # string value

"session": "0555bbba-c858-11e7-8c32-56003d995201" # string value

"context": "" # string value

"target": "" # string value

"async": "false" # boolean value

"isBackgroundThread": "false" # boolean value

"threadName": "" # string value

"skip": "false" # boolean value

"normalOffset": "0s" time-span value

"acceleratedOffset": "0s" time-span value

"estimatedStepExecutionTime": "0s" time-span value

"command.headers": "{}"

"command.contentType": "TEXT" enum value one of [TEXT, XML]

"command.body": "None" # string value

"command.isEncrypted": "false" # boolean value

"documentation.label": "" # string value

"documentation.tag": "" # string value

"documentation.comment": "" # string value

...

...

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
