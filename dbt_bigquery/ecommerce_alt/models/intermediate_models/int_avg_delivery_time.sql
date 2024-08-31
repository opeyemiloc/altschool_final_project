{{ config(materialized='table') }}

SELECT
    o.order_id,
    o.customer_id,
    DATEDIFF(o.order_delivered_customer_date, o.order_purchase_timestamp) AS delivery_time_days
FROM {{ ref('stg_orders') }} o
WHERE o.order_status = 'delivered'
