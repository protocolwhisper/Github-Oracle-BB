#!/bin/bash

function display_loading {
    echo -ne 'Loading...\r'
    sleep 1
    echo -ne 'Loading....\r'
    sleep 1
    echo -ne 'Loading......\r'
    sleep 1
    echo -ne 'Loading........\r'
    sleep 1
    echo -ne '\n'
}

function display_banner {
    echo "                                                                                                        "
    echo "          _ __        _                            __                  __                                         __   "
    echo "   ____ _(_) /_      (_)___________  _____        / /__________ ______/ /_____  _____      ____  _________ ______/ /__ "
    echo "  / __ '/ / __/_____/ / ___/ ___/ / / / _ \______/ __/ ___/ __ '/ ___/ //_/ _ \/ ___/_____/ __ \/ ___/ __ '/ ___/ / _ \ "
    echo " / /_/ / / /_/_____/ (__  |__  ) /_/ /  __/_____/ /_/ /  / /_/ / /__/ ,< /  __/ /  /_____/ /_/ / /  / /_/ / /__/ /  __/ "
    echo " \__, /_/\__/     /_/____/____/\__,_/\___/      \__/_/   \__,_/\___/_/|_|\___/_/         \____/_/   \__,_/\___/_/\___/ "
    echo "/____/                                                                                                                 "
}

function setup_locklift {
    cd ./oracletx/locklift/sample-project-typescript
    yarn install
    npx locklift init -f
    npx locklift build
}

function run_and_capture_output {
    output=$(npx locklift run --network local --script scripts/1-deploy-sample.ts)
    while IFS= read -r line
    do
        if [[ $line == 0:* ]]
        then
            echo "SC_ADDRESS=$line" > .env
            break
        fi
    done <<< "$output"
}

function setup_python_watcher {
    cd ../../../pythonwatcher/
    source bin/activate
    cd ..
    pip3 install -r requirements.txt
    celery -A tasker worker --loglevel=info &
    python3 fast.py > /dev/null 2>&1 &
}

display_loading
display_banner
sudo docker-compose up -d
setup_locklift
run_and_capture_output
setup_python_watcher
