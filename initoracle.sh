#!/bin/bash
# Run Docker Compose
sudo docker-compose up -d
# Change to the required directory
cd ./oracletx/locklift/sample-project-typescript

# Run yarn install
yarn install

# Run npx locklift commands
npx locklift init -f
npx locklift build

# Run the command and capture output
output=$(npx locklift run --network local --script scripts/1-deploy-sample.ts)

# Loop through each line of output
while IFS= read -r line
do
    # If the line starts with '0:', write it to the .env file
    if [[ $line == 0:* ]]
    then
        echo "SC_ADDRESS=$line" > .env
        break
    fi
done <<< "$output"

# Change to the pythonwatcher directory
cd ../../../pythonwatcher/

# Activate Python virtual environment
source bin/activate

# Install Python requirements
pip3 install -r requirements.txt

# Run celery worker
celery -A tasker worker --loglevel=info &

# Run Python script
python3 fast.py
