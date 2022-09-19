from pydantic import BaseModel


class LogMessage(BaseModel):
    logString: str
    clientId: str
    authToken: str
