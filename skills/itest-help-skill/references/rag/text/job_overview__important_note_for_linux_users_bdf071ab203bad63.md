---
{
  "chunk_id": "job_overview__important_note_for_linux_users_bdf071ab203bad63",
  "source_file": "topics/job_overview.htm",
  "source_original_path": "topics/job_overview.htm",
  "toc_path": [
    "iTest Online Help",
    "Scheduling Execution",
    "Overview: Scheduling execution using Jobs"
  ],
  "heading_path": [
    "Overview: Scheduling execution using Jobs",
    "Overview: Scheduling execution using Jobs",
    "Important note for Linux users"
  ],
  "anchor": "1192619",
  "context_ids": [
    "job_overview"
  ],
  "index_keywords": [
    "iTestRT",
    "jobs",
    "scheduled execution",
    "scheduling",
    "scheduling execution",
    "time zone",
    "time zones"
  ],
  "index_keyword_paths": [
    "execution > scheduling",
    "execution > time zone",
    "iTestRT > scheduling execution",
    "jobs > scheduling",
    "jobs > time zones",
    "runs > scheduling",
    "scheduling execution",
    "scheduling execution > iTestRT",
    "time zone > jobs",
    "time zone > scheduled execution"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "bdf071ab203bad63",
  "level": 2
}
---

# Overview: Scheduling execution using Jobs > Overview: Scheduling execution using Jobs > Important note for Linux users

On some Linux systems, Java applications may not pick up the correct time zone. You might experience the problem as scheduled jobs executing at incorrect times. To eliminate the problem, set the following environment variable before you start Velocity iTest:

export TZ=`cat /etc/timezone`
