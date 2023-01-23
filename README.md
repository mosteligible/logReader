# logReader

A system design problem that requires designing a logging service.
It consists of client ends that subscribe to this logging service to save their logs. This logging service provides a way for clients to send their logs as they are generated.

The system consists of three parts to function.

1. A receiver to receive logs from clients.
2. A handler/parser to get logs received from clients to right format/structure to save.
3. A storage system to save the logs passed on by clients that also provides a way to acces the logs at later point in time.

## Preparing the application

`logReader` requires `db.env`, `client.env`, `box.env` and `hoarder.env` to run. Fields required in the `*.env` files are according to template provided in the repository. Template contains valid pre-populated values and if these are to be used, rename the template files by removing `.template` from filename and [run the application](#running-application).

The files should have following content.

`box.env`:
```
APP_NAME=box

RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672
RABBITMQ_USER=queueUser
RABBITMQ_PASSWORD=queueUserPassword
RABBITMQ_VHOST=QueueVhost

CLIENT_AUTH_TOKEN=tokenforboxtoauthenticateagainstforrretreivinginformation
CLIENT_ENDPOINT=http://clienttracker:8000
```

`client.env`:
```
CLIENT_DB_USERNAME=clientDBuname
CLIENT_DB_PASSWORD=ClientPW
CLIENT_DB_NAME=clientDB
CLIENT_DB_TABLE_NAME=clientData
CLIENT_DB_HOST=mysql

CLIENT_ADD_TOKEN=somevaluetoauthenticateagainstyeehaaww
BOX_ENDPOINT=http://box:5000
BOX_AUTH_TOKEN=tokenforboxtoauthenticateagainstforrretreivinginformation
HOARDER_ENDPOINT=http://hoarder:3000
HOARDER_AUTH_TOKEN=tokenforhoardertoauthenticateagainstforrretreivinginformation
```

`db.env`:
```
CLIENT_DB_USERNAME=clientDBuname
CLIENT_DB_PASSWORD=ClientPW
CLIENT_DB_NAME=clientDB
CLIENT_DB_TABLE_NAME=clientData
CLIENT_ADD_TOKEN=somevaluetoauthenticateagainstyeehaaww
MYSQL_ROOT_PASSWORD=rootpassword
```

`hoarder.env`:
```
APP_NAME=hoarder

RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672
RABBITMQ_USER=queueUser
RABBITMQ_PASSWORD=queueUserPassword
RABBITMQ_VHOST=QueueVhost

CLIENT_AUTH_TOKEN=tokenforhoardertoauthenticateagainstforrretreivinginformation
CLIENT_ENDPOINT=http://clienttracker:8000
```

## Running application

When right values are placed in the appropriate `env` files `logReader` can be run with:
```
$ make compose-logreader
...
Recreating logreader_mysql_1 ... done
Recreating logreader_clienttracker_1 ... done
Recreating logreader_hoarder_1       ... done
Recreating logreader_box_1           ... done
Attaching to logreader_mysql_1, logreader_clienttracker_1, logreader_hoarder_1, logreader_box_1
clienttracker_1  | INFO:     Started server process [1]
clienttracker_1  | INFO:     Waiting for application startup.
clienttracker_1  | INFO:     Application startup complete.
clienttracker_1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
mysql_1          | 2023-01-23 05:05:37+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.31-1debian11 started.
clienttracker_1  | INFO:     127.0.0.1:45114 - "GET /status HTTP/1.1" 200 OK
mysql_1          | 2023-01-23 05:05:37+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
mysql_1          | 2023-01-23 05:05:37+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.31-1debian11 started.
mysql_1          | 2023-01-23T05:05:38.053673Z 0 [Warning] [MY-011068] [Server] The syntax '--skip-host-cache' is deprecated and will be removed in a future release. Please use SET GLOBAL host_cache_size=0 instead.
mysql_1          | 2023-01-23T05:05:38.053738Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.32) starting as process 1
mysql_1          | 2023-01-23T05:05:38.063855Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
mysql_1          | 2023-01-23T05:05:38.125929Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
mysql_1          | 2023-01-23T05:05:38.203324Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
mysql_1          | 2023-01-23T05:05:38.203341Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
mysql_1          | 2023-01-23T05:05:38.204144Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
mysql_1          | 2023-01-23T05:05:38.212738Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.32'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
mysql_1          | 2023-01-23T05:05:38.212751Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Bind-address: '::' port: 33060, socket: /var/run/mysqld/mysqlx.sock
hoarder_1        | INFO:     Started server process [1]
hoarder_1        | INFO:     Waiting for application startup.
hoarder_1        | INFO:     Application startup complete.
hoarder_1        | INFO:     Uvicorn running on http://0.0.0.0:3000 (Press CTRL+C to quit)
clienttracker_1  | INFO:     172.25.0.5:43076 - "GET /clients/all HTTP/1.1" 200 OK
box_1            | INFO:     Started server process [1]
box_1            | INFO:     Waiting for application startup.
box_1            | INFO:     Application startup complete.
box_1            | INFO:     Uvicorn running on http://0.0.0.0:5000 (Press CTRL+C to quit)
clienttracker_1  | INFO:     172.25.0.4:49614 - "GET /clients/all HTTP/1.1" 200 OK
clienttracker_1  | INFO:     127.0.0.1:56674 - "GET /status HTTP/1.1" 200 OK
clienttracker_1  | INFO:     127.0.0.1:59934 - "GET /status HTTP/1.1" 200 OK
```

## Clean the images

Delete the images built with `make docker-cleanup`.
