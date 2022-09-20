import os
from dotenv import load_dotenv
from pathlib import Path

from Exceptions import EnvironmentVariableError


load_dotenv()


def isEnvValid(var: str, varName: str, default: str) -> bool:
    if var == default:
        raise EnvironmentVariableError(f"{varName} is not set")
    return True


TIMEOUT_DURATION = os.getenv("TIMEOUT_DURATION", 3600)

################################
# LOG DIRECTORY SETUP
################################

CWD = Path().cwd().absolute()
LOG_DIR = CWD / "LOGS"
LOG_DIR.mkdir(exist_ok=True, parents=True)

################################
# CLIENT AUTHENTICATION
################################

CLIENT_ENDPOINT = os.getenv("CLIENT_ENDPOINT", "")
isEnvValid(CLIENT_ENDPOINT, "CLIENT_ENDPOINT", "")
