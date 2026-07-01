---
{
  "chunk_id": "threaded_execution__overview_synchronizing_threaded_executio_1577e154d447babf",
  "source_file": "topics/threaded_execution.htm",
  "source_original_path": "topics/threaded_execution.htm",
  "toc_path": [
    "iTest Online Help",
    "Making your test case thread-safe",
    "Overview: Synchronizing threaded execution in iTest"
  ],
  "heading_path": [
    "Overview: Synchronizing threaded execution in iTest",
    "Overview: Synchronizing threaded execution in iTest"
  ],
  "anchor": "1530084",
  "context_ids": [
    "threaded_execution"
  ],
  "index_keywords": [
    "asynchronous execution overview",
    "multi-threaded execution overview"
  ],
  "index_keyword_paths": [
    "asynchronous execution overview",
    "multi-threaded execution overview"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "1577e154d447babf",
  "level": 1
}
---

# Overview: Synchronizing threaded execution in iTest > Overview: Synchronizing threaded execution in iTest

:This chapter describes steps for making your test case thread-safe and actions that help you to synchronize execution threads.

iTest supports multi-threaded execution and provides the following types of tools for managing thread synchronization:



lock: Ensure that only one thread at a time can work within a critical set of steps

A lock step specifies a lock name, and all steps that are indented as children of the lock step are locked (often referred to as mutex or semaphore). The named lock is released for use by other lock steps when execution finishes for the currently locked steps. A lock is useful in the following situations:

- When you need to ensure that no steps in a separate section of a test case or procedure alter a variable while a particular set of steps is working with it

- To ensure that all steps in a procedure that opens a session, performs actions in the session, and finally closes the session can execute atomically — that is, with no steps in other threads changing something about the session.



signal: Pause one or more threads until one or more specified signals occur

The signal group of actions enable a variety of options:

- Pause a thread until it is signaled to proceed by a specified event. For example, to encapsulate the procedure that opens a session so that no other steps in the session will proceed until the session is open

- Pause particular threads of execution until other threads notify (signal) them that it is safe to proceed. This capability enables you to encapsulate test cases and to improve the multi-threaded aspects of test cases.

- Pause threads until explicitly signaled. For example, you can begin a test case by initializing several devices and other steps or procedures cannot use the devices until initialization is complete.

- Advanced users can combine synchronization actions to prevent deadlock, starvation, livelock, and other common liveness issues



waitThread: Ensure that execution does not continue until specified threads finish execution

A waitThread step completes only when the last thread finishes (you specify which threads to wait for). Execution then continues with the next step.
