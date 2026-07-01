---
{
  "chunk_id": "pal_slc_working_with_projects__importing_opening_projects_4eeca7f7a609f0a1",
  "source_file": "topics/pal_slc_working_with_projects.htm",
  "source_original_path": "topics/pal_slc_working_with_projects.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Session Level Control Library",
    "Working With Projects"
  ],
  "heading_path": [
    "Working With Projects",
    "Working With Projects",
    "Importing/Opening Projects"
  ],
  "anchor": "1447085",
  "context_ids": [
    "pal_slc_working_with_projects"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "4eeca7f7a609f0a1",
  "level": 2
}
---

# Working With Projects > Working With Projects > Importing/Opening Projects

To access session profiles and topologies in a project, the project must first be “imported” or “opened”. Since import is a reserved word in Python, it is called open in the Spirent Python Automation Library. Use the following code to import a project:

proj = slc.open('project1_name')

projs = slc.project1_name.open() # Alternative for the same method.

# multiple projects can be imported if needed

proj2 = slc.open('project2_name')

proj3 = slc.open('project3_name')
