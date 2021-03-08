#!/bin/bash

pip3 install -r requirements.txt

#docker-compose up -d

docker cp ./tmp/dump.sql restaurant_postgres_1:/tmp
docker exec -ti restaurant_postgres_1 bash -c "dropdb -U postgres dev && createdb -U postgres dev && psql -U postgres -d dev -f /tmp/dump.sql"
python3 manage.py runserver