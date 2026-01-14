from collections import Counter
from datetime import datetime, timedelta
from typing import Dict, List, Any


def calculate_metrics(
    records: List[Dict[str, Any]],
    report_days: int,
    now: datetime,
) -> Dict[str, Any]:
    """
    Calculate weekly operational metrics.
    """
    period_start = now - timedelta(days=report_days)

    new_requests = 0
    completed_requests = 0
    processing_times = []
    consultant_counter = Counter()

    for record in records:
        created_at = record.get("created_at")
        completed_at = record.get("completed_at")
        status = record.get("status")
        consultant = record.get("consultant")

        if created_at and created_at >= period_start:
            new_requests += 1

        if (
            status == "Completed"
            and completed_at
            and completed_at >= period_start
        ):
            completed_requests += 1
            consultant_counter[consultant] += 1

            if created_at:
                processing_times.append(
                    (completed_at - created_at).total_seconds()
                )

    avg_processing_time_hours = (
        sum(processing_times) / len(processing_times) / 3600
        if processing_times
        else 0
    )

    top_consultants = consultant_counter.most_common(3)

    return {
        "new_requests_7d": new_requests,
        "completed_requests_7d": completed_requests,
        "avg_processing_time_hours": round(avg_processing_time_hours, 2),
        "top_consultants": top_consultants,
    }
