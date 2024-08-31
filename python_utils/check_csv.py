from data_extract_load_utils import DataPipeline
# Initialize DataPipeline class
pipeline = DataPipeline()

# Extract data from PostgreSQL and convert to CSV format
pipeline.extract_and_convert_data()

# Print names of tables for verification
pipeline.print_table_names()