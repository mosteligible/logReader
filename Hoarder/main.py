from Exceptions import UserValidationError
from fastapi import FastAPI, Request

from Models import LogMessage, ClientInformation
from User import User
from Config import Clientel


app = FastAPI()


@app.get("/status")
async def status(request: Request):
    clientId = request.headers.get("id")
    if Clientel.get(clientId, False):
        return {"status": 200}
    else:
        return {"message": "Not Allowed"}


@app.post("/clientel")
async def updateClientel(clientData: ClientInformation):
    try:
        client = User(id=clientData.clientId, token=clientData.token)
    except UserValidationError:
        return {"status": 403, "message": "Not Allowed"}

    Clientel.update({clientData.clientId: client})
    return {"status": 200}


@app.post("/message")
async def addClient(logMessage: LogMessage, request: Request):
    logText = logMessage.logString
    clientId = logMessage.clientId

    # Validate connection and send message to queue to be saved

    return {
        "status": 200,
        "message": f"Log added successfully.",
    }
