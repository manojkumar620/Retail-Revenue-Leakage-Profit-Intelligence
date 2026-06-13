CREATE DATABASE IF NOT EXISTS retail_profit_intelligence;
USE retail_profit_intelligence;

CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    city VARCHAR(50),
    segment VARCHAR(30),
    join_date DATE
);

CREATE TABLE dim_product (
    product_id INT PRIMARY KEY,
    category VARCHAR(50),
    cost_price DECIMAL(10,2),
    brand VARCHAR(50)
);

CREATE TABLE dim_store (
    store_id INT PRIMARY KEY,
    location VARCHAR(50)
);

CREATE TABLE dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE,
    day INT,
    month INT,
    year INT
);

CREATE TABLE fact_sales (
    order_id INT,
    customer_id INT,
    product_id INT,
    store_id INT,
    date_key INT,
    quantity INT,
    selling_price DECIMAL(10,2),
    discount_amount DECIMAL(10,2),
    coupon_amount DECIMAL(10,2),
    return_flag INT,
    net_profit DECIMAL(10,2),
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY (store_id) REFERENCES dim_store(store_id),
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
);

CREATE INDEX idx_sales_profit ON fact_sales(net_profit);
CREATE INDEX idx_sales_customer ON fact_sales(customer_id);