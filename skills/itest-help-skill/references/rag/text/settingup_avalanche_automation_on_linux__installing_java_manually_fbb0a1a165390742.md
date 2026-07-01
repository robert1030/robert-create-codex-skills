---
{
  "chunk_id": "settingup_avalanche_automation_on_linux__installing_java_manually_fbb0a1a165390742",
  "source_file": "topics/settingup_avalanche_automation_on_linux.htm",
  "source_original_path": "topics/settingup_avalanche_automation_on_linux.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent Avalanche sessions",
    "Setting up Avalanche Automation on Linux"
  ],
  "heading_path": [
    "Setting up Avalanche Automation on Linux",
    "Setting up Avalanche Automation on Linux",
    "Installing Java Manually"
  ],
  "anchor": "1321800",
  "context_ids": [
    "settingup_avalanche_automation_on_linux"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/03-AV_Linux_install_java_manually.png",
    "topics/images/04-AV-Linux_installRPM_set_env.png"
  ],
  "content_hash": "fbb0a1a165390742",
  "level": 2
}
---

# Setting up Avalanche Automation on Linux > Setting up Avalanche Automation on Linux > Installing Java Manually

Go to the following location and download jdk-7u79-linux-i586.rpm

http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html.

1. Install the RPM file.

sudo rpm -ivh filename.rpm

where filename is the name of your rpm file (for example, jdk-7u9-linux-i586.rpm).

Set environment: JAVA_HOME=/usr/java/jdk1.7.0_79

1. 2

1. Append JAVA_HOME to PATH

sudo Alternatives --install /usr/bin/java java /usr/java/jdk1.7.0_79/bin/java 100

Sudo alternatives --config java

1. 3

1. Select java jdk 1.7

1. 4

1. Restart.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/03-AV_Linux_install_java_manually.png) <!-- image_chunk: img_af93d8a3a3e895a0 -->

![screenshot](topics/images/04-AV-Linux_installRPM_set_env.png) <!-- image_chunk: img_d9ee6398a810c686 -->
