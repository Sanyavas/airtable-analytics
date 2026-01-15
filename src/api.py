from fastapi import FastAPI, Response
from src.weekly_report import main

app = FastAPI()


@app.post("/run-weekly-report")
def run_report():
    csv_bytes = main()

    headers = {
        "Content-Disposition": 'attachment; filename="weekly_report.csv"'
    }

    return Response(
        content=csv_bytes,
        media_type="text/csv",
        headers=headers,
    )
