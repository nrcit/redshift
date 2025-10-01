# Redshift

## Overview
This repo contains:
- SQL scripts for schema and analytics
- Python script to execute SQL on AWS Redshift
- GitHub Actions workflows for SQL execution

## Usage
### Run SQL
Trigger `Run SQL on Redshift` workflow manually with:
- `branch`: branch name
- `sql_path`: path to a file or folder (`sql/init`, `sql/analytics/daily_report.sql`, etc.)
- `execution_order`: optional comma-separated list

## Local Testing
```bash
pip install -r requirements.txt
python scripts/run_sql.py
