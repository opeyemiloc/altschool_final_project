# Brazilian E-Commerce Data ETL Project

## Overview

This project involves building an end-to-end ETL (Extract, Transform, Load) pipeline to process Brazilian e-commerce data. The pipeline uses PostgreSQL, Docker, Docker Compose, Apache Airflow, dbt, and Google BigQuery for data ingestion, transformation, and analysis.

## Prerequisites

- **Docker** and **Docker Compose**: For containerization and orchestration.
- **Python 3.x**: For scripting and dbt.
- **Google Cloud Platform (GCP)** account with BigQuery access.
- **Kaggle** account: To download the dataset.
- **BI Tools**: For data visualization and analytics (e.g., Tableau, Looker).

## Requirements

- PostgreSQL for data storage and initial processing.
- Apache Airflow for orchestrating the ETL pipeline.
- Google BigQuery for data warehousing.
- dbt for transforming and modeling data.

## Setup Instructions

### 1. Create a Virtual Environment

1. **Set Up Virtual Environment**

   Create a virtual environment to manage Python dependencies:

   ```bash
   python -m venv venv
   
### 2. Data Ingestion into PostgreSQL

**Download the Dataset**

Obtain the Brazilian E-Commerce dataset from Kaggle and place the CSV files in the project’s `data` directory.

**Setup PostgreSQL with Docker**

Use Docker and Docker Compose to create and configure a PostgreSQL container. Ensure the database is named `ecommerce`.

**Create Tables and Ingest Data**

Define the schema and load data into PostgreSQL tables. This can be done using custom Python ETL scripts or an `init.sql` script executed when setting up the PostgreSQL container.

### 3. Setting Up Apache Airflow

**Install Airflow with Docker**

Add Airflow to your Docker Compose configuration to manage ETL workflows.

**Create DAGs**

Define Directed Acyclic Graphs (DAGs) in Airflow to orchestrate the ETL process. The DAGs should handle tasks for extracting data from PostgreSQL and loading it into BigQuery.

### 4. Loading Data from PostgreSQL to BigQuery

**Setup BigQuery**

Create a project and dataset in Google Cloud Platform for storing the e-commerce data.

**Load Data**

Configure Airflow to transfer data from PostgreSQL to BigQuery, applying any necessary transformations.
### 5. Transforming and Modeling Data with dbt

**Setup dbt**

Install dbt and initialize a new dbt project.

**Configure dbt**

Configure dbt to connect to your BigQuery dataset.

**Create Models**

Create dbt models to transform the raw data into a clean and usable format. This involves defining staging, intermediate, and final models to answer the analytical questions.

### 6. Connecting Power BI for Analytics

**Connect Power BI to BigQuery**

Use Power BI to connect to your BigQuery dataset. This will allow you to create visualizations and perform analytics based on the transformed data.
