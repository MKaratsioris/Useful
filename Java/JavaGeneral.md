# General Notes for Java

## Install Java Version
1. Download JDK version from Oracle (x64 Debian package): https://www.oracle.com/de/java/technologies/downloads/
2. Go where the .deb file is saved and follow through to install Java
```bash
sudo dpkg -i jdk-########_linux-x64_bin.deb
```
```bash
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-########-oracle-x64/bin/java 3
```
```bash
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-########-oracle-x64/bin/javac 1
```
If you have more versions, check which ones
```bash
sudo update-alternatives --config java
```
5. Check version
```bash
java --version
```
```bash
javac --version
```
6. Set JAVA_HOME system variable
```bash
sudo gedit /etc/environment
```
Press Enter and add the following in line 2: JAVA_HOME="/usr/lib/jvm/jdk-########-oracle-x64/"
Save and close. Finally, reload the system variables
```bash
source /etc/environment
```
Check if everything went as planned
```bash
echo $JAVA_HOME
```
