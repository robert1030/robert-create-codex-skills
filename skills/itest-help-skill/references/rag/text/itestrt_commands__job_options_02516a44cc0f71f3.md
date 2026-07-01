---
{
  "chunk_id": "itestrt_commands__job_options_02516a44cc0f71f3",
  "source_file": "topics/itestrt_commands.htm",
  "source_original_path": "topics/itestrt_commands.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Runtime: iTestRT",
    "iTestRT command reference"
  ],
  "heading_path": [
    "iTestRT command reference",
    "iTestRT command reference",
    "Job options"
  ],
  "anchor": "1238295",
  "context_ids": [
    "itestrt_commands"
  ],
  "index_keywords": [
    "command reference",
    "iTestRT",
    "iTestRT command reference"
  ],
  "index_keyword_paths": [
    "command reference > iTestRT",
    "iTest Runtime > iTestRT command reference",
    "iTestRT > command reference"
  ],
  "related_links": [
    "#1255776"
  ],
  "images": [],
  "content_hash": "02516a44cc0f71f3",
  "level": 2
}
---

# iTestRT command reference > iTestRT command reference > Job options

The job options support scheduled execution by running iTest jobs.

The long forms of option names begin with: com.fnfr.open.runtime.jobexecutor.optionModule

| --licenseServer | Required. See Checking out a runtime license. |
| --- | --- |
| --job URI | Specifies the URI of the job file to run Note Use a single slash character after “file:” in the URI. For example: file:/C:/Workspace/my_project/<folder>/<filename>.<extension> |
| Note | Use a single slash character after “file:” in the URI. For example: |
| --job.logfile URI | Specifies the URI of an output log file that will collect execution information. You must specify the log file before the associated --job URI option. The --job.logfile option applies to all subsequent --job URI options, unless the logfile option is overridden by a logfile option with a new value. That is, if a command includes multiple instances of the of the --job.logfile option for an associated --job URI option, then only the last logfile instance is used. Note Use a single slash character after “file:” in the URI. For example: file:/C:/Workspace/my_project/<folder>/<filename>.<extension> |
| Note | Use a single slash character after “file:” in the URI. For example: |
| --job.quiet | Suppresses output from the job run |
