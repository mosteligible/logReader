from fastapi import FastAPI, Request
from typing import Union

from Log import APP_LOGGER
from Models import LogMessage
from Config import Clientel


app = FastAPI()


@app.get("/status")
async def status(request: Request):
    clientId = request.headers.get("id")
    if Clientel.get(clientId, False):
        return {"status": 200}
    else:
        return {"message": "Not Allowed"}


@app.post("/message")
async def add_client(logMessage: LogMessage, request: Request):
    return {
        "status": 200,
        "message": f"Log added successfully.",
    }
