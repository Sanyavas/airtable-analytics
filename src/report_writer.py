import csv
import io
from datetime import date
from pathlib import Path
from typing import Dict, Any


def write_csv_report(metrics: Dict[str, Any]) -> Path:
    """
    Write weekly metrics report to CSV file.
    Returns path to generated file.
    """
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    filename = f"weekly_report_{date.today().isoformat()}.csv"
    filepath = reports_dir / filename

    rows = [
        ("new_requests_7d", metrics["new_requests_7d"]),
        ("completed_requests_7d", metrics["completed_requests_7d"]),
        ("avg_processing_time_hours", metrics["avg_processing_time_hours"]),
    ]

    # Top consultants
    top_consultants = metrics.get("top_consultants", [])
    for i in range(3):
        if i < len(top_consultants):
            name, count = top_consultants[i]
            value = f"{name} ({count})"
        else:
            value = "—"

        rows.append((f"top_consultant_{i + 1}", value))

    with filepath.open(mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["metric", "value"])
        writer.writerows(rows)

    return filepath


def build_csv_bytes(metrics: Dict[str, Any]) -> bytes:
    """
    Build weekly metrics report as CSV bytes (in-memory).
    Used for HTTP response / n8n integration.
    """
    buffer = io.StringIO()
    writer = csv.writer(buffer)

    rows = [
        ("new_requests_7d", metrics["new_requests_7d"]),
        ("completed_requests_7d", metrics["completed_requests_7d"]),
        ("avg_processing_time_hours", metrics["avg_processing_time_hours"]),
    ]

    # Top consultants
    top_consultants = metrics.get("top_consultants", [])
    for i in range(3):
        if i < len(top_consultants):
            name, count = top_consultants[i]
            value = f"{name} ({count})"
        else:
            value = "—"

        rows.append((f"top_consultant_{i + 1}", value))

    writer.writerow(["metric", "value"])
    writer.writerows(rows)

    return buffer.getvalue().encode("utf-8")
