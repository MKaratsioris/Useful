# Docker

## Running Containers

| COMMAND | DESCRIPTION |
| --- | --- |
| `docker run <image>` | Start a new container from an image |
| `docker run -it <image>` | Start a new container in interactive mode |
| `docker run --rm <image>` | Start a new container and remove it when it exits |
| `docker create <image>` | Create a new container |
| `docker start <container>` | Start a container |
| `docker stop <container>` | Graceful stop a container |
| `docker kill <container>` | Kill (SIGKILL) a container |
| `docker restart <container>` | Graceful stop and restart a container |
| `docker pause <container>` | Suspend a container |
| `docker unpause <container>` | Resume a container |
| `docker rm <container>` | Destroy a container |

## Container Bulk Management

| COMMAND | DESCRIPTION |
| --- | --- |
| `docker stop $(docker ps -q)` | To stop all the running containers |
| `docker stop $(docker ps -a -q)` | To stop all the stopped and running containers |
| `docker kill $(docker ps -q)` | To kill all the running containers |
| `docker kill $(docker ps -a -q)` | To kill all the stopped and running containers |
| `docker restart $(docker ps  -q)` | To restart all  running containers |
| `docker restart $(docker ps -a -q)` | To restart all the stopped and running containers |
| `docker rm $(docker ps  -q)` | To destroy all running containers |
| `docker rm $(docker ps -a -q)` | To destroy all the stopped and running containers |
| `docker pause $(docker ps  -q)` | To pause all  running containers |
| `docker pause $(docker ps -a -q)` | To pause all the stopped and running containers |
| `docker start $(docker ps  -q)` | To start all  running containers |
| `docker start $(docker ps -a -q)` | To start all the stopped and running containers |
| `docker rm -vf $(docker ps -a -q)` | To delete all containers including its volumes use |
| `docker rmi -f $(docker images -a -q)` | To delete all the images |
| `docker system prune` | To delete all dangling and unused images, containers, cache and volumes |
| `docker system prune -a` | To delete all used and unused images |
| `docker system prune --volumes` | To delete all docker volumes |

## Inspect Containers

| COMMAND | DESCRIPTION |
| --- | --- |
| `docker ps` | List running containers |
| `docker ps --all` | List all containers, including stopped |
| `docker logs <container>` | Show a container output |
| `docker logs -f <container>` | Follow a container output |
| `docker top <container>` | List the processes running in a container |
| `docker diff` | Show the differences with the image (modified files) |
| `docker inspect` | Show information of a container (json formatted) |
| `docker export chronocraft-backend-1 \| tar -tvf - \| grep '\.venv/bin/'` | Inspect Inside stopped container |

## Executing Commands

| COMMAND | DESCRIPTION |
| --- | --- |
| `docker attach <container>` | Attach to a container |
| `docker cp <container>:<container-path> <host-path>` | Copy files from the container |
| `docker cp <host-path> <container>:<container-path>` | Copy files into the container |
| `docker export <container>` | Export the content of the container (tar archive) |
| `docker exec <container>` | Run a command inside a container |
| `docker exec -it <container> /bin/bash` | Open an interactive shell inside a container (there is no bash in some images, use /bin/sh) |
| `docker wait <container>` | Wait until the container terminates and return the exit code |

## Images

| COMMAND | DESCRIPTION |
| --- | --- |
| `docker build . -t <local_image_name>` | Build docker image |
| `docker image ls` | List all local images |
| `docker history <image>` | Show the image history |
| `docker inspect <image>` | Show information (json formatted) |
| `docker tag <image> <tag>` | Tag an image |
| `docker commit <container> <image>` | Create an image (from a container) |
| `docker import <url>` | Create an image (from a tarball) |
| `docker rmi <image>` | Delete images |
| `docker pull <user>/<repository>:<tag>` | Pull an image from a registry |
| `docker push <user>/<repository>:<tag>` | Push and image to a registry |
| `docker search <test>` | Search an image on the official registry |
| `docker login` | Login to a registry |
| `docker logout` | Logout from a registry |
| `docker save <user>/<repository>:<tag>` | Export an image/repo as a tarball |
| `docker load` | Load images from a tarball |

## Volumes

| COMMAND | DESCRIPTION |
| --- | --- |
| `docker volume ls` | List all vol1umes |
| `docker volume create <volume>` | Create a volume |
| `docker volume inspect <volume>` | Show information (json formatted) |
| `docker volume rm <volume>` | Destroy a volume |
| `docker volume ls --filter="dangling=true"` | List all dangling volumes (not referenced by any container) |
| `docker volume prune` | Delete all volumes (not referenced by any container) |
| `docker run --rm --volumes-from <container> -v $(pwd):/backup busybox tar cvfz /backup/backup.tar.gz <container-path>` | Backup a container |
| `docker run --rm --volumes-from <container> -v $(pwd):/backup busybox sh -c "cd <container-path> && tar xvfz /backup/backup.tar.gz --strip 1"` | Restore a container from backup |

## Container file system extracted
docker export chronocraft-backend-1 -o backend.tar
mkdir extracted && tar -xf backend.tar -C extracted && cd extracted
tree -L 1 -a && tree -L 2 -a && tree -L 3 -a

## Container IP address in the host network
docker inspect nginx-server | grep IPAddress

## Docker image to a file
docker save -o my-image.tar my-image-name:tag

- Load to new machine: docker load -i my-image.tar
- Open tar file: tar -xf my-image.tar -C ./my-image

## Docker compose logs
docker compose logs -f dns
docker compose logs --tail=100

## private docker registry
- Log in to the private repository using the following command:
```docker login <repository_url>```
You will be prompted for your username and password for the repository.
- Tag your local Docker image with the repository URL using the following command:
```docker tag <local_image_name> <repository_url>/<image_name>:<tag>```
Replace <local_image_name> with the name of the Docker image you want to push, <repository_url> with the URL of your private repository, <image_name> with the name you want to use for the image in the repository, and <tag> with the tag you want to use for the image.
- Push the Docker image to the private repository using the following command:
```docker push <repository_url>/<image_name>:<tag>```
- Verify that the Docker image is available in your private repository by checking the repository's web interface or by running the following command:
```docker search <repository_url>/<image_name>```
This will search for the Docker image in your private repository.