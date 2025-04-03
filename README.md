# FinanceFlow

🚀 End-to-End ETL System for Synthetic Financial Transactions

## ✅ Tech Stack
- **Apache Airflow** – for orchestration
- **Python** – for ETL scripts
- **AWS Lambda** – serverless transformation
- **Snowflake** – cloud data warehouse
- **Great Expectations** – for data validation
- **Logging** – Python's built-in logging module

## 📁 Project Structure

```
FinanceFlow/
├── dags/
│   └── financeflow_etl.py
├── lambda/
│   └── transform_function.py
├── scripts/
│   └── generate_data.py
├── validation/
│   └── expectations_suite.py
├── utils/
│   └── logger.py
├── requirements.txt
└── README.md
```

## ▶️ How to Run

1. Start Airflow:
   ```bash
   airflow standalone
   ```

2. Deploy Lambda function manually or via AWS CLI:
   ```bash
   aws lambda create-function ...
   ```

3. Add your Snowflake credentials to Airflow connections.

4. Trigger the DAG in Airflow UI.
