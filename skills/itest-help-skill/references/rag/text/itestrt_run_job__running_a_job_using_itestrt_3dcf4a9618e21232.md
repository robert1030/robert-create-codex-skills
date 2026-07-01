---
{
  "chunk_id": "itestrt_run_job__running_a_job_using_itestrt_3dcf4a9618e21232",
  "source_file": "topics/itestrt_run_job.htm",
  "source_original_path": "topics/itestrt_run_job.htm",
  "toc_path": [
    "iTest Online Help",
    "Scheduling Execution",
    "Running a job using iTestRT"
  ],
  "heading_path": [
    "Running a job using iTestRT",
    "Running a job using iTestRT"
  ],
  "anchor": "1145220",
  "context_ids": [
    "itestrt_run_job"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "itestrt_commands.htm#1133277",
    "itestrt.htm#1147665"
  ],
  "images": [],
  "content_hash": "3dcf4a9618e21232",
  "level": 1
}
---

# Running a job using iTestRT > Running a job using iTestRT

To run a job from the command line, you enter a command of the following form:

itestrt --job [jobUri]

> **Note:** Note The full iTestRT command set appears in iTestRT command reference.

- iTestRT starts and writes the following information to the console:

- If the job is running, iTestRT displays Running job: <jobFilename> and the sort of information shown in Example iTestRT output.

- If iTestRT is waiting for a job to start, it displays Waiting for job and a list of scheduled jobs (five maximum) with the next start time and time limit. STDOUT is then silent until the next job starts running.

- While iTestRT runs a job, it sends output from the job to STDOUT.

- When the run completes, then iTestRT displays the scheduling (if any) of the next run.

- iTestRT continues running until the specified job has no more work pending. For recurring jobs, this means that iTestRT will run indefinitely.

- To kill iTestRT at any time, press Ctrl-C.

> **Tip:** Tip Use the iTestRT reporting plug‑ins to publish reports in various ways.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
