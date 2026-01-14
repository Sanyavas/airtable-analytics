# Airtable Analytics

Weekly analytics report for client requests stored in Airtable.

## Features
- Fetch data from Airtable
- Generate weekly operational metrics
- Export report to file

## Tech stack
- Python 3
- Airtable REST API

## Scheduling (n8n)

The weekly analytics report is executed via n8n.

A Cron node triggers the workflow once per week and runs the Python script
using an Execute Command node.

n8n is responsible for scheduling, retries and orchestration,
while Python handles analytics and report generation.
