{{ config(materialized='table') }}

WITH order_sales AS (
    SELECT
        oi.product_id,
        SUM(oi.price) AS total_sales
    FROM {{ ref('stg_orders') }} o
    JOIN {{ source('flimsy_dataset_alt', 'order_items') }} oi
    ON o.order_id = oi.order_id
    WHERE o.order_status = 'delivered'
    GROUP BY oi.product_id
)

SELECT
    p.product_category_name_english AS category,
    SUM(os.total_sales) AS category_sales
FROM order_sales os
JOIN {{ ref('stg_products') }} p
ON os.product_id = p.product_id
GROUP BY p.product_category_name_english
ORDER BY category_sales DESC
