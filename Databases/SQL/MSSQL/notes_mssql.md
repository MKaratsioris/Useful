# Setting up MSSQL in Ubuntu

## 1. Download the public key, convert from ASCII to GPG format, and write it to the required location:
```bash
sudo apt-get install curl
curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | sudo gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
sudo cp /usr/share/keyrings/microsoft-prod.gpg /etc/apt/trusted.gpg.d/
```
NOTE: If you receive a warning about the public key not being available, you can use the following command instead:
```bash
curl https://packages.microsoft.com/keys/microsoft.asc | sudo tee /etc/apt/trusted.gpg.d/microsoft.asc
```
## 2. Manually download and register the SQL Server Ubuntu repository
```bash
curl -fsSL https://packages.microsoft.com/config/ubuntu/22.04/mssql-server-2022.list | sudo tee /etc/apt/sources.list.d/mssql-server-2022.list
```
## 3. Install SQL Server
```bash
sudo apt-get update
sudo apt-get install -y mssql-server
```

## 4. Configure MSSQL Server
- ACCEPT_EULA:          accept end user licence agreement
- MSSQL_PID:            use the Developer Edition of MSSQL Server (good for non production use cases)
- MSSQL_SA_PASSWORD:    sets up the System Administrator Password
```bash
sudo ACCEPT_EULA='Y' MSSQL_PID='Developer' MSSQL_SA_PASSWORD='mkar1984!' /opt/mssql/bin/mssql-conf setup
```

## 5. Check MSSQL Server status
```bash
systemctl status mssql-server --no-pager
```

## 6. Install extra packages
```bash
curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list | sudo tee /etc/apt/sources.list.d/ms-prod.list
```
```bash
sudo apt-get update
sudo apt-get install -y mssql-tools18 unixodbc-dev
```
NOTE: Allow both licences in the pop-up windows

## 7. Enable the MSSQL Server Agent in this machine
```bash
sudo /opt/mssql/bin/mssql-conf set sqlagent.enabled true
sudo systemctl restart mssql-server
```

## 8. Download Azure Data Studio UI
https://learn.microsoft.com/en-us/azure-data-studio/download-azure-data-studio?tabs=win-install%2Cwin-user-install%2Credhat-install%2Cwindows-uninstall%2Credhat-uninstall

```bash
cd Downloads
sudo dpkg -i azuredatastudio-linux-<VERSION>.deb
```

## 9. Use Azure Data Studio UI
1. Feel the following fields accordingly:
    - Connection type: Microsoft SQL Server
    - Parameters
    - Server: '.' (indicates local instance)
    - Authentication type: SQL Login
    - User name: sa
    - Password: mkar1984!
    - Database: <Default>
    - Encrypt: Mandatory
    - True server certificate: False
    - Server group: <Default>
    - Name(optional): <Default>
2. Connect
3. Enable Trust server certificate

## 10. Use with python
```bash
pip install pyodbc
```


# Extras
## See the space used in different filesystems
```bash
df -kh
```
## RAM usage
```bash
free -g
```