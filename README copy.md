# Sales Analytics Pipeline

Automated sales data validation and reporting pipeline using GitHub Actions.

## Project Structure

```
.
├── .github/
│   └── workflows/
│       ├── build_test.yml      # Runs on every push & PR
│       └── build_deploy.yml    # Runs on push to main
├── data/
│   └── sales.csv               # Sales data
├── reports/
│   └── index.html              # Generated web report
├── scripts/
│   ├── validate.py             # Validates sales.csv
│   └── reports.py              # Generates report.txt
└── README.md
```

## Workflows

### Build_Test
- Triggers on every `push` and `pull_request`
- Validates `data/sales.csv` using `scripts/validate.py`
- Checks required columns and null values

### Build_Deploy
- Triggers on push to `main` branch only
- Generates analytics report via `scripts/reports.py`
- Uploads report as GitHub Actions artifact

## Running Locally

```bash
pip install pandas
python scripts/validate.py
python scripts/reports.py
```
