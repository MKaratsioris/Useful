### 1. Installing Toxiproxy in Linux

Check the latest version of Toxiproxy here: https://github.com/Shopify/toxiproxy/releases

```bash
wget -O toxiproxy-2.1.4.deb https://github.com/Shopify/toxiproxy/releases/download/v2.1.4/toxiproxy_2.1.4_amd64.deb
sudo dpkg -i toxiproxy-2.1.4.deb
sudo service toxiproxy start
```

### 2. Populating Toxiproxy with toxiproxy-cli

```bash
toxiproxy-cli create -l localhost:26379 -u localhost:6379 shopify_test_redis_master
```

We recommend a naming such as the above: `<app>_<env>_<data store>_<shard>`. This makes sure there are no clashes between applications using the same Toxiproxy.

Use ports outside the ephemeral port range to avoid random port conflicts. It's 32,768 to 61,000 on Linux by default, see `/proc/sys/net/ipv4/ip_local_port_range`.

### 3. Using Toxiproxy

```bash
toxiproxy-cli toxic add -t latency -a latency=1000 shopify_test_redis_master
```

### 4. Example using Redis server
`redis-cli [26379]  -->  toxiproxy  -->  [6379] redis-server` 
- Run the Toxiproxy server to observe the traffic
    ```bash
    toxiproxy-server
    ```
- Create Proxy
    ```bash
    $ toxiproxy-cli create -l localhost:26379 -u localhost:6379 redis
    Created new proxy redis
    $ toxiproxy-cli list
    Listen          Upstream        Name  Enabled Toxics
    ======================================================================
    127.0.0.1:26379 localhost:6379  redis true    None

    Hint: inspect toxics with `toxiproxy-client inspect <proxyName>`
    ```
- Setup listen port to Redis CLI, and check latency [no latency expected]
    ```bash
    $ redis-cli -p 26379
    127.0.0.1:26379> SET omg pandas
    OK
    127.0.0.1:26379> GET omg
    "pandas"
    ```
- Add latency toxic to proxy
    ```bash
    $ toxiproxy-cli toxic add -t latency -a latency=1000 redis
    Added downstream latency toxic 'latency_downstream' on proxy 'redis'
    ```
- Inspect toxics
    ```bash
    $ toxiproxy-cli inspect redis1
    ```
- Check latency making a request to the Redis server
    ```bash
    $ redis-cli -p 26379
    127.0.0.1:26379> GET omg
    "pandas"
    (1.00s)
    127.0.0.1:26379> DEL omg
    (integer) 1
    (1.00s)
    ```
- Remove toxic
    ```bash
    $ toxiproxy-cli toxic remove -n latency_downstream redis
    Removed toxic 'latency_downstream' on proxy 'redis'
    ```
- Check latency making a request to the Redis server [no latency expected]
    ```bash
    $ redis-cli -p 26379
    127.0.0.1:26379> GET omg
    (nil)
    ```
- Delete proxy
    ```bash
    $ toxiproxy-cli delete redis
    Deleted proxy redis
    ```
- Check connection to Redis server [should fail...]
    ```bash
    $ redis-cli -p 26379
    Could not connect to Redis at 127.0.0.1:26379: Connection refused
    ```

source: https://github.com/Shopify/toxiproxy?tab=readme-ov-file#1-installing-toxiproxy