### 1. Update the local package index

```bash
sudo apt update
```
### 2. Install Redis on Ubuntu 22.04

```bash
sudo apt install redis-server -y
```

Before using Redis, you must make a crucial configuration change in the default configuration file. So, access the `redis.conf` configuration file with your preferred text editor:

```bash
sudo nano /etc/redis/redis.conf
```

Scroll down and locate the `supervised` directive. This directive lets you select your preferred init system to manage Redis as a service. By default, this is set to `no`. Since you are running Ubuntu 22.04, which uses systemd to manage running services, set this directive to `systemd`.Save the changes (Ctrl+O) and exit the configuration file (Ctrl+X). Then restart the Redis server for the changes to come into effect.

```bash
sudo systemctl restart redis
sudo systemctl status  redis
redis-server -v
```

### 3. Access Redis CLI ( Command line interface )

With Redis installed on Ubuntu, the next step is to test it and see whether our server works as intended. To achieve this, connect to the server using the `redis-cli` command-line tool.

Upon running the command, your prompt will change to `127.0.0.1:6379`, signifying that you are now working on the Redis shell.

To test connectivity, run the `ping` command. The output `PONG` will be displayed as shown, a confirmation that Redis is functioning as expected.

Moving on, let's try to set a key. In this example, we will set a key called `city`, which will hold `San Francisco` value.

```bash
set city "San Francisco"
```

To retrieve the value of the key, use the `get` command as shown.

```bash
get city
```

source: https://www.cherryservers.com/blog/install-redis-ubuntu





