---
{
  "chunk_id": "se_setting_preferences_for_itest_jobs__setting_preferences_for_velocity_itest_j_2d81314a3e625262",
  "source_file": "topics/se_setting_preferences_for_itest_jobs.htm",
  "source_original_path": "topics/se_setting_preferences_for_itest_jobs.htm",
  "toc_path": [
    "iTest Online Help",
    "Scheduling Execution",
    "Setting preferences for Velocity iTest jobs"
  ],
  "heading_path": [
    "Setting preferences for Velocity iTest jobs",
    "Setting preferences for Velocity iTest jobs"
  ],
  "anchor": "1210435",
  "context_ids": [
    "se_setting_preferences_for_itest_jobs"
  ],
  "index_keywords": [
    "iTest jobs",
    "preference settings"
  ],
  "index_keyword_paths": [
    "iTest jobs > preference settings",
    "jobs > preference settings",
    "preference settings > iTest jobs"
  ],
  "related_links": [
    "preferences_itest.htm#"
  ],
  "images": [],
  "content_hash": "2d81314a3e625262",
  "level": 1
}
---

# Setting preferences for Velocity iTest jobs > Setting preferences for Velocity iTest jobs

To view or edit preferences, click Window > Preferences. On the Preferences page, click Spirent > Jobs.

General information on setting and sharing preference settings appears in “Configuring iTest Preferences”

| Open / close session windows during job runs | This setting does not affect test execution. It affects only what you see while test cases are executing. Check the box to make the opening and closing of sessions windows visible while test cases are executing. Uncheck the box to run the job without displaying session windows. Default: unchecked |
| --- | --- |
| Export test reports for test cases executed by jobs | Check the box to cause iTest to export a test report document in HTML format after each test case execution One report is generated for each test case execution Test report files are named with the test case name and a timestamp Optional. You can specify the location to save reports using the Folder for test reports property Optional. You can specify the location of XSL format files using the Location of test report format files property If you uncheck the box, then iTest does not automatically export test report documents. Default: unchecked |
|  | One report is generated for each test case execution |
|  | Test report files are named with the test case name and a timestamp |
|  | Optional. You can specify the location to save reports using the Folder for test reports property |
|  | Optional. You can specify the location of XSL format files using the Location of test report format files property |
| Folder for test reports | Optional. Used only if you check the box for Export test reports. Specify where to save the test report files. You can use any of the listed { } replacements in the URI that you specify. For example: Project://my_project/jobs/{jobfilename}/reports_{date} This text dynamically places the name of the job.ffjd file under my_project/jobs/ and the report subfolder will include the date that the particular job ran. |
| Location of test report format files | Optional. Used only if you check the box for Export test reports. Specify the URI of the folder where the XSL format files (to apply to the test reports) are stored. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
