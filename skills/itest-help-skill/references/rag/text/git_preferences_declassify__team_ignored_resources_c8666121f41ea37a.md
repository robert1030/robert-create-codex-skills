---
{
  "chunk_id": "git_preferences_declassify__team_ignored_resources_c8666121f41ea37a",
  "source_file": "topics/git_preferences_declassify.htm",
  "source_original_path": "topics/git_preferences_declassify.htm",
  "toc_path": [
    "iTest Online Help",
    "Using Git in iTest",
    "Setting preferences to Declassify iTest Files as Derived Resources"
  ],
  "heading_path": [
    "Setting preferences to Declassify iTest Files as Derived Resources",
    "Setting preferences to Declassify iTest Files as Derived Resources",
    "Team> Ignored Resources"
  ],
  "anchor": "1479250",
  "context_ids": [
    "git_preferences_declassify"
  ],
  "index_keywords": [
    "Egit",
    "declassify preference settings"
  ],
  "index_keyword_paths": [
    "Egit > declassify preference settings",
    "declassify preference settings > Egit"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "c8666121f41ea37a",
  "level": 2
}
---

# Setting preferences to Declassify iTest Files as Derived Resources > Setting preferences to Declassify iTest Files as Derived Resources > Team> Ignored Resources

Use the Ignored Resources page to specify a list of resource name patterns that should be excluded from version control.

| Ignore patterns | Select the listed patterns and click Apply or Apply and Close for the changes to take affect or click Restore Defaults or Cancel to discard your changes. Note To ensure that iTest files in a project are not classified as derived, the following ignore pattern are selected by default: .project .formmaplib.fffmcat .testcaselib.fftccat .maplib.ffrmcat When pushing iTest content to a Git repository, none of the iTest project files of the pattern selected are added to .gitignore file. | Note |  |  | .project |  | .formmaplib.fffmcat |  | .testcaselib.fftccat |  | .maplib.ffrmcat |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Note |  |  |  |  |  |  |  |  |  |  |  |
|  | .project |  |  |  |  |  |  |  |  |  |  |
|  | .formmaplib.fffmcat |  |  |  |  |  |  |  |  |  |  |
|  | .testcaselib.fftccat |  |  |  |  |  |  |  |  |  |  |
|  | .maplib.ffrmcat |  |  |  |  |  |  |  |  |  |  |
| Add Pattern... | Click Add Pattern... and on the Add Ignore Pattern dialog enter the file name or path pattern that should not be in version control. Enter a name or path pattern (* = any string, ? = any character). Click OK to save pattern or Cancel to discard any changes. |  |  |  |  |  |  |  |  |  |  |
| Remove | Select an Ignore Pattern and click Remove to delete the pattern from the list. |  |  |  |  |  |  |  |  |  |  |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
