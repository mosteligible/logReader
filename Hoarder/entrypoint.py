import time
from threading import Thread

import uvicorn
from Config import Clientel, Senders
from httpserver import app
from Package import Sender
from User import User
from utils import retreiveAllClients


def initMessaging() -> None:
    while True:
        clientels = retreiveAllClients()
        for client in clientels:
            user = User(id=client["id"], token=client["token"], validate=True)
            Clientel[client["id"]] = user
            Senders[client["id"]] = Sender(clientId=client["id"])
        # Every 5 minutes, check for update to client list
        time.sleep(300)


if __name__ == "__main__":
    appThread = Thread(target=initMessaging)
    appThread.start()
    uvicorn.run(app=app, host="0.0.0.0", port=3000)
