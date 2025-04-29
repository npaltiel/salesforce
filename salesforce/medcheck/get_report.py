import requests
from apiKeys import client_group, client_entity


async def get_report(token, run_id):
    url = "https://backendapi.medcheckusa.com/results/basic/report"

    # Replace with the actual data required by the API
    payload = {
        "group": client_group,
        "entity": client_entity,
        "run_id": run_id
    }

    headers = {
        "Content-Type": "application/json",
        "id-token": token
    }

    response = requests.post(url, json=payload, headers=headers)
    response_text = response.json()
    results = response_text['results']

    return results
