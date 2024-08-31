{{ config(materialized='table') }}

SELECT
    AVG(delivery_time_days) AS avg_delivery_time
FROM {{ ref('int_avg_delivery_time') }}
