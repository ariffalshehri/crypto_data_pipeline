from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'admin',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='crypto_etl_pipeline',
    default_args=default_args,
    start_date=datetime(2026, 3, 18),
    schedule_interval='@daily',
    catchup=False,
    description='ETL pipeline for cryptocurrency data'
) as dag:

    extract_task = BashOperator(
        task_id='extract_data',
        bash_command='python /opt/airflow/scripts/extract.py'
    )

    load_task = BashOperator(
        task_id='load_data',
        bash_command='python /opt/airflow/scripts/load.py'
    )

    transform_task = BashOperator(
        task_id='transform_data',
        bash_command='python /opt/airflow/scripts/transform.py'
    )

    extract_task >> load_task >> transform_task