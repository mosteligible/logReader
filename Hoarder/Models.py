from pydantic import BaseModel


class ClientInformation(BaseModel):
    clientId: str
    token: str


class LogMessage(BaseModel):
    logString: str
    clientId: str
    authToken: str
