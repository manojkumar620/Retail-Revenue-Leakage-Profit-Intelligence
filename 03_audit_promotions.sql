USE retail_profit_intelligence;

SELECT 
    f.order_id,
    c.city,
    p.category,
    f.selling_price,
    f.discount_amount,
    f.coupon_amount,
    f.net_profit,
    CASE 
        WHEN f.coupon_amount > 0 AND f.discount_amount > 0 THEN 'ALERT: Stacked Promotion'
        ELSE 'Normal Clearance'
    END AS operational_audit_status
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id
JOIN dim_product p ON f.product_id = p.product_id
WHERE p.category = 'Electronics'
ORDER BY f.net_profit ASC;