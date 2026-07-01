---
{
  "chunk_id": "testcenter_session_rest_editor_concept__spirent_testcenter_rest_session_window_b2b17ad4b9b5caa2",
  "source_file": "topics/testcenter_session_rest_editor_concept.htm",
  "source_original_path": "topics/testcenter_session_rest_editor_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter REST sessions",
    "Spirent TestCenter REST session window",
    "Spirent TestCenter REST session window"
  ],
  "heading_path": [
    "Spirent TestCenter REST session window",
    "Spirent TestCenter REST session window"
  ],
  "anchor": "1210524",
  "context_ids": [
    "testcenter_session_rest_editor_concept"
  ],
  "index_keywords": [
    "REST session window",
    "TestCenter REST"
  ],
  "index_keyword_paths": [
    "TestCenter > REST session window",
    "session windows > TestCenter REST"
  ],
  "related_links": [],
  "images": [
    "topics/images/spirent_testcenter_rest.1.jpg"
  ],
  "content_hash": "b2b17ad4b9b5caa2",
  "level": 1
}
---

# Spirent TestCenter REST session window > Spirent TestCenter REST session window

The session window for Spirent TestCenter sessions in iTest has been designed to closely resemble Spirent TestCenter. As a result, you can capture TestCenter session steps using iTest without having to learn a new interface or new command names. You interact with the iTest session almost exactly like you interact with TestCenter.

iTest integrates with Spirent TestCenter (STC) and provides REST API to ensure that the automation functionality is readily available to a wide variety of clients using both script and GUI. This integration also eliminates the requirement of an STC installation on the client system. This allows you to use existing tools available to create STC automation clients that can run on any platform.

- The iTest REST API session communicates with STC chassis via STC Lab server or the STCWeb RESTful endpoint using the REST API. When using STCWeb RESTful endpoint, you may automate sessions via REST by installing the STC application software on your desktop instead of creating an STC lab server VM.

Important To use the STCWeb application, the Spirent TestCenter application must be installed and running on your local PC/Workstation. See the iTest Installation Guide for instruction on installing and setting up the Spirent TestCenter application on your local PC/Workstation.

- The iTest REST session can run on multiple platform without requiring the STC libraries.

Because all actions and responses are captured, you can use captured items to create test case steps that configure, control, and request statistics from Spirent TestCenter.

- Any action that you perform in the iTest session is forwarded to Spirent TestCenter running on the device. TestCenter performs the action and returns its normal text response. You can view the response in the Results section on the iTest window, just like you do in TestCenter.

- iTest captures all of the actions that you perform in a TestCenter session and all of the responses returned by TestCenter.

![screenshot](topics/images/spirent_testcenter_rest.1.jpg) <!-- image_chunk: img_7893bd9f83939141 -->
