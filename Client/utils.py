from random import random
from hashlib import md5


def generateToken():
    pseudoToken = f"{random.random()}"
    hash = md5(pseudoToken.encode())
    return hash.hexdigest()
