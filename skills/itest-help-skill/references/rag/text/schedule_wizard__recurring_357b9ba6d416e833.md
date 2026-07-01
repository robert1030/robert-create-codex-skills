---
{
  "chunk_id": "schedule_wizard__recurring_357b9ba6d416e833",
  "source_file": "topics/schedule_wizard.htm",
  "source_original_path": "topics/schedule_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "Scheduling Execution",
    "Defining a job (using the Schedule wizard)"
  ],
  "heading_path": [
    "Defining a job (using the Schedule wizard)",
    "Defining a job (using the Schedule wizard)",
    "Recurring"
  ],
  "anchor": "1209826",
  "context_ids": [
    "schedule_wizard"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "357b9ba6d416e833",
  "level": 4
}
---

# Defining a job (using the Schedule wizard) > Defining a job (using the Schedule wizard) > Recurring

Select Recurring to run the job on an hourly basis or once per day every day or on specified days of the week over a specified time period.

To execute a test case multiple times per day, create a job for each execution time.

Specify the following settings:

| Start at | Specify the time of day that the job should start. Click Noon or Midnight to set that time. Tip Click Noon or Midnight and then use the arrows to fine-tune the time. Note U.S. users: The start time will fail for the one hour during which the time changes due to daylight saving time. For example, between 2 AM and 3 AM on 14 March because the time does not exist. | Tip | Click Noon or Midnight and then use the arrows to fine-tune the time. | Note | U.S. users: The start time will fail for the one hour during which the time changes due to daylight saving time. For example, between 2 AM and 3 AM on 14 March because the time does not exist. |
| --- | --- | --- | --- | --- | --- |
| Tip | Click Noon or Midnight and then use the arrows to fine-tune the time. |  |  |  |  |
| Note | U.S. users: The start time will fail for the one hour during which the time changes due to daylight saving time. For example, between 2 AM and 3 AM on 14 March because the time does not exist. |  |  |  |  |
| Repeat Hours:minutes | Check the box to execute on an hourly basis. Uncheck to execute on a daily or less frequent basis. Specify the time between executions. |  |  |  |  |
| Stop after | If you checked Repeat every, then specify the time when execution should stop. Tip Click Noon or Midnight and then use the arrows to fine-tune the time. | Tip | Click Noon or Midnight and then use the arrows to fine-tune the time. |  |  |
| Tip | Click Noon or Midnight and then use the arrows to fine-tune the time. |  |  |  |  |
| Days | Specify the days of the week that the runs should occur. Use the All and None links to check and clear all days. |  |  |  |  |
| End date | Specify the date in the future that scheduled runs of the job should stop. |  |  |  |  |

1. 6

1. If you specified Immediate run, then click Finish. The run will start in a moment.

> **Note:** Note By default, the last page of the wizard enables the job to run as scheduled, so there is no need to continue past this wizard page for an immediate run.

1. 7

1. For jobs with start times other than Immediate: On the Enable Job page, you specify whether the job that you just defined should become an actively scheduled job or should wait to start its scheduled runs until you enable it at some later time.

Check Enable this job to allow the job to run on the schedule that you just configured. This is the default setting.



To modify the schedule for a job

1. Delete the existing job

1. 2

1. Create a new job that specifies the same Test Case/test Suite as the original with the new schedule settings.



To cancel a job (cancel execution)

In the Execution Activity view, right-click the job and select Cancel. The job is removed from the queue.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
