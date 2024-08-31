# Project Overview

This project involves setting up a PostgreSQL database to serve as the source data for an ETL process. The dataset used is the Brazilian E-Commerce dataset, which is ingested into PostgreSQL using Docker and Docker Compose.

## Project Steps

### Step 1: Data Ingestion into PostgreSQL

1. **Download the Dataset**:  
   Download the Brazilian E-Commerce dataset from Kaggle.

2. **Setup PostgreSQL Database**:  
   Set up PostgreSQL using Docker & Docker Compose. A new database named `ecommerce` will be created.

3. **Create Tables**:  
   Use the provided `init.sql` script to create tables in the PostgreSQL database corresponding to each CSV file in the dataset.

4. **Ingest Data**:  
   Ingest the data into the tables using the `init.sql` script. This will populate the PostgreSQL database with the source data needed for the subsequent ETL process.

## How to Spin Up the Server

Simply run `docker-compose up` in the project root folder. This will start the PostgreSQL service, and you can connect to the database using the following credentials:



## Managing State File

When you start Docker Compose, a `pg_data` folder will be created in your project root folder. If you ever want to clear state information, simply stop the Docker Compose service, delete the folder, and restart the service. This will allow Docker to recreate PostgreSQL from scratch and reload your data from the `init.sql` script.
