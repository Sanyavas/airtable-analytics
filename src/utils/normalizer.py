from datetime import datetime
from typing import Any, Dict, List, Optional


def parse_datetime(value: Optional[str]) -> Optional[datetime]:

    if not value:
        return None

    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def normalize_records(raw_records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:

    normalized: List[Dict[str, Any]] = []

    for record in raw_records:
        fields = record.get("fields", {})

        normalized.append(
            {
                "created_at": parse_datetime(fields.get("Created At")),
                "completed_at": parse_datetime(fields.get("Completed At")),
                "status": fields.get("Status"),
                "consultant": fields.get("Assigned Consultant"),
            }
        )

    return normalized
