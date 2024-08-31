import pandas as pd
#from io import StringIO
from postgres_connection_utils import PostgresConnection


class PostgresDataExtraction:
    def __init__(self):
        self.pg_connection = PostgresConnection()

    def extract_data_from_schema(self, schema_name):
        """
        Extract data from all tables within a schema and store it in a dictionary as DataFrames.
        
        :param schema_name: The schema name to query.
        :return: A dictionary where keys are table names and values are DataFrames.
        """
        self.pg_connection.connect()
        data = {}

        # Retrieve all tables in the specified schema
        query = f"""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = '{schema_name.lower()}'
        """
        self.pg_connection.cursor.execute(query)
        tables = self.pg_connection.cursor.fetchall()
        
        for (table,) in tables:
            table_name = table
            query = f"SELECT * FROM {schema_name}.{table_name};"
            self.pg_connection.cursor.execute(query)
            columns = [desc[0] for desc in self.pg_connection.cursor.description]
            rows = self.pg_connection.cursor.fetchall()
            # Convert rows to DataFrame
            df = pd.DataFrame(rows, columns=columns)
            data[table_name] = df

        self.pg_connection.close()
        return data

    def compute_table_details(self, data):
        """
        Compute and store details of each table such as row counts, column counts, and column names.
        
        :param data: A dictionary where keys are table names and values are DataFrames.
        :return: A dictionary where keys are table names and values are dictionaries with row counts, column counts, and column names.
        """
        table_details = {}
        for table_name, df in data.items():
            table_details[table_name] = {
                'row_count': len(df),
                'column_count': len(df.columns),
                'column_names': list(df.columns)
            }

        return table_details

  