-- Create schema
CREATE SCHEMA IF NOT EXISTS ECOMMERCE;

-- Create and populate customers table
CREATE TABLE IF NOT EXISTS ECOMMERCE.CUSTOMERS
(
    customer_id UUID PRIMARY KEY,
    customer_unique_id UUID NOT NULL,
    customer_zip_code_prefix VARCHAR(20) NOT NULL,
    customer_city VARCHAR(255) NOT NULL,
    customer_state VARCHAR(2) NOT NULL
);

COPY ECOMMERCE.CUSTOMERS (customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state)
FROM '/data/olist_customers_dataset.csv' DELIMITER ',' CSV HEADER;

-- Create and populate geolocation table
CREATE TABLE IF NOT EXISTS ECOMMERCE.GEOLOCATION
(
    geolocation_zip_code_prefix NUMERIC(20) NOT NULL,
    geolocation_latitude NUMERIC(20, 6) NOT NULL,
    geolocation_longitude NUMERIC(20, 6) NOT NULL,
    geolocation_city VARCHAR(255) NOT NULL,
    geolocation_state VARCHAR(2) NOT NULL
);

COPY ECOMMERCE.GEOLOCATION (geolocation_zip_code_prefix, geolocation_latitude, geolocation_longitude, geolocation_city, geolocation_state)
FROM '/data/olist_geolocation_dataset.csv' DELIMITER ',' CSV HEADER;

-- Create and populate orders table
CREATE TABLE IF NOT EXISTS ECOMMERCE.ORDERS
(
    order_id UUID PRIMARY KEY,
    customer_id UUID NOT NULL,
    order_status VARCHAR(50) NOT NULL,
    order_purchase_timestamp TIMESTAMP NOT NULL,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP
);

COPY ECOMMERCE.ORDERS (order_id, customer_id, order_status, order_purchase_timestamp, order_approved_at, order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date)
FROM '/data/olist_orders_dataset.csv' DELIMITER ',' CSV HEADER;

-- Create and populate order items table
CREATE TABLE IF NOT EXISTS ECOMMERCE.ORDER_ITEMS
(
    order_id UUID NOT NULL,
    order_item_id SERIAL,
    product_id UUID NOT NULL,
    seller_id UUID NOT NULL,
    shipping_limit_date TIMESTAMP NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    freight_value NUMERIC(10, 2) NOT NULL
);

COPY ECOMMERCE.ORDER_ITEMS (order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, freight_value)
FROM '/data/olist_order_items_dataset.csv' DELIMITER ',' CSV HEADER;

-- Create and populate order payments table
CREATE TABLE IF NOT EXISTS ECOMMERCE.ORDER_PAYMENTS
(
    order_id UUID NOT NULL,
    payment_sequential INT NOT NULL,
    payment_type VARCHAR(20) NOT NULL,
    payment_installments INT NOT NULL,
    payment_value NUMERIC(10, 2) NOT NULL
);

COPY ECOMMERCE.ORDER_PAYMENTS (order_id, payment_sequential, payment_type, payment_installments, payment_value)
FROM '/data/olist_order_payments_dataset.csv' DELIMITER ',' CSV HEADER;

-- Create and populate orders reviews table
CREATE TABLE IF NOT EXISTS ECOMMERCE.ORDER_REVIEWS
(
    review_id UUID NOT NULL,
    order_id UUID NOT NULL,
    review_score INT NOT NULL,
    review_comment_title TEXT,
    review_comment_message TEXT,
    review_creation_date TIMESTAMP NOT NULL,
    review_answer_timestamp TIMESTAMP NOT NULL
);

COPY ECOMMERCE.ORDER_REVIEWS (review_id, order_id, review_score, review_comment_title, review_comment_message, review_creation_date, review_answer_timestamp)
FROM '/data/olist_order_reviews_dataset.csv' DELIMITER ',' CSV HEADER;

-- Create and populate products table
CREATE TABLE IF NOT EXISTS ECOMMERCE.PRODUCTS
(
    product_id UUID PRIMARY KEY,
    product_category_name VARCHAR(255),
    product_name_length INT,
    product_description_length INT,
    product_photos_qty INT,
    product_weight_g INT,
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);

COPY ECOMMERCE.PRODUCTS (product_id, product_category_name, product_name_length, product_description_length, product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm)
FROM '/data/olist_products_dataset.csv' DELIMITER ',' CSV HEADER;

-- Create and populate sellers table
CREATE TABLE IF NOT EXISTS ECOMMERCE.SELLERS
(
    seller_id UUID PRIMARY KEY,
    seller_zip_code_prefix VARCHAR(20) NOT NULL,
    seller_city VARCHAR(255) NOT NULL,
    seller_state VARCHAR(2) NOT NULL
);

COPY ECOMMERCE.SELLERS (seller_id, seller_zip_code_prefix, seller_city, seller_state)
FROM '/data/olist_sellers_dataset.csv' DELIMITER ',' CSV HEADER;

-- Create and populate product category name translation table
CREATE TABLE IF NOT EXISTS ECOMMERCE.PRODUCT_CATEGORY_NAME_TRANSLATION
(
    product_category_name VARCHAR(255) PRIMARY KEY,
    product_category_name_english VARCHAR(255) NOT NULL
);

COPY ECOMMERCE.PRODUCT_CATEGORY_NAME_TRANSLATION (product_category_name, product_category_name_english)
FROM '/data/product_category_name_translation.csv' DELIMITER ',' CSV HEADER;
