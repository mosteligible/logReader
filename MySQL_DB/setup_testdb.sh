#!/bin/bash

export $(cat .test.env)

if [[ -z "$TEST_DB_USERNAME" || \
      -z "$MYSQL_ROOT_PASSWORD" || \
      -z "$TEST_ADD_TOKEN" || \
      -z "$TEST_DB_PASSWORD" || \
      -z "$TEST_DB_TABLE_NAME" ]]; then
    echo ">> Environment variables
    TEST_DB_USERNAME
    TEST_DB_PASSWORD
    TEST_DB_TABLE_NAME
    TEST_ADD_TOKEN
    MYSQL_ROOT_PASSWORD
    must be set before running this target."
    exit 1
fi

echo ">> Database environment variables exported..."

echo ">> Generating testdb_setup.sql file..."

echo \
"CREATE DATABASE IF NOT EXISTS $TEST_DB_NAME;
USE $TEST_DB_NAME;
CREATE TABLE IF NOT EXISTS $TEST_DB_TABLE_NAME (
    id varchar(50) NOT NULL,
    name varchar(50),
    plan varchar(20),
    token varchar(100),
    PRIMARY KEY (ID)
);
CREATE USER '$TEST_DB_USERNAME'@'%' IDENTIFIED BY '$TEST_DB_PASSWORD';
GRANT ALL ON $TEST_DB_NAME.* TO '$TEST_DB_USERNAME'@'%';" > ./MySQL_DB/testdb_setup.sql
