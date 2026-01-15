from datetime import datetime, timezone
from pprint import pprint

from src.airtable_client import fetch_all_records
from src.utils.normalizer import normalize_records
from src.metrics import calculate_metrics
from src.report_writer import write_csv_report, build_csv_bytes
from config.settings import settings


def main() -> bytes:
    raw_records = fetch_all_records()
    records = normalize_records(raw_records)

    metrics = calculate_metrics(
        records=records,
        report_days=settings.REPORT_DAYS,
        now=datetime.now(timezone.utc),
    )

    csv_bytes = build_csv_bytes(metrics)
    return csv_bytes


if __name__ == "__main__":
    main()
