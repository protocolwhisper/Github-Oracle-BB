#!/bin/bash

# Stop Docker Compose
sudo docker compose down

# Remove Docker images
docker rmi $(docker images -a -q)

# Kill running Python3 scripts
pkill -f python3
