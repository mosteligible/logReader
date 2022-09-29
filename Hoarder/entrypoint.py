from threading import Thread
import time
import uvicorn
from utils import retreiveAllClients

from httpserver import app
from Config import Clientel, Senders
from Package import Sender
from User import User
from Log import APP_LOGGER


def initMessaging() -> None:
    time.sleep(5)
    clientels = retreiveAllClients()
    for client in clientels:
        user = User(id=client[0], token=client[4], validate=True)
        Clientel[client[0]] = user
        Senders[client[0]] = Sender(clientId=client[0])
    return None


if __name__ == "__main__":
    appThread = Thread(target=initMessaging)
    appThread.start()
    uvicorn.run(app=app, host="0.0.0.0", port=3000)
