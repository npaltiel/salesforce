from get_token import get_token
from realtime import realtime_request
from batch_request import batch_request
from get_run_status import get_run_details
import asyncio
import time


async def main():
    # Get Medicaid IDs
    # Format them into a list of objects

    token = await get_token()

    run_id, run_status = batch_request(token, medicaid_ids)

    while True:
        result = get_run_details(token, run_id)
        print("Run status:", result)

        if result == "Success":
            print("✅ Run completed successfully.")
            break

        print("⏳ Not ready yet. Checking again in 15 minutes...")
        time.sleep(15 * 60)  # 15 minutes
