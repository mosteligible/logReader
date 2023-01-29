#!/bin/bash

export $(cat db.env)

if [[ -z "$CLIENT_DB_USERNAME" || \
      -z "$MYSQL_ROOT_PASSWORD" || \
      -z "$CLIENT_ADD_TOKEN" || \
      -z "$CLIENT_DB_PASSWORD" || \
      -z "$CLIENT_DB_TABLE_NAME" ]]; then
    echo ">> Environment variables
    CLIENT_DB_USERNAME
    CLIENT_DB_PASSWORD
    CLIENT_DB_TABLE_NAME
    CLIENT_ADD_TOKEN
    MYSQL_ROOT_PASSWORD
    must be set before running this target."
    exit 1
fi

echo ">> Database environment variables exported..."

echo ">> Generating db_setup.sql file..."

echo \
"CREATE DATABASE IF NOT EXISTS $CLIENT_DB_NAME;
USE $CLIENT_DB_NAME;
CREATE TABLE IF NOT EXISTS $CLIENT_DB_TABLE_NAME (
    id varchar(50) NOT NULL,
    name varchar(50),
    plan varchar(20),
    ip varchar(50),
    token varchar(100),
    PRIMARY KEY (ID)
);
CREATE USER '$CLIENT_DB_USERNAME'@'%' IDENTIFIED BY '$CLIENT_DB_PASSWORD';
GRANT ALL ON $CLIENT_DB_NAME.* TO '$CLIENT_DB_USERNAME'@'%';" > ./MySQL_DB/db_setup.sql
