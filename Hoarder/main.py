from fastapi import FastAPI
from typing import Union

from Log import APP_LOGGER
from Models import LogMessage


app = FastAPI()


@app.get("/status")
async def status():
    return {"status": 200}


@app.post("/message")
async def add_client(logMessage: LogMessage):
    return {
        "status": 200,
        "message": f"Log added successfully.",
    }
