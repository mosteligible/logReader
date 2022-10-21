from Exceptions import UserValidationError
from fastapi import FastAPI, Request
import threading
from Log import APP_LOGGER

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


@app.post("/message")
def addClient(logMessage: LogMessage, request: Request):
    logText = logMessage.logString
    clientId = logMessage.clientId
    token = logMessage.authToken
    client = Clientel.get(clientId, None)
    APP_LOGGER.info(f"client Id: {clientId} - client in Clientel: {client}")
    if client is None:
        return StatusCodes.notAllowed

    if token != client.token:
        return StatusCodes.notAllowed

    sender = Senders.get(clientId)
    senderThread = threading.Thread(daemon=True, target=sender.send, args=(logText,))
    senderThread.start()

    return StatusCodes.success
