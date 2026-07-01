---
{
  "chunk_id": "new_job_wizard__configuring_a_job_the_job_wizard_1023a81886350dd5",
  "source_file": "topics/new_job_wizard.htm",
  "source_original_path": "topics/new_job_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "Scheduling Execution",
    "Configuring a job: The Job wizard"
  ],
  "heading_path": [
    "Configuring a job: The Job wizard",
    "Configuring a job: The Job wizard"
  ],
  "anchor": "1137879",
  "context_ids": [
    "new_job_wizard"
  ],
  "index_keywords": [
    "Job wizard",
    "scheduling",
    "scheduling execution"
  ],
  "index_keyword_paths": [
    "Job wizard",
    "execution > scheduling",
    "scheduling execution",
    "wizards > Job wizard"
  ],
  "related_links": [
    "parameters_overview.htm#"
  ],
  "images": [
    "topics/images/scheduling_execution.3.jpg",
    "topics/images/scheduling_execution.4.jpg"
  ],
  "content_hash": "1023a81886350dd5",
  "level": 1
}
---

# Configuring a job: The Job wizard > Configuring a job: The Job wizard

Use the Job wizard to add and modify a job definition.

1. Start the Job wizard using one of the following methods:

- If you know the test case or test suite that the job should run, then right-click it in the Project Explorer or Favorites view and select New Job.

- While working in the Job editor, click New Job .

- Click New and select Other. (Alternatively, click File > New > Other.) The Select a wizard page opens. In the iTest group, select Job and then click Next.

1. 2

1. The Job wizard starts. On the Job page, specify the following properties and then click Next.

| Enter or select the parent folder | Select the project and folder that will hod the new job file. |
| --- | --- |
| File name | Provide a name for the job that you are creating. This is the name that will appear in the Jobs view. |

> **Note:** Advanced users To define a job in the file system outside the current workspace, click Advanced and browse to the location. To specify a path variable that will help Velocity iTest to locate the resource, click Variables and then specify the Name and Location of the path variable.

1. 3

1. On the General page, you configure identifying information for the job and specify the documents to use during execution.

| Headline | Optional. Type a single line of text that describes the job that you are scheduling. This text appears on the Job editor to help you and coworkers when working on the job. |
| --- | --- |
| Description | Optional. Type text that will help coworkers understand the intent and operation of the job. |
| Test case or test suite | Specify a test case or a test suite to execute. All test cases in a test suite will execute. |
| Topology | Optional. Specify a topology file to use during execution. The topology that you specify will be used during execution instead of any topologies that are referenced by the test case or test suite. |
| Parameter file | Optional. Specify a parameter file to use during execution Using a parameter file enables you to supply values that a test case should use at runtime. See “Parameters”. |

1. 4

1. On the Schedule Job page,

![inline_icon](topics/images/scheduling_execution.3.jpg) <!-- image_chunk: img_6fb4327c9fc583ac -->

![screenshot](topics/images/scheduling_execution.4.jpg) <!-- image_chunk: img_258efc7ae9be6578 -->
