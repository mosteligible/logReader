from threading import Thread
import uvicorn
from utils import retreiveAllClients

from httpserver import app
from Config import LogReceivers
from Receiver import Receiver


def initMessaging() -> None:
    clientels = retreiveAllClients()
    for client in clientels:
        logReceiver = Receiver(client[0])
        LogReceivers[client[0]] = logReceiver
        logReceiver.run()
    return None


if __name__ == "__main__":
    appThread = Thread(target=initMessaging)
    appThread.start()
    uvicorn.run(app=app, host="0.0.0.0", port=5000)
