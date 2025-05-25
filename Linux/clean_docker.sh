#!/bin/bash

# Function to stop and remove all running and stopped containers
clean_containers() {
    echo "[1/5] Cleaning up Docker containers..."
    if [ -n "$(docker ps -aq)" ]; then
        docker stop $(docker ps -aq) && docker rm $(docker ps -aq)
    fi
}

check_containers() {
    docker ps -a
    echo ""
}

# Function to remove unused images
clean_images() {
    echo "[2/5] Cleaning up Docker images..."
    docker image prune -af
}

check_images() {
    docker images
    echo ""
}

# Function to remove unused volumes
clean_volumes() {
    echo "[3/5] Cleaning up Docker volumes..."
    if [ -n "$(docker volume ls -q)" ]; then
        docker volume rm $(docker volume ls -q)
    fi

}

check_volumes() {
    docker volume ls
    echo ""
}

# Function to remove unused networks
clean_networks() {
    echo "[4/5] Cleaning up Docker networks..."
    docker network prune -f
}

check_networks() {
    docker network ls
    echo ""
}

clean_cache_memory() {
    echo "[5/5] Cleaning cache memory..."
    docker builder prune -f
}

# Main function to run all clean up functions
cleanup_docker() {
    echo ""
    echo "----- START -----"
    echo ""
    clean_containers
    check_containers
    echo ""
    clean_images
    check_images
    echo ""
    clean_volumes
    check_volumes
    echo ""
    clean_networks
    check_networks
    echo ""
    clean_cache_memory
    echo ""
    echo "----- FINISH -----"
    echo ""
}

# Run the cleanup
cleanup_docker
