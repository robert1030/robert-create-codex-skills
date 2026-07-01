---
{
  "chunk_id": "data_view__how_the_data_view_works_3dbf6dd406002ce6",
  "source_file": "topics/data_view.htm",
  "source_original_path": "topics/data_view.htm",
  "toc_path": [
    "iTest Online Help",
    "Executing Tests",
    "Data view"
  ],
  "heading_path": [
    "Data view",
    "Data view",
    "How the Data view works:"
  ],
  "anchor": "1119239",
  "context_ids": [
    "data_view"
  ],
  "index_keywords": [
    "Data view",
    "setting during execution"
  ],
  "index_keyword_paths": [
    "Data view",
    "parameters > setting during execution",
    "variables > setting during execution",
    "views > Data view"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "3dbf6dd406002ce6",
  "level": 2
}
---

# Data view > Data view > How the Data view works:

During execution, the following actions occur:

- When the test case to be executed is first loaded, the parameters defined in the test case are merged into the execution heap.

- When a foreign test case is loaded (typically on a run step that refers to a test case file that has not yet been loaded), then the parameters from the foreign test case are merged into the execution heap.

- On an open step, the parameters associated with the session profile are integrated into the heap at /parameters/profiles/profile[@session='{session}'] where {session} is the ID of the session about to be opened (after perhaps being overridden because of parameter merging, or because you explicitly changed one of the properties). On a close step, the node is deleted.

- During execution, the Data view shows the heap as it existed before execution was started/resumed. When execution pauses, the contents of the view are updated and editing is enabled. There is no restriction on which elements' values can be edited, however you cannot add new elements or delete existing elements.

In many cases, you may want to keep changes that you have made to the parameters so that the same values will be used in the next execution. For this reason, iTest retains the parameters section of the heap between executions, as long as the same test case is being executed in the same workbench window. See the descriptions for the Reuse parameters between executions and Clear All Data buttons.
