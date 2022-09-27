from Exceptions import UserValidationError
from fastapi import FastAPI, Request
import threading

from Models import LogMessage, ClientInformation
from User import User
from Config import Clientel, Senders
import StatusCodes


app = FastAPI()


@app.get("/status")
async def status(request: Request):
    clientId = request.headers.get("id")
    if Clientel.get(clientId, False):
        return StatusCodes.success
    else:
        return StatusCodes.notAllowed


@app.post("/clientel")
async def updateClientel(clientData: ClientInformation):
    try:
        client = User(id=clientData.clientId, token=clientData.token)
    except UserValidationError:
        return StatusCodes.notAllowed

    Clientel.update({clientData.clientId: client})
    return StatusCodes.success


# TODO: Add endpoint or process to get all clients list on startup


@app.post("/message")
async def addClient(logMessage: LogMessage, request: Request):
    logText = logMessage.logString
    clientId = logMessage.clientId
    token = request.headers.get("token")
    client = Clientel.get(clientId, None)
    if client is None:
        return StatusCodes.notAllowed

    if token != client.token:
        return StatusCodes.notAllowed

    sender = Senders.get(clientId)
    senderThread = threading.Thread(daemon=True, target=sender.send, args=(logText))
    senderThread.start()

    return StatusCodes.success
