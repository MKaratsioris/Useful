General Notes for Ubuntu
- Remove directory
$ sudo rm -r -f <path-to-dir>

1. Cannot open Settings
$ sudo apt install gnome-control-center


2. Cannot open Terminal
- This happens when installing different Python versions. At the moment, the terminal can only open from the 'Home' folder (for some reason :D), by right click and selecting 'Open in Terminal'. To find all the versions of Python
$ ls /usr/bin/python*
- Then you need to specify the version used when trying to open the terminal
$ sudo gedit /usr/bin/gnome-terminal
- In the first line write: #!/usr/bin/python3.<try-different-versions>. For example, in Ubuntu 22.04 TLS, it is: #!/usr/bin/python3.10

NOTE: (source) https://www.youtube.com/watch?v=djYfAgeVMnY


3. Check Release
$ cat /etc/lsb-release


4. Create custom commands
- Create the .c file, i.e. mycommand.c
- Compile the .c file and create the executable
$ gcc -o <executable-name> mycommand.c
- Check that it works
$ /home/mkar/Desktop/Ubuntu/<executable-name>
- Create solf link to /bin, to be able to execute the command globaly
$ sudo ln -s /home/mkar/Desktop/Ubuntu/<executable-name> /bin


5. Find out the commands you typed
$ history

6. Install packages
- Install
$ sudo dpkg -i package_name.deb
- Remove
$ sudo dpkg -r package_name
- Check if it is installed
$ sudo dpkg -S package_name