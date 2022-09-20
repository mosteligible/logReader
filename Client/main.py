from Models import ClientModel, ClientValidateModel
from fastapi import FastAPI
from typing import Union

from Config import CLIENTDB
from Log import APP_LOGGER


app = FastAPI()


@app.get("/status")
async def status():
    return {"status": 200}


@app.get("/get")
async def readClient(client_id: Union[str, None] = None):
    if client_id is None:
        return {"status": 403, "message": "Client ID must be provided. Client id was not supplied."}

    client_details = CLIENTDB.RetreiveClient(client_id)

    if client_details is False:
        return "Error getting client details from DB"
    return {
        "status": "200",
        "id": client_id,
        "name": client_details[1],
    }


@app.post("/add")
def addClient(client: ClientModel):
    if CLIENTDB.AddEntry(client.dict()):
        return {
            "status": 200,
            "message": f"Successfully added {client.id} to Database",
        }
    else:
        return {"status": 500, "message": "Error adding provided client to Database"}


@app.post("/validate")
async def validateClient(client: ClientValidateModel):
    client_details = CLIENTDB.RetreiveClient(client.id)

    if client_details is False:
        return {"status": 403}
    return {
        "status": "200",
        "id": client.id,
        "name": client_details[1],
        "plan": client_details[2],
        "token": client_details[3],
    }


@app.delete("/delete")
def delete_client(client: str):
    if client is None:
        return {"status": 400, "message": "Required parameters were not provided"}
    if CLIENTDB.DeleteClient(client) is False:
        return {"status": 500, "message": "Error deleting client"}
    return {"status": 200, "message": "successfully deleted client from Database"}
