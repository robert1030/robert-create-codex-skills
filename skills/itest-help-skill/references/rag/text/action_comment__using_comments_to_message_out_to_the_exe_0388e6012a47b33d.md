---
{
  "chunk_id": "action_comment__using_comments_to_message_out_to_the_exe_0388e6012a47b33d",
  "source_file": "topics/action_comment.htm",
  "source_original_path": "topics/action_comment.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Actions for CLI session types",
    "The ‘comment’ action: Add a comment to a test case"
  ],
  "heading_path": [
    "The ‘comment’ action: Add a comment to a test case",
    "The ‘comment’ action: Add a comment to a test case",
    "Using comments to “message out” to the Execution view"
  ],
  "anchor": "1598094",
  "context_ids": [
    "action_comment"
  ],
  "index_keywords": [
    "adding to test cases",
    "comment",
    "comment action"
  ],
  "index_keyword_paths": [
    "actions > comment",
    "comment action",
    "comments > adding to test cases"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "0388e6012a47b33d",
  "level": 2
}
---

# The ‘comment’ action: Add a comment to a test case > The ‘comment’ action: Add a comment to a test case > Using comments to “message out” to the Execution view

On the Test Case editor General page, select Generate an execution issue for every comment step executed. Comment text can include field replacements. This is an easy way to send data to the Execution view.



To enable substitution for a comment step

In the General properties group for the step, check For the Command field, perform command, variable, and backslash substitutions.

To ensure access to certain data that is available when the message is generated, iTest first applies its standard field substitution and then uses Java-style format strings for messages. Java format strings uses escaping rules that differ from Tcl rules.

For example, Java string format uses single quote ' as its special character and you need two of these for escaping. So, to cause ‘ to appear in the message, use two single quotes ‘’ in the message text. For the Java string format rules, see http://java.sun.com/j2se/1.4.2/docs/api/java/text/MessageFormat.html

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
