import os
from dotenv import load_dotenv

from Exceptions import EnvironmentVariableError


load_dotenv()


def isEnvValid(var: str, varName: str, default: str) -> bool:
    if var == default:
        raise EnvironmentVariableError(f"{varName} is not set")
    return True


################################
# CLIENT AUTHENTICATION
################################

CLIENT_ENDPOINT = os.getenv("CLIENT_ENDPOINT", "")
isEnvValid(CLIENT_ENDPOINT, "CLIENT_ENDPOINT", "")

Clientel = {}

################################
# RABBITMQ CONNECTION PARAMS
################################
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "")
isEnvValid(RABBITMQ_HOST, "RABBITMQ_HOST", "")
