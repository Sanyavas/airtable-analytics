# Airtable Weekly Analytics Automation

End-to-end automation for generating and delivering weekly analytics reports from Airtable using **Python**, **Docker**, and **n8n**.

---

## Architecture

* **n8n** — orchestration

  * weekly scheduling
  * HTTP trigger
  * email delivery

* **Python (FastAPI)** — analytics

  * fetch data from Airtable
  * calculate metrics
  * generate CSV

* **Docker** — isolation and deployment

**Flow:**

```
Schedule Trigger (n8n)
        ↓
HTTP Request
        ↓
Python Analytics Service
        ↓
CSV (HTTP response)
        ↓
Email with attachment (n8n)
```

---

## Weekly Report Metrics

* New requests (last 7 days)
* Completed requests (last 7 days)
* Average processing time (Created → Completed)
* Completion rate (%)
* Top 3 consultants by completed requests

---

## API

```
POST /run-weekly-report
```

Returns a CSV file via HTTP response (`text/csv`).

---

## n8n Workflow

1. Schedule Trigger (weekly, UTC)
2. HTTP Request (response format: File)
3. Email node (CSV as attachment)

n8n handles orchestration and delivery, Python handles business logic only.

---

## Docker Setup

* Python service runs in a standalone container
* Communication via Docker network using container names
* No public ports exposed for the Python service

---

## Configuration

All configuration is provided via environment variables:

```bash
AIRTABLE_API_KEY=pat_xxx
AIRTABLE_BASE_ID=app_xxx
AIRTABLE_TABLE_NAME=Requests
REPORT_DAYS=7
TIMEZONE=UTC
```

Secrets are not stored in the repository.

---

## Deployment

```bash
git pull
docker build -t airtable-analytics .
docker stop airtable-analytics && docker rm airtable-analytics
docker run -d \
  --name airtable-analytics \
  --network automation_net \
  -e AIRTABLE_API_KEY=*** \
  -e AIRTABLE_BASE_ID=*** \
  -e AIRTABLE_TABLE_NAME=Requests \
  -e REPORT_DAYS=7 \
  -e TIMEZONE=UTC \
  airtable-analytics
```



