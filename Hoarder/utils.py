from typing import Dict
import requests
from Log import APP_LOGGER


def collectResponse(url: str, payload: Dict) -> requests.models.Response:
    retries = 0
    response = None
    while retries < 3:
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            APP_LOGGER.info(f"{response.request.method} - <{response.status_code}> - {url}")
            break
        except Exception as e:
            APP_LOGGER.error(f"{e} on {retries+1} tries requesting url:: {url}")
            retries += 1
    return response
