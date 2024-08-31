{{ config(materialized='table') }}

SELECT
p.product_id,pct.product_category_name_english
    p.product_id,
    pct.product_category_name_english,
FROM {{ source('flimsy_dataset_alt', 'products') }} p
JOIN {{ source('flimsy_dataset_alt', 'product_category_name_translation') }} pct
ON p.product_category_name = pct.product_category_name

