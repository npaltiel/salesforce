from apiKeys import client_secret, client_id
import requests


async def get_token():
    url = "https://backendapi.medcheckusa.com/app-client/basic/get-access-token"

    # Replace with the actual data required by the API
    payload = {
        "client_id": client_id,
        "client_secret": client_secret
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    response_text = response.json()
    token = response_text['access_token']

    return token
