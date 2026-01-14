from airtable_client import fetch_all_records


def main():
    records = fetch_all_records()
    print(f"Fetched records: {len(records)}")


if __name__ == "__main__":
    main()
