#importing libraries
import sys
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from python_utils.data_extract_load_utils import DataPipeline


# Initialize the DataPipeline class
pipeline = DataPipeline()

# Define callable functions for each method
def extract_data():
    pipeline.extract_and_convert_data()

def create_bigquery_dataset():
    pipeline.create_bigquery_dataset()

def load_data_to_bigquery():
    pipeline.load_all_data_to_bigquery()

# Define the default arguments for the DAG
default_args = {
    'start_date': datetime.now(),
    'retries': 1
}

# Define the DAG
with DAG(
    'data_pipeline_dag',
    default_args=default_args,
    description='A simple data pipeline DAG',
    schedule_interval=None,
    catchup=False
) as dag:

    # Define the tasks using PythonOperator
    task_1 = PythonOperator(
        task_id='extract_and_convert_data',
        python_callable=extract_data
    )

    task_2 = PythonOperator(
        task_id='create_bigquery_dataset',
        python_callable=create_bigquery_dataset
    )

    task_3 = PythonOperator(
        task_id='load_data_to_bigquery',
        python_callable=load_data_to_bigquery
    )

    # Set the sequence of tasks
    task_1 >> task_2 >> task_3
