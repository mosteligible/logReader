from pydantic import BaseModel


class ClientModel(BaseModel):
    id: str
    name: str
    plan: str
