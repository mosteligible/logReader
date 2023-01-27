import os
from pathlib import Path

from Database import ClientDatabase
from dotenv import load_dotenv

CLIENT_PATH = Path(__file__).absolute().parent.parent.parent
load_dotenv(dotenv_path=CLIENT_PATH / ".test.env")


TEST_DB_USERNAME = os.getenv("TEST_DB_USERNAME", "")
TEST_DB_PASSWORD = os.getenv("TEST_DB_PASSWORD", "")
TEST_DB_NAME = os.getenv("TEST_DB_NAME", "")
TEST_DB_HOST = os.getenv("TEST_DB_HOST", "127.0.0.1")
TEST_DB_TABLE_NAME = os.getenv("TEST_DB_TABLE_NAME", "")
TEST_DB_PORT = os.getenv("TEST_DB_PORT", 6603)

TEST_DB = ClientDatabase(
    username=TEST_DB_USERNAME,
    password=TEST_DB_PASSWORD,
    host=TEST_DB_HOST,
    database=TEST_DB_NAME,
    port=TEST_DB_PORT,
)
