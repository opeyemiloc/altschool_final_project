from python_utils.data_extract_load_utils import DataPipeline
# Initialize DataPipeline class
pipeline = DataPipeline()

# Extract data from PostgreSQL and convert to CSV format
pipeline.extract_data()

# Print names of tables for verification
pipeline.print_table_names()

# Attempt to create the dataset in BigQuery
pipeline.create_bigquery_dataset()

# Optional: List all datasets in the project to verify creation
pipeline.list_datasets()

# Load CSV into BigQuery as a table by index
pipeline.load_all_data_to_bigquery()

