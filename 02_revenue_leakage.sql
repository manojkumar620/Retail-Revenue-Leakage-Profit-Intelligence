USE retail_profit_intelligence;

SELECT 
    p.category,
    SUM(f.quantity * p.cost_price) AS theoretical_gross_revenue,
    SUM(f.net_profit) AS actual_net_profit,
    ROUND(SUM(f.quantity * p.cost_price) - SUM(f.net_profit), 2) AS absolute_revenue_leakage,
    ROUND(SUM(f.discount_amount + f.coupon_amount), 2) AS total_markdown_slippage
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.category;

SELECT 
    s.location,
    p.category,
    ROUND(SUM(f.quantity * p.cost_price) - SUM(f.net_profit), 2) AS absolute_revenue_leakage,
    DENSE_RANK() OVER(PARTITION BY p.category ORDER BY (SUM(f.quantity * p.cost_price) - SUM(f.net_profit)) DESC) AS leakage_rank
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
JOIN dim_store s ON f.store_id = s.store_id
GROUP BY s.location, p.category;