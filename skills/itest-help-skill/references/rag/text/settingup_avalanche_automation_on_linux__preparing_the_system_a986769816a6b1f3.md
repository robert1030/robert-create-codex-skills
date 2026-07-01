---
{
  "chunk_id": "settingup_avalanche_automation_on_linux__preparing_the_system_a986769816a6b1f3",
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
    "Preparing the system"
  ],
  "anchor": "1316218",
  "context_ids": [
    "settingup_avalanche_automation_on_linux"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/01-AV_Linux_filebrowser.png",
    "topics/images/02-AV_linux_cmd_line.png"
  ],
  "content_hash": "a986769816a6b1f3",
  "level": 2
}
---

# Setting up Avalanche Automation on Linux > Setting up Avalanche Automation on Linux > Preparing the system

1. Install the TCL shell and extract the Avalanche API under the /opt folder.

$ tar -xvzf ActiveTcl8.5.17.0.298612-linux-x86_64-threaded.tar.gz[…..]

$ sudo ./ActiveTcl8.5.17.0.298612-linux-x86_64-threaded/install.sh

[stuff happening, use all default values]

1. 2

1. Extract the API and to /opt/spirent/api folder

$ tar -xvzf Layer_4_7_Auto_Linux_4.46.tar.gz

$ sudo mkdir /opt/spirent/

$ sudo mkdir /opt/spirent/api

$ sudo mv -f Layer_4_7_Auto_Linux_4.46/Layer_4_7_Application_Linux/ /opt/spirent/api/

1. 3

1. Create these directories.

- Create a directory to store licenses of the load generators.

$ sudo mkdir /opt/spirent/licenses

> **Note:** Note Skip this step if you use an appliance other than the C1 or C100-MP.

- Create a directory to store all the tests (this can be anywhere of your liking, I’m putting it under the home of the user).

$ mkdir ~/spirent/

$ mkdir ~/spirent/tests

1. 4

1. Add the directory path to the TCL interpreter in your PATH environment variable:

- Edit file: $ vi ~/.bash_profile

- Append the path to Active TCL 8.5 as follows.

PATH=$PATH:$HOME/bin:/opt/ActiveTcl-8.5/bin

export PATH

- Reload the profile to make sure it works.

$ source ~/.bash_profile

$ echo $PATH

/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/bench/bin:/home/bench/bin:/opt/ActiveTcl-8.5/bin

1. 5

1. Edit the user profile file and add the environment variable (that Avalanche TCL scripts rely on) at the end of the file.

export SPIRENT_TCLAPI_ROOT=/opt/spirent/api/Layer_4_7_Application_Linux/TclAPI

export SPIRENT_TCLAPI_LICENSEROOT=/opt/spirent/licenses

1. 6

1. Install the Java Runtime Environment (JRE) version (for example, 1.6. OpenJDK).

$ sudo yum install java-1.6.0-openjdk.x86_64

1. 7

1. Install the Session Manager daemon. This is a middleware that interfaces the GUI/TCL scripts and the Avalanche backend. Its main function is to ensure backward compatibility of scripts and track the sessions between a front end (TCL, GUI) and the backend.

Create a Shell script as follows to set the required commands.

> **Note:** Note Create an executable script and run this as root or a sudoer.

# cd /opt/spirent/api/Layer_4_7_Application_Linux/service/bin/

# chmod +x ./*

# ./installDaemon.sh

[…]

# ./startDaemon.sh

> **Note:** Note An indication that the script was setup correctly is when you see the daemon listening on port 9194:# netstat -tap | grep 9194 tcp 0 0 *:9194 *:*

![screenshot](topics/images/01-AV_Linux_filebrowser.png) <!-- image_chunk: img_033c6503592be8b8 -->

![screenshot](topics/images/02-AV_linux_cmd_line.png) <!-- image_chunk: img_c6c416834cffa3a2 -->
