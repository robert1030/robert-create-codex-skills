---
{
  "chunk_id": "sharing_3__export_to_directory_2239e919e4256309",
  "source_file": "topics/sharing.3.htm",
  "source_original_path": "topics/sharing.3.htm",
  "toc_path": [
    "iTest Online Help",
    "Sharing iTest Resources",
    "Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity"
  ],
  "heading_path": [
    "Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity",
    "Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity",
    "Export to Directory"
  ],
  "anchor": "1244126",
  "context_ids": [],
  "index_keywords": [
    "export projects to Itars",
    "signing artifact"
  ],
  "index_keyword_paths": [
    "export projects to Itars > signing artifact",
    "signing artifacts > export projects to Itars"
  ],
  "related_links": [
    "sharing.4.htm#1094263",
    "#1251004",
    "#1253926",
    "#1253890"
  ],
  "images": [
    "topics/images/exppot_itar_publishIntoDirectory.png"
  ],
  "content_hash": "2239e919e4256309",
  "level": 4
}
---

# Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity > Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity > Export to Directory

In the Export to directory field, specify the folder or browse to the folder to export the iTar files.

For example, this can be a location in your regression system under source control. (For instructions on accessing files that are stored in iTar files, see Accessing iTest files that are held in iTar files.)

You have the following options:

- Save all iTar files to a central location (typically under source control). Any reference to a file using a project:// URI in an instance of iTest or iTestRT will look in this location to find files that are included in an iTar file.

- While browsing to the folder, create a subfolder directly under a shared workspace root directory and name the subdirectory iTar. Any instance of iTest will, by default, look in this location to find files that are included in an iTar file.

- Select Encrypt exported iTars, if required. See Encrypt exported iTars.

- When Export to directory and Encrypt exported iTars are selected, the Next option does not display.

Click Finish. See Click Finish to create iTar files.

- When Export to directory is selected and Encrypt exported iTars is not selected, click Next option is available. Click Next to display the Signing Artifacts page. Go to Signing Artifacts to sign the artifacts and then create iTars.

![screenshot](topics/images/exppot_itar_publishIntoDirectory.png) <!-- image_chunk: img_e470b247dbed501d -->
