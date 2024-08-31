{{ config(materialized='table') }}

SELECT
    category,
    category_sales
FROM {{ ref('int_sales_by_category') }}
