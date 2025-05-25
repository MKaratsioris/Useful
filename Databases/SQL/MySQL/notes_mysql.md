# Setting up MySQL in Ubuntu
## 1. Check if already exists
```bash
dpkg -l | grep -i mysql
```
## 2. Install
```bash
sudo apt install mysql-server
```
## 3. Check status
```bash
sudo systemctl status mysql.service
```
```bash
sudo systemctl start mysql.service
```
## 4. Create user and password
#### - Enter in shell mode
```bash
sudo mysql
```
#### - Create credentials:
    username: root
    password: password
```bash
mysql>ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```
#### - Complete set up
```bash
sudo mysql_secure_installation
```
#### - Login with new credentials
```bash
sudo mysql -u root -p
```
## 5. Install GUI using snap
```bash
sudo snap install mysql-workbench-community
```
## 6. Python library
```bash
python3 -m pip install mysql-connector-python
```
