from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

from .conftest import TEST_ADD_TOKEN

client = TestClient(app=app)


def test_add_client():
    headers = {"token": TEST_ADD_TOKEN}
    postbody = {
        "id": "clientid01",
        "name": "clientName01",
        "plan": "small",
        "token": "client01token",
    }
    response = client.post("/add", headers=headers, json=postbody)
    response_json = response.json()
    assert response_json["status"] == 200
    assert response_json["message"] == f"Successfully added {postbody['id']} to Database"
