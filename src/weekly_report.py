from airtable_client import fetch_all_records
from utils.normalizer import normalize_records


def main():
    raw_records = fetch_all_records()
    records = normalize_records(raw_records)

    print("First normalized record:")
    print(records[0])
    print(raw_records)


if __name__ == "__main__":
    main()
