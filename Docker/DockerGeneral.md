# General Notes for Docker

## 1. Install from default Ubuntu repositories
- Install
```bash
sudo apt install docker.io -y
```
- Verify
```bash
sudo systemctl status docker
```
- Add the logged-in user to the Docker group
```bash
sudo usermod -aG docker $USER
```
```bash
newgrp docker
```
```bash
groups $USER
```
- check version
```bash
docker version
```
- Run the basic hello-world
```bash
docker run hello-world
```
- Optional: Enable docker start when logged in
```bash
sudo systemctl enable docker
```

## 2. Install from Official Docker repository
- Install Prerequisite Packages
```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y 
```
- Add the GPG key for the official Docker repository
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
- Add Docker repository to APT repository
```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
```bash
sudo apt update
```
- Install Docker
```bash
sudo apt install docker-ce -y
```
- Verify
```bash
sudo systemctl status docker
```
- Add the logged-in user to the Docker group
```bash
sudo usermod -aG docker $USER
```
```bash
newgrp docker
```
```bash
groups $USER
```
- check version
```bash
docker version
```
- Run the basic hello-world
```bash
docker run hello-world
```
- Optional: Enable docker start when logged in
```bash
sudo systemctl enable docker
```

## 3. Migrate
- Create backup
```bash
$ docker volume ls
$ source_volume=name_of_your_source_volume 

$ backup_date=$(date +"%Y%m%d")
$ docker run --tty --rm --interactive --volume ${source_volume}:/source --volume ${PWD}/archive:/backup  alpine tar czvf /backup/${source_volume}_${backup_date}.tar.gz -C /source .
```
- Migrate to new host
```bash
$ target_volume=name_of_your_target_volume
$ restore_archive=${volume}_${backup_date}.tar.gz # of course the real name without placeholders

$ docker run --tty --rm --interactive --volume ${target_volume}:/target --volume ${PWD}/archive:/backup  alpine tar xzvf /backup/${restore_archive} -C /target
```


## 4. Other

#### Removing build cache
```bash
docker buildx prune -f
```

#### Volumes
```bash
docker volume list
```
```bash
docker volume inspect ----
```
```bash
docker volume rm ----
```
```bash
docker run -it --name <container-name> -v <volume-name>:<container-data-path> <image-name> /bin/bash
```

#### Compressed image
```bash
docker load -i ---.tar
```