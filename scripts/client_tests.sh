#!/bin/bash

echo ">> Setting up test mysql docker image.."
bash ./MySQL_DB/setup_testdb.sh && \

docker build -t testdb-mysql:1.0.0 \
             -f ./MySQL_DB/Dockerfile.test_db ./MySQL_DB && \

echo ">> Starting test db docker image.."
docker run -d -p 6603:3306 --env-file .test.env testdb-mysql:1.0.0
sleep 10

echo ">> Pulling python image for running tests.."

docker pull python:3.10.0-slim-bullseye

echo ">> Initiating tests..."

docker run -it -v $(pwd)/Client:/mnt \
           --env-file .test.env \
           --network="host" \
           python:3.10.0-slim-bullseye \
           bash -c 'cd /mnt && \
                    pip install -r requirements.txt --no-cache-dir && \
                    python3 -m unittest'

echo ">> Finishing tests and stopping containers.."
running_images=$(docker ps -aq | wc -l)
sleep 2
if [[ $running_images -gt 0 ]]; then
    docker stop $(docker ps -aq)
fi

echo ">> Deleting containers and freeing caches.."
docker rmi -f python:3.10.0-slim-bullseye
docker rmi -f testdb-mysql:1.0.0
docker system prune -f
