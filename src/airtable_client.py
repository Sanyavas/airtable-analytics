import requests
from typing import List, Dict, Any

from config.settings import settings


AIRTABLE_API_URL = "https://api.airtable.com/v0"


def fetch_all_records() -> List[Dict[str, Any]]:
    records: List[Dict[str, Any]] = []
    offset: str | None = None

    headers = {
        "Authorization": f"Bearer {settings.AIRTABLE_API_KEY}",
    }

    while True:
        params = {}
        if offset:
            params["offset"] = offset

        response = requests.get(
            f"{AIRTABLE_API_URL}/{settings.AIRTABLE_BASE_ID}/{settings.AIRTABLE_TABLE_NAME}",
            headers=headers,
            params=params,
            timeout=10,
        )
        response.raise_for_status()

        data = response.json()
        records.extend(data.get("records", []))

        offset = data.get("offset")
        if not offset:
            break

    return records
