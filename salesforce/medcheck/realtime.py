import requests
from apiKeys import client_group, client_entity


async def realtime_request(token, medicaid_id):
    url = "https://backendapi.medcheckusa.com/realtime/basic/submit"

    # Replace with the actual data required by the API
    payload = {
        "group": client_group,
        "entity": client_entity,
        "benefit_provider": "medicaid",
        "benefit_provider_id": medicaid_id,
        "date_of_service": "2025-04-07"
    }

    headers = {
        "Content-Type": "application/json",
        "id-token": token
    }

    response = requests.post(url, json=payload, headers=headers)
    response_text = response.json()

    print(response.status_code)
    return response_text
