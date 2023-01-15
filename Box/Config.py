import os

from dotenv import load_dotenv
from Exceptions import EnvironmentVariableError

load_dotenv()


def isEnvValid(var: str, varName: str, default: str) -> bool:
    if var == default:
        raise EnvironmentVariableError(f"{varName} is not set")
    return True


LogReceivers = {}

APP_NAME = os.getenv("APP_NAME", "box")

################################
# RABBITMQ CONNECTION PARAMS
################################
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "")
isEnvValid(RABBITMQ_HOST, "RABBITMQ_HOST", "")

RABBITMQ_PORT = os.getenv("RABBITMQ_PORT", "")
isEnvValid(RABBITMQ_PORT, "RABBITMQ_PORT", "")

RABBITMQ_USER = os.getenv("RABBITMQ_USER", "")
isEnvValid(RABBITMQ_USER, "RABBITMQ_USER", "")

RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "")
isEnvValid(RABBITMQ_PASSWORD, "RABBITMQ_PASSWORD", "")

RABBITMQ_VHOST = os.getenv("RABBITMQ_VHOST", "")
isEnvValid(RABBITMQ_VHOST, "RABBITMQ_VHOST", "")

CLIENT_AUTH_TOKEN = os.getenv("CLIENT_AUTH_TOKEN", "")
isEnvValid(CLIENT_AUTH_TOKEN, "CLIENT_AUTH_TOKEN", "")

CLIENT_ENDPOINT = os.getenv("CLIENT_ENDPOINT", "")
isEnvValid(CLIENT_ENDPOINT, "CLIENT_ENDPOINT", "")
