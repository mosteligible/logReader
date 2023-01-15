from pathlib import Path

################################
# LOG DIRECTORY SETUP
################################

CWD = Path().cwd().absolute()
LOG_DIR = CWD / "LOGS"
LOG_DIR.mkdir(exist_ok=True, parents=True)

RECEIVER_LOG_DIR = LOG_DIR / "RECEIVER"
RECEIVER_LOG_DIR.mkdir(exist_ok=True, parents=True)
