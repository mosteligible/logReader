from threading import active_count
import uvicorn
from utils import retreiveAllClients

from httpserver import app
from Log import APP_LOGGER
from Config import LogReceivers
from Receiver import Receiver


def initMessaging() -> None:
    clientels = retreiveAllClients()
    for client in clientels:
        logReceiver = Receiver(client["id"])
        LogReceivers[client["id"]] = logReceiver
        logReceiver.start()
    APP_LOGGER.info(f"logReceivers: {LogReceivers}")
    return None


if __name__ == "__main__":
    initMessaging()
    APP_LOGGER.info(f"Active threads: {active_count()}")
    uvicorn.run(app=app, host="0.0.0.0", port=5000)
