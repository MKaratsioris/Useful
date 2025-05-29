# Create automations in Ubuntu OS

- Create the shell script file, for example: `example_automation.sh`
- Make sure your script is executable: `chmod +x /path/to/example_automation.sh`. Make sure to replace /path/to/example_automation.sh with the full path to your script.
- Create a systemd service file: `sudo nano /etc/systemd/system/example_automation.service` and paste inside the file the following:
```bash
[Unit]
Description=<Write you description here...>
After=network-online.target

[Service]
Type=oneshot
ExecStart=/path/to/example_automation.sh
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```
- Enable the service
	- `sudo systemctl daemon-reexec`
	- `sudo systemctl daemon-reload`
	- `sudo systemctl enable example_automation.service`
- If in the future you want to disable it: `sudo systemctl disable example_automation.service`
