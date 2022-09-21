import os
from dotenv import load_dotenv


load_dotenv()


################################
# RABBITMQ CONNECTION PARAMS
################################
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "")
isEnvValid(RABBITMQ_HOST, "RABBITMQ_HOST", "")
