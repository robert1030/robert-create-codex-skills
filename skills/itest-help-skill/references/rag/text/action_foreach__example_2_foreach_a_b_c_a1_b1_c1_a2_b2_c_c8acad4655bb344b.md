---
{
  "chunk_id": "action_foreach__example_2_foreach_a_b_c_a1_b1_c1_a2_b2_c_c8acad4655bb344b",
  "source_file": "topics/action_foreach.htm",
  "source_original_path": "topics/action_foreach.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "For and ForEach loops",
    "The foreach action: Execute a group of steps in a loop"
  ],
  "heading_path": [
    "The foreach action: Execute a group of steps in a loop",
    "The foreach action: Execute a group of steps in a loop",
    "How foreach loops work",
    "Example 2: foreach {A B C} {a1 b1 c1 a2 b2 c2 a3 b3 c3 a4 b4 c4}"
  ],
  "anchor": "1518111",
  "context_ids": [
    "action_foreach"
  ],
  "index_keywords": [
    "foreach",
    "foreach loops"
  ],
  "index_keyword_paths": [
    "actions > foreach",
    "foreach loops",
    "loops > foreach"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "c8acad4655bb344b",
  "level": 4
}
---

# The foreach action: Execute a group of steps in a loop > The foreach action: Execute a group of steps in a loop > How foreach loops work > Example 2: foreach {A B C} {a1 b1 c1 a2 b2 c2 a3 b3 c3 a4 b4 c4}

foreach also supports updating multiple variables in the same way as Tcl does. The following steps

foreach { A B C} {a1 b1 c1 a2 b2 c2 a3 b3 c3 a4 b4}

comment "A = $A" "B = $B" "C = $C"

result in four comment steps being executed. Notice that the second list “runs out” in the middle on the last round, so C will be equal to an empty string on the last round.
