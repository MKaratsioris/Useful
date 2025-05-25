# Docker Volume Migration
Make sure you are in the directory `docker migration` with the following structure:
```
.
└── docker migration
    ├── data
    │   ├── grafana_storage_old.tar.gz
    └── grafana-image.tar
```

## 1. Migrate the volume
* Create backup in the old host
    ```bash
    $ docker volume ls
    DRIVER    VOLUME NAME
    local     grafana_storage_old
    $ source_volume=grafana_storage_old
    $ docker run --tty --rm --interactive --volume ${source_volume}:/source --volume ${PWD}/data:/backup  alpine tar czvf /backup/${source_volume}.tar.gz -C /source .
    ```
* Migrate to new host
This should create a new volume `grafana_storage` from the compressed file
    ```bash
    $ target_volume=grafana_storage
    $ restore_archive=grafana_storage_old.tar.gz
    $ docker run --tty --rm --interactive --volume ${target_volume}:/target --volume ${PWD}/data:/backup  alpine tar xzvf /backup/${restore_archive} -C /target
    ```

* Verify:
    ```bash
    $ docker volume ls
    DRIVER    VOLUME NAME
    local     grafana_storage
    $ docker volume inspect grafana_storage
    [
        {
            "CreatedAt": "2024-09-05T18:48:33+02:00",
            "Driver": "local",
            "Labels": null,
            "Mountpoint": "/var/lib/docker/volumes/grafana_storage/_data",
            "Name": "grafana_storage",
            "Options": null,
            "Scope": "local"
        }
    ]
    $ docker system df
    TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
    Images          
    Containers      
    Local Volumes   1         1         20.99MB   0B (0%)
    Build Cache     
    ```

## 2. Migrate the image
This will create an image with the name `grafana/grafana:latest`
```bash
$ docker load -i grafana-image.tar
```
Verify:
```bash
$ docker images
REPOSITORY          TAG       IMAGE ID       CREATED        SIZE
grafana/grafana     latest    c42c21cd0ebc   2 months ago   453MB
```

## 3. Create the container and attach the volume
```bash
$ docker run -it --name grafana-vol -p 3000:3000 -v grafana_storage:/var/lib/grafana grafana/grafana:latest
```
Verify:
* Container is up and running
    ```bash
    $ docker ps
    CONTAINER ID   IMAGE                    COMMAND     CREATED          STATUS         PORTS                                       NAMES
    527591ba0d25   grafana/grafana:latest   "/run.sh"   31 minutes ago   Up 2 seconds   0.0.0.0:3000->3000/tcp, :::3000->3000/tcp   grafana-vol
    ```
* Container has the volume mounted
    ```bash
    $ docker container inspect grafana-vol
    [
        {
            ...
            "Mounts": [
                {
                    "Type": "volume",
                    "Name": "grafana_storage",
                    "Source": "/var/lib/docker/volumes/grafana_storage/_data",
                    "Destination": "/var/lib/grafana",
                    "Driver": "local",
                    "Mode": "z",
                    "RW": true,
                    "Propagation": ""
                }
            ],
            ...
        }
    ]
    $ docker inspect -f '{{ (index .Mounts 0).Source }}' grafana-vol
    /var/lib/docker/volumes/grafana_storage/_data
    ```

* `error: ✗ attempt to write a readonly database`

    This might happen the when you try to create the new container. The solution is:
    ```bash
    chmod 777 /var/lib/grafana
    ```
    If this does not work, try:
    ```bash
    chmod -R a+w /var/lib/grafana
    ```