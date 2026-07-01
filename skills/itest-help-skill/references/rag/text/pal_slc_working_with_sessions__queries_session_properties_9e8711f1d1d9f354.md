---
{
  "chunk_id": "pal_slc_working_with_sessions__queries_session_properties_9e8711f1d1d9f354",
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
    "Opening a Session",
    "Queries Session properties"
  ],
  "anchor": "1454950",
  "context_ids": [
    "pal_slc_working_with_sessions"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "9e8711f1d1d9f354",
  "level": 3
}
---

# Working with Sessions > Working with Sessions > Opening a Session > Queries Session properties

You may query for Session Properties available after a session is opened.

| # open session, specifying additional session properties s1 = proj.rest_session_ffsp.open(properties={"authentication.authenticationType": "Basic", "authentication.user": "me", "authentication.password": "totes_secret!"}) # Query for session properties s1.session_properties() List of session properties: com.fnfr.itest.applications.webservices.restful "url": "https://jsonplaceholder.typicode.com/" "acceptAllCookies": "false" "autoRedirect": "true" "authentication.authenticationType": "Basic" "authentication.user": "me" "authentication.password": "totes_secret!" "authentication.keyStoreFile": "" "authentication.passphrase": "" "authentication.acceptAllCertificates": "true" "httpHeader": "[]" "urlParameters": "[]" |
| --- |

> **Note:** Note Each individual session has different set of properties available and may be specified during session open.
