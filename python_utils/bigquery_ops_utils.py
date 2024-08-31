from cred_manager_utils import CredManager
from google.cloud import bigquery
from project_constants import GCP_PROJECT_ID, BIGQUERY_DATASET, LOCATION  # Import constants

class BigQueryUtils:
    def __init__(self):
        self.credentials_manager = CredManager()
        self.project_id = GCP_PROJECT_ID  # Use constant here
        self.bigquery_client = bigquery.Client.from_service_account_json(
            self.credentials_manager.get_bigquery_credentials()
        )

    def delete_all_tables_in_dataset(self):
        dataset_name = BIGQUERY_DATASET  # Use the default dataset name
        dataset_id = f"{self.project_id}.{dataset_name}"
        
        tables = self.bigquery_client.list_tables(dataset_id)
        for table in tables:
            table_id = f"{dataset_id}.{table.table_id}"
            self.bigquery_client.delete_table(table_id)
            print(f"Deleted table '{table_id}'")

    def create_bigquery_dataset(self):
        dataset_name = BIGQUERY_DATASET  # Default to constant
        dataset_id = f"{self.project_id}.{dataset_name}"
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = LOCATION

        # List existing datasets to check if the dataset already exists
        existing_datasets = [ds.dataset_id for ds in self.bigquery_client.list_datasets()]
        
        if dataset_id in existing_datasets:
            print(f"Dataset '{dataset_id}' already exists.")
            # Delete all tables in the existing dataset
            self.delete_all_tables_in_dataset()
            return self.bigquery_client.get_dataset(dataset_id)  # Return the existing dataset

        # Create the dataset if it does not exist
        try:
            dataset = self.bigquery_client.create_dataset(dataset, timeout=30)
            print(f"Created dataset {dataset_id}")
        except Exception as e:
            print(f"Failed to create dataset {dataset_id}. Error: {str(e)}")
            return None

        return dataset

    def load_data_to_bigquery(self, table_name, dataframe):
        # Configuration for the BigQuery load job
        job_config = bigquery.LoadJobConfig(
            write_disposition="WRITE_TRUNCATE"  # Overwrite the table if it exists
        )

        # Load the DataFrame into BigQuery
        table_id = f"{self.project_id}.{BIGQUERY_DATASET}.{table_name}"
        load_job = self.bigquery_client.load_table_from_dataframe(
            dataframe=dataframe,
            destination=table_id,
            job_config=job_config
        )

        load_job.result()  # Wait for the load job to complete

        print(f"Loaded data into table '{table_id}'")
