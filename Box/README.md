# Box

Hoarder sends logs into box. Box is where logs will be held and can be retreived when required.

It receives messages to save from Hoarder via rabbitmq. Any update to client list in DB is propagated to Box so it can generate queue to accept clients message as soon as they are added.

Clients list is validated at every session refresh time.


## Setting up the Box

Following environment variables are required:

```
RABBITMQ_HOST=      # ip address of host where Rabbitmq is running
RABBITMQ_PORT=      # Port on which Rabbitmq is listening
RABBITMQ_USER=      # Username to authenticate against rabbitmq host
RABBITMQ_PASSWORD=  # Password to authenticate against rabbitmq host
RABBITMQ_VHOST=     # vHost that will be used for message passing
CLIENT_AUTH_TOKEN=  # Token/string used to authenticate against client for sending requests to it
CLIENT_ENDPOINT=    # http endpoint associated with client app
```


## Endpoints for client updates

### `/status`
A GET endpoint to check if application is up.


### `/clientel`
A POST endpoint that is specifically made for `Client App` to send client information to Box. POST body should be in following format:
```
{
    "clientId": "id-of-a-client",
    "token": "token-of-client-to-auth-against"
}
```
