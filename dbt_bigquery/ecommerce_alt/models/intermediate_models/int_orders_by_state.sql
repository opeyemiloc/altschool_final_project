{{ config(materialized='table') }}

SELECT
    c.customer_state,
    COUNT(o.order_id) AS total_orders
FROM {{ ref('stg_orders') }} o
JOIN {{ source('flimsy_dataset_alt', 'customers') }} c
ON o.customer_id = c.customer_id
GROUP BY c.customer_state
ORDER BY total_orders DESC
