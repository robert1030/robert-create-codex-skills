---
{
  "chunk_id": "workspace_working_with__about_workspaces_a73126637a540f48",
  "source_file": "topics/workspace_working_with.htm",
  "source_original_path": "topics/workspace_working_with.htm",
  "toc_path": [
    "iTest Online Help",
    "About the iTest Window",
    "About workspaces"
  ],
  "heading_path": [
    "About workspaces",
    "About workspaces"
  ],
  "anchor": "1131728",
  "context_ids": [
    "workspace_working_with"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/workspace_title_annotated.png"
  ],
  "content_hash": "a73126637a540f48",
  "level": 1
}
---

# About workspaces > About workspaces

Watch a short video to learn nearly everything you need to know to get started on the Spirent Knowledge Base

Your workspace is the folder on your file system that holds the projects in which you'll store all folders and files that you generate using iTest and the settings associated with your iTest environment.

When you first start using iTest, you work in the default workspace — the directory structure on your file system into which all iTest files are saved and from which all iTest files are opened. While working in iTest, you can add, move, rename, and delete folders just as you do in any file system.

A test case will almost always depend on other files – especially topologies, response maps, and session profiles – but potentially other things as well (such as SNMP MIBs, and so on). To ensure that all such files can move around easily from computer to computer, iTest uses URIs rather than hard-coded paths — URIs that are always relative to the resource of interest. Many URIs will be relative to the root of the workspace. The fundamental idea is that when running a test case, if it depends on other files, the files need to be in a workspace (or in an itar file — more on them later).

> **Note:** Note Any preferences that you set apply to the current workspace only.

The path to the current workspace appears in the title of the iTest window:

![screenshot](topics/images/workspace_title_annotated.png) <!-- image_chunk: img_c9902d38ff463914 -->
