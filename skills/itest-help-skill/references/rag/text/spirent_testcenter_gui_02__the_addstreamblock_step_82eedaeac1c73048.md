---
{
  "chunk_id": "spirent_testcenter_gui_02__the_addstreamblock_step_82eedaeac1c73048",
  "source_file": "topics/spirent_testcenter_gui.02.htm",
  "source_original_path": "topics/spirent_testcenter_gui.02.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter sessions",
    "Spirent TestCenter session window",
    "To create a test case that includes Spirent TestCenter sessions"
  ],
  "heading_path": [
    "To create a test case that includes Spirent TestCenter sessions",
    "To create a test case that includes Spirent TestCenter sessions",
    "The addStreamBlock step"
  ],
  "anchor": "1238653",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/spirent_testcenter_gui.15.jpg",
    "topics/images/spirent_testcenter_gui.18.jpg",
    "topics/images/STC_configurePort_IEEE80211_properties06-20-19.png"
  ],
  "content_hash": "82eedaeac1c73048",
  "level": 4
}
---

# To create a test case that includes Spirent TestCenter sessions > To create a test case that includes Spirent TestCenter sessions > The addStreamBlock step

iTest generated this addStreamBlock step because it captured an addStreamBlock action when you clicked and clicked OK in the StreamBlock Editor. Notice that the Description field for the step specifies the port (1) to add the stream block to.

> **Note:** Note Remember that the device’s response to this command is auto-mapped, so, you could add an analysis rule for the step to have the automated test verify the settings or extract a value from the response.

We captured a few steps after the addStreamBlock step. Let’s look at the other steps in the test case. We can see that the test case will:

Step 3: Start capture on port 2 (we selected Traffic Generator Port 2 and then clicked )

Step 4: Start the generator on port 1 (we selected Traffic Generator Port 1 and then clicked )

Step 5: Stop the generator on port 1

Step 6: Stop capture on port 2

Step 7: Get the RxPortPairResults data for port 2 (in the Statistics portion of the tree for port 2, we selected RxPortPairResults and then clicked . iTest captured the action and returned the data. You could, for example, add an analysis rule here to verify the data that was returned.)

Step 8: Clear the RxPortPairResults statistics for port 2

Step 9: Get the RxPortPairResults statistics for port 2 again (this step exists so you can add analysis rules to verify that step 8 indeed cleared the starts).

Example 2a: The steps in the test case and the properties of the example step.

![unknown](topics/images/spirent_testcenter_gui.15.jpg) <!-- image_chunk: img_a8a5971fd059427d -->

![unknown](topics/images/spirent_testcenter_gui.18.jpg) <!-- image_chunk: img_caa02f87565131eb -->

![screenshot](topics/images/STC_configurePort_IEEE80211_properties06-20-19.png) <!-- image_chunk: img_06b7dea3966f6cf5 -->
