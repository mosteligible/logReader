import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


TIMEOUT_DURATION = os.getenv("TIMEOUT_DURATION", 3600)

################################
# LOG DIRECTORY SETUP
################################

CWD = Path().cwd().absolute()
LOG_DIR = CWD / "LOGS"
LOG_DIR.mkdir(exist_ok=True, parents=True)

CLIENTEL_LOG = LOG_DIR / "CLIENTEL"
CLIENTEL_LOG.mkdir(exist_ok=True, parents=True)

USER_LOG_DIR = LOG_DIR / "USER"
USER_LOG_DIR.mkdir(exist_ok=True, parents=True)

SENDER_LOG_DIR = LOG_DIR / "SENDER"
SENDER_LOG_DIR.mkdir(exist_ok=True, parents=True)
