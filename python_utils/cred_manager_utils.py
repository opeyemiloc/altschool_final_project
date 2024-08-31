import os
from dotenv import load_dotenv

class CredManager:
    def __init__(self):
        # Load environment variables
        load_dotenv()

    def get_postgres_credentials(self):
        """Retrieve PostgreSQL database credentials."""
        return {
            'dbname': os.getenv('POSTGRES_DBNAME'),
            'user': os.getenv('POSTGRES_USER'),
            'password': os.getenv('POSTGRES_PASSWORD'),
            'host': os.getenv('POSTGRES_HOST'),
            'port': os.getenv('POSTGRES_PORT', '5432')  # Default port is 5432
        }

    def get_bigquery_credentials(self):
        """Retrieve BigQuery credentials (path to the JSON key file)."""
        return os.getenv('GOOGLE_APPLICATION_CREDENTIALS')