import requests
from apiKeys import client_group, client_entity


async def batch_request(token, medicaid_ids: list):
    url = "https://backendapi.medcheckusa.com/batches/submit-json"

    # Replace with the actual data required by the API
    payload = {
        "group": client_group,
        "entity": client_entity,
        "benefit_provider": "medicaid",
        "beneficiaries": medicaid_ids
    }

    headers = {
        "Content-Type": "application/json",
        "id-token": token
    }

    response = requests.post(url, json=payload, headers=headers)
    response_text = response.json()
    run_id = response_text['run_id']
    run_status = response_text['run_status']

    return run_id, run_status
