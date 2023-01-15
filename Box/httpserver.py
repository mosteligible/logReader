import StatusCodes
from Config import LogReceivers
from fastapi import FastAPI, Request
from Models import ClientInformation
from User import User

app = FastAPI()


@app.get("/status")
async def status(request: Request):
    return StatusCodes.success


@app.post("/clientel")
async def updateClientel(client: ClientInformation):
    user = User(id=client.clientId, token=client.token)
    LogReceivers.update({client.clientId: user})
