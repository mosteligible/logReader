# Hoarder

Accepts log messages from clients, parses them and saves them to storage for retreival from clients later.

Hoarder expects clients to send their authentication credentials in request headers. These credentials are provided to clients and they should be appended to request headers.



## Endpoints

### `/status`
A GET endpoint to check if the application is running. Status of 200 means that application is up.

### `/clientel`
A POST endpoint that receives information of new clientel added to DB and adds the client to memory.

### `/message`
A POST endpoint that receives log messages from clients and saves them in a storage for retreival at later time.
