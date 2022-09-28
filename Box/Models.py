from pydantic import BaseModel


class ClientInformation(BaseModel):
    clientId: str
    token: str
