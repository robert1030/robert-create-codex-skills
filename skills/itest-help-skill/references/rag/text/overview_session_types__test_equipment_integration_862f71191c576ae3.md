---
{
  "chunk_id": "overview_session_types__test_equipment_integration_862f71191c576ae3",
  "source_file": "topics/overview_session_types.htm",
  "source_original_path": "topics/overview_session_types.htm",
  "toc_path": [
    "iTest Online Help",
    "Welcome to iTest",
    "Session types"
  ],
  "heading_path": [
    "Session types",
    "Session types",
    "Built-in Session Types",
    "Test Equipment Integration"
  ],
  "anchor": "1169509",
  "context_ids": [
    "overview_session_types"
  ],
  "index_keywords": [
    "Python",
    "Python sessions",
    "Ranorex",
    "Ranorex test sessions"
  ],
  "index_keyword_paths": [
    "Python sessions",
    "Ranorex test sessions",
    "sessions > Python",
    "sessions > Ranorex"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "862f71191c576ae3",
  "level": 3
}
---

# Session types > Session types > Built-in Session Types > Test Equipment Integration

iTest supports a broad variety of traffic and test equipment by several suppliers.

Each traffic generator session window is an interactive terminal where you enter commands to the device and the device returns text responses. Because all commands and responses are captured, you can use captured items to create test case steps that configure, control, and request statistics from traffic generator devices.

| Ixia IxLoad | To run an IxLoad session in iTest, you first define a test or tests in IxLoad and save the configuration file (RFX file) as you normally would. You then start the IxLoad session in iTest and run the IxLoad test. When the session starts, it checks out the libraries and connects and runs the initialization script and then loads the configuration, validates it, and transforms it (see the description for the iTest load command). The test produces responses and CSV files, which you can then post-process. The IxLoad session window is an interactive terminal where you enter commands to perform IxLoad actions on the device. IxLoad returns text responses. The responses to IxLoad responses are structured and iTest uses built-in mappers to supply read-made queries. |
| --- | --- |
| Ixia IxLoad REST | In IxLoad REST sessions, similar to Tcl-based IxLoad sessions, you can start and stop traffic, start and stop capture, and review statistics. That is command and response are similar in both REST and Tcl-based IxLoad sessions. To run an IxLoad REST session in iTest, you first define a test or tests in IxLoad REST and save the configuration file (RFX file) as you normally would. You then start the IxLoad REST session in iTest and run the IxLoad REST test. When the session starts, it checks out the libraries and connects and runs the initialization script and then loads the configuration, validates it, and transforms it (see the description for the iTest load command). The test produces responses and CSV files, which you can then post-process. The IxLoad REST session window is an interactive terminal where you enter commands to perform IxLoad REST actions on the device. IxLoad REST returns text responses. The responses to IxLoad REST responses are structured and iTest uses built-in mappers to supply read-made queries. |
| IxNetwork | In IxNetwork sessions, you can start and stop traffic, start and stop capture, and review statistics. The levels of the Object Data Matrix are represented as subdirectories (see Table 1-11, API Command Data Model Structure in the IxNetwork Tcl API Guide). The iTest IxNetwork session window enables you to navigate the object hierarchy by using commands that you typically use to navigate a file system. |
| IxNetwork REST | In IxNetwork REST sessions, similar to Tcl-based IxNetwork sessions, you can start and stop traffic, start and stop capture, and review statistics. That is command and response are similar in both REST and Tcl-based IxNetwork sessions. The levels of the Object Data Matrix are represented as subdirectories (see IxNetwork REST API Guide). The iTest IxNetwork REST session window enables you to navigate the object hierarchy by using commands that you typically use to navigate a file system. |
| Ixia N2X | The Ixia N2X session window is an interactive terminal where you enter commands to perform Ixia N2X actions on the device. Ixia N2X returns text responses. Because all commands and responses are captured, you can use captured items to create test case steps that configure, control, and request statistics from Ixia devices. iTest captures both the text response and a structured version of the response. iTest auto-generates appropriate queries for response data, so you can easily work with or analyze data of interest in the response |
| Ixia Traffic | The Ixia Traffic session window is an interactive terminal where you enter commands to perform Ixia Traffic actions on the device. The session on the Ixia device returns text responses. |
| Spirent Avalanche | There are several options for running an Avalanche test in iTest: Running a test using the Tcl scripts generated by Avalanche Running an Avalanche test on a TestCenter device Running a test using Demo mode |
|  | Running a test using the Tcl scripts generated by Avalanche |
|  | Running an Avalanche test on a TestCenter device |
|  | Running a test using Demo mode |
| Spirent Landslide NTAF | You can use iTest to automate Spirent Landslide tests. In iTest, when you start a Landslide session, iTest launches the Landslide TAS user interface running on the Landslide device. 1. Now you can interact with the TAS in the normal way. For example, you might load a test configuration, start the test session, collect the responses, wait to collect several data sets, stop the test session, request the test session results, and then close the test session. 2. When you are finished working on the TAS, you return to iTest and close the Landslide session window. 3. You can now save the captured steps and responses as an iTest test case. As needed, you can modify and update the test case (for example, modify the ImportTestSuite step by causing it to load a different Landslide test suite file or replace the filename with a variable whose value is set at runtime). |
| 1. | Now you can interact with the TAS in the normal way. For example, you might load a test configuration, start the test session, collect the responses, wait to collect several data sets, stop the test session, request the test session results, and then close the test session. |
| 2. | When you are finished working on the TAS, you return to iTest and close the Landslide session window. |
| 3. | You can now save the captured steps and responses as an iTest test case. As needed, you can modify and update the test case (for example, modify the ImportTestSuite step by causing it to load a different Landslide test suite file or replace the filename with a variable whose value is set at runtime). |
| Spirent Landslide REST | iTest integrates with Spirent Landslide and provides REST API to ensure that the automation functionality is readily available to a wide variety of clients using both script and GUI. This integration also eliminates the requirement of a Landslide installation on the client system. This allows you to use existing tools available to create Landslide automation clients that can run on any platform. The iTest REST API session communicates with Landslide TestServer via Landslide Lab server using the REST API ( Landslide Lab is required when working with the session). The iTest REST session can run on multiple platform without requiring the Landslide libraries. Since all actions and responses are captured, you can use captured items to create test case steps that configure, control, and request statistics from Spirent Landslide. Any action that you perform in the iTest Landslide session is forwarded to Spirent Landslide running on the device. Landslide performs the action and returns its normal response. You can view the response in the Results section on the iTest window, just like you do in Landslide. |
|  | The iTest REST API session communicates with Landslide TestServer via Landslide Lab server using the REST API ( Landslide Lab is required when working with the session). |
|  | The iTest REST session can run on multiple platform without requiring the Landslide libraries. |
|  | Since all actions and responses are captured, you can use captured items to create test case steps that configure, control, and request statistics from Spirent Landslide. |
| Spirent SmartBits | The SmartBits session window is an interactive terminal where you enter commands to perform SmartBits actions on the device. SmartBits returns text responses. |
| Spirent TestCenter GUI | This session type appears in iTest only to support old test cases. |
| Spirent TestCenter REST | iTest integrates with Spirent TestCenter (STC) and provides REST API to ensure that the automation functionality is readily available to a wide variety of clients using both script and GUI. This integration also eliminates the requirement of an STC installation on the client system. This allows you to use existing tools available to create STC automation clients that can run on any platform. |
