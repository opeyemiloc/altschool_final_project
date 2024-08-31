-- {{ config(materialized='table') }}

-- SELECT
--     customer_state AS state,
--     total_orders
-- FROM {{ ref('int_orders_by_state') }}
