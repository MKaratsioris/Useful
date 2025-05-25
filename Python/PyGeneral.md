General Notes for Python

1. Install Python using the deadsnakes/ppa repository
- See current version
$ python3 -V

- Update and download the necessary packages
$ sudo apt update
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt update

- You can see the repository being added in the following file
$ ls -l /etc/apt/sources.list.d

- Install python version
$ sudo apt install python3.12 -y

- Change priority of versions
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 2
- Verify it worked
$ sudo update-alternatives --config python3
$ python3 -V




2. Install Python using manual downloads (This way will automatically change the default version to the one downloaded)
- Download all the necessary libraries
$ sudo apt -y install gdb lcov libbz2-dev libffi-dev libgdbm-dev libgdbm- compat-dev liblzma-dev libncurses5-dev libreadline6-dev libssl-dev lzma lzma-dev tk-dev uuid-dev zlib1g-dev gcc make pkg-config

- Download the tar file (copy link address: XZ compressed source tarball)
$ wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tar.xz
$ tar -xvf Python-3.12.0.tar.xz
$ cd Python-3.12.0

- Check if you have everything needed to build Python
$ sudo ./configure --enable-optimizations

- Install Python
$ sudo make -j 2

- Compile Python
$ sudo make install




3. Virtual Environments
- Install
$ sudo apt install python3-venv

- Create a new venv
$ sudo python3 -m venv .vevn

- Change the permissions
$ sudo chmod -R a+rwx .venv

- Activate the venv
$ source .venv/bin/activate

- Deactivate the venv
$ deactivate




4. PIP
- Install
$ sudo apt install python3-pip
$ pip --version

- If you get the error: ModuleNotFoundError: No module named 'distutils.util' it is because you are using a version of Python3.12 or later.
$ sudo apt-get install python3.12-distutils
$ pip --version

- Use
$ pip list
$ pip install -r <file-name>.txt




5. Make Packages




6. Make Desktop Apps