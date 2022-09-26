from fastapi import FastAPI, Request
from typing import Union
from threading import Thread

from Config import CLIENTDB
from Log import APP_LOGGER
from utils import generateToken, updateBoxReceiverQueue, updateHoarderClientel
from Models import ClientModel, ClientValidateModel



app = FastAPI()


@app.get("/status")
async def status():
    return {"status": 200}


@app.get("/get")
async def readClient(client_id: Union[str, None] = None):
    if client_id is None:
        return {
            "status": 403,
            "message": "Client ID must be provided. Client id was not supplied.",
        }

    client_details = CLIENTDB.RetreiveClient(client_id)

    if client_details is False:
        return {
            "status": 404,
            "message": "Client id does not exist",
        }
    return {
        "status": "200",
        "id": client_id,
        "name": client_details[1],
    }


@app.post("/add")
def addClient(client: ClientModel, request: Request):
    clientIp = request.client.host
    print("client ip:", clientIp)
    token = request.headers.get("token", None)
    payload = client.dict()
    payload.update({"ip": clientIp})
    print("Payload:", payload)
    if token is not None and CLIENTDB.AddEntry(dbPayload=payload):
        threads = [
            Thread(daemon=True, target=updateHoarderClientel),
            Thread(daemon=True, target=updateBoxReceiverQueue)
            ]
        for th in threads:
            th.run()
        return {
            "status": 200,
            "message": f"Successfully added {client.id} to Database",
        }
        
    else:
        return {"status": 500, "message": "Error adding provided client to Database"}


@app.post("/validate")
def validateClient(client: ClientValidateModel):
    client_details = CLIENTDB.RetreiveClient(client.id)

    # TODO: Authenticate for right service connection. Anyone can get client token here
    if client_details is False:
        return {"status": 403, "token": generateToken()}
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
