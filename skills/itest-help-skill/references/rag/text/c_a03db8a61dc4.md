# Spirent Avalanche sessions > Setting up Avalanche Automation on Linux > Installing Java Manually

Go to the following location and download jdk-7u79-linux-i586.rpm

http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html.

![](images/03-AV_Linux_install_java_manually.png) <!-- image_ref -->

![*](bullet_blue.jpg) <!-- image_ref -->

1. Install the RPM file.

```
sudo rpm -ivh filename.rpm
```

where filename is the name of your rpm file (for example, jdk-7u9-linux-i586.rpm).

```
Set environment: JAVA_HOME=/usr/java/jdk1.7.0_79
```

1. 2 Append JAVA_HOME to PATH

```
sudo Alternatives --install /usr/bin/java java /usr/java/jdk1.7.0_79/bin/java 100
```

```
Sudo alternatives --config java
```

![](images/04-AV-Linux_installRPM_set_env.png) <!-- image_ref -->

1. 3 Select java jdk 1.7

1. 4 Restart.
