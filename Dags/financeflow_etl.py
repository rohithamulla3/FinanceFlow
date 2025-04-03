from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.generate_data import generate_synthetic_data
from validation.expectations_suite import validate_data
from lambda.transform_function import lambda_transform
from utils.logger import get_logger

logger = get_logger("FinanceFlow")

def load_to_snowflake():
    logger.info("Loading validated data to Snowflake...")
    print("Data loaded to Snowflake")

with DAG(dag_id='financeflow_etl',
         start_date=datetime(2024, 1, 1),
         schedule_interval='@daily',
         catchup=False) as dag:

    task_generate = PythonOperator(
        task_id='generate_data',
        python_callable=generate_synthetic_data
    )

    task_validate = PythonOperator(
        task_id='validate_data',
        python_callable=validate_data
    )

    task_transform = PythonOperator(
        task_id='transform_data',
        python_callable=lambda_transform
    )

    task_load = PythonOperator(
        task_id='load_to_snowflake',
        python_callable=load_to_snowflake
    )

    task_generate >> task_validate >> task_transform >> task_load
