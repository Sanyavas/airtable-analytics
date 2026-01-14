from config.settings import settings


def main():
    print("Airtable table:", settings.AIRTABLE_TABLE_NAME)
    print("Report days:", settings.REPORT_DAYS)


if __name__ == "__main__":
    main()
