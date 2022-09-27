# Client

A Client Tracker application. This provides a way to keep track of which clients are currently subscribed and who should Hoarder system keep receiving logs from.

## To setup Client Tracker

Set following environment variables

```
CLIENT_DB_USERNAME=    # DB Username for Client Tracker App
CLIENT_DB_PASSWORD=    # DB Password for Client Tracker App
CLIENT_DB_NAME=        # DB Name that is used be Client Tracker App
CLIENT_DB_HOST=        # Host ip, where DB is hosted
CLIENT_DB_TABLE_NAME=  # Table name where client information is held
BOX_ENDPOINT=          # Endpoint associated with Box App
BOX_AUTH_TOKEN=        # Token for Box App to authenticate against client for information retreival
HOARDER_ENDPOINT=      # Endpoint of Hoarder App
HOARDER_AUTH_TOKEN=    # Token for Hoarder App to authenticate against client for information retreival
```

To run client from a docker image save above environment variables in a file called `client.env` then run following to start docker image:
```
make docker

# To validate if docker image is running, use following
docker ps

# To stop docker image
make docker-stop
```

To run locally, either export the above variables in environment or save them in a `.env` file in the project directory then run:
```
make local
```

## Endpoints available for Client Tracker

### `/status`
A GET endpoint to check if the client tracker application is up and running. This endpoint provides status of 200 when invoked and it means that application is up and running at that moment.

This endpoint does not require any validation to use at the moment. No authentication token should be passed to get application status with this endpoint.


### `/get`
A GET endpoint that takes client's id as a parameter and returns name of client associated with the id. If no match is found, it returns error.


### `/add`
A POST endpoint that adds client to the Client Database. Post request contains client's id, name, plan and connection token provided to them.

To successfully add client to the database, request should contain header with a token used to authenticate so just anyone won't be able to send request to add entry in Database. Token in headers should be as following:

```
{"token": "some#string:value-to-authenticate@against"}
```

After successful addition to Database, Client App will update Hoarder and Box with updated client's information.


### `/validate`
A POST endpoint to check if a given client exists in the Database.


### `/delete`
A DELETE endpoint to remove client from database.
