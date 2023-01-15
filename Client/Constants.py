import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

CLIENT_DB_USERNAME = os.getenv("CLIENT_DB_USERNAME", "")
CLIENT_DB_PASSWORD = os.getenv("CLIENT_DB_PASSWORD", "")
CLIENT_DB_NAME = os.getenv("CLIENT_DB_NAME", "")
CLIENT_DB_HOST = os.getenv("CLIENT_DB_HOST", "")
CLIENT_DB_TABLE_NAME = os.getenv("CLIENT_DB_TABLE_NAME", "")

################################
# LOG DIRECTORY SETUP
################################

CWD = Path().cwd().absolute()
LOG_DIR = CWD / "LOGS"
LOG_DIR.mkdir(exist_ok=True, parents=True)

CLIENT_LOG_LOCATION = LOG_DIR / "CLIENTS"
CLIENT_LOG_LOCATION.mkdir(exist_ok=True, parents=True)
DB_LOG_LOCATION = LOG_DIR / "DB"
DB_LOG_LOCATION.mkdir(exist_ok=True, parents=True)
