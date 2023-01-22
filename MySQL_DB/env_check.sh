#!/bin/bash

if [[ -z "$CLIENT_DB_USERNAME" || \
      -z "$MYSQL_ROOT_PASSWORD" || \
      -z "$CLIENT_ADD_TOKEN" || \
      -z "$CLIENT_DB_PASSWORD" || \
      -z "$CLIENT_DB_TABLE_NAME" ]]; then
    echo "Environment variables
    CLIENT_DB_USERNAME
    CLIENT_DB_PASSWORD
    CLIENT_DB_TABLE_NAME
    CLIENT_ADD_TOKEN
    MYSQL_ROOT_PASSWORD
    must be set before running this target."
    exit 1
fi
