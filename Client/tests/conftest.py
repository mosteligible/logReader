import os
from pathlib import Path

from dotenv import load_dotenv

CLIENT_PATH = Path(__file__).absolute().parent.parent
load_dotenv(dotenv_path=CLIENT_PATH / ".test.env")


TEST_DB_USERNAME = os.getenv("TEST_DB_USERNAME", "")
TEST_DB_PASSWORD = os.getenv("TEST_DB_PASSWORD", "")
TEST_DB_NAME = os.getenv("TEST_DB_NAME", "")
TEST_DB_HOST = os.getenv("TEST_DB_HOST", "")
TEST_DB_TABLE_NAME = os.getenv("TEST_DB_TABLE_NAME", "")