FROM node:latest

# install dependencies
RUN apt-get update && \
    apt-get install -y wget unzip build-essential python3-pip && \
    rm -rf /var/lib/apt/lists/*

# install Redis GUI
RUN npm install -g redis-commander

# expose port 8001
EXPOSE 8001

# set Redis GUI to run on port 8001
CMD ["redis-commander", "--redis-host", "redis", "--redis-port", "6379", "--http-auth-username", "admin", "--http-auth-password", "password", "--port", "8001"]

