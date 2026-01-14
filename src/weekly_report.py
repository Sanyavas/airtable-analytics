from datetime import datetime, timezone
from pprint import pprint

from airtable_client import fetch_all_records
from report_writer import write_csv_report
from utils.normalizer import normalize_records
from metrics import calculate_metrics
from config.settings import settings


def main():
    raw_records = fetch_all_records()
    records = normalize_records(raw_records)

    metrics = calculate_metrics(
        records=records,
        report_days=settings.REPORT_DAYS,
        now=datetime.now(timezone.utc),
    )

    report_path = write_csv_report(metrics)
    print(f"Weekly report generated: {report_path}")

    print(metrics)

    # pprint(raw_records)


if __name__ == "__main__":
    main()
