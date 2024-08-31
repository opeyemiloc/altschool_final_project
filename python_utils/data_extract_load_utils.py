from postgres_extraction_utils import PostgresDataExtraction
from bigquery_ops_utils import BigQueryUtils
from project_constants import SCHEMA_NAME

class DataPipeline:
    def __init__(self):
        self.data_extraction = PostgresDataExtraction()
        self.bigquery_utils = BigQueryUtils()

    # Extract data from PostgreSQL
    def extract_data(self):
        self.data = self.data_extraction.extract_data_from_schema(SCHEMA_NAME)

    # Print table names of available DataFrames
    def print_table_names(self):
        if not self.data:
            print("No data available.")
            return
        print("tables available:")
        for table_name in self.data.keys():
            print(f"- {table_name}")

    # Create BigQuery dataset
    def create_bigquery_dataset(self):
        self.dataset = self.bigquery_utils.create_bigquery_dataset()
        if self.dataset:
            print(f"Dataset '{self.dataset.dataset_id}' created successfully.")
        else:
            print("Dataset already exists or could not be created.")

    # List all datasets in the project
    def list_datasets(self):
        print("\nDatasets in the project:")
        datasets = self.bigquery_utils.bigquery_client.list_datasets()
        for dataset in datasets:
            print(f"- {dataset.dataset_id}")

    # Load a specific table's DataFrame into BigQuery
    def load_data_to_bigquery(self, index):
        if not self.data:
            print("No data available.")
            return

        # Ensure the index is within the range of the dictionary keys
        table_names = list(self.data.keys())
        if index < 0 or index >= len(table_names):
            raise IndexError("Index out of range for the DataFrame list.")

        # Get the table name and DataFrame
        table_name = table_names[index]
        df = self.data[table_name]

        # Load the data into BigQuery
        self.bigquery_utils.load_data_to_bigquery(table_name=table_name, dataframe=df)
        print(f"Loaded data into table '{table_name}' in BigQuery.")

    # Load all DataFrames into BigQuery
    def load_all_data_to_bigquery(self):
        if not self.data:
            print("No data available.")
            return

        for table_name, df in self.data.items():
            # Load the data into BigQuery
            self.bigquery_utils.load_data_to_bigquery(table_name=table_name, dataframe=df)
            print(f"Loaded data into table '{table_name}' in BigQuery.")
