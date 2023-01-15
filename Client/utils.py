from hashlib import md5
from random import random


def generateToken():
    pseudoToken = f"{random.random()}"
    hash = md5(pseudoToken.encode())
    return hash.hexdigest()


def updateHoarderClientel() -> None:
    return None


def updateBoxReceiverQueue() -> None:
    return None
