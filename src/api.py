from fastapi import FastAPI
from weekly_report import main

app = FastAPI()


@app.post("/run-weekly-report")
def run_report():
    main()
    return {"status": "ok"}
