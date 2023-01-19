import time
from typing import Dict

import requests
from Config import APP_NAME, CLIENT_AUTH_TOKEN, CLIENT_ENDPOINT
from Log import APP_LOGGER


def collectResponse(url: str, payload: Dict) -> requests.models.Response:
    retries = 0
    response = None
    APP_LOGGER.info(f"Sending POST request to: {url} with payload: {payload}")
    while retries < 3:
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            APP_LOGGER.info(f"{response.request.method} - <{response.status_code}> - {url}")
            break
        except Exception as e:
            APP_LOGGER.error(f"{e} on {retries+1} tries requesting url:: {url}")
            time.sleep(10)
            retries += 1
    return response


def retreiveAllClients():
    headers = {"application_instance": APP_NAME, "token": CLIENT_AUTH_TOKEN}
    url = f"{CLIENT_ENDPOINT}/clients/all"
    retries = 0
    clientel = []
    APP_LOGGER.info(f"Sending GET request to: {url}")
    while retries < 3:
        try:
            response = requests.get(url=url, headers=headers)
            clientel = response.json()["clientel"]
            break
        except Exception as e:
            APP_LOGGER.error(f"{e} on {retries+1} tries requesting url: {url}")
            print(f"{e} on {retries+1} tries requesting url: {url}")
            time.sleep(10)
            retries += 1
    return clientel
