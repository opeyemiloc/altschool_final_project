from python_utils.cred_manager_utils import CredManager
import psycopg2


class PostgresConnection:
    def __init__(self):
        self.credentials_manager = CredManager()
        self.db_params = self.credentials_manager.get_postgres_credentials()
        self.conn = None
        self.cursor = None

    def connect(self):
        """Establish a connection to the PostgreSQL database."""
        self.conn = psycopg2.connect(**self.db_params)
        self.cursor = self.conn.cursor()
        print("Connected to PostgreSQL")

    def close(self):
        """Close the cursor and connection."""
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()
        print("PostgreSQL connection closed")
