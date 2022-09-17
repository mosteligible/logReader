import Constants
from Database import ClientDatabase


CLIENTDB = ClientDatabase(
    username=Constants.CLIENT_DB_USERNAME,
    password=Constants.CLIENT_DB_PASSWORD,
    host=Constants.CLIENT_DB_HOST,
    database=Constants.CLIENT_DB_NAME,
)
