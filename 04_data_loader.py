import mysql.connector
import random

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="manoj123",
        database="retail_profit_intelligence"
    )
    cursor = conn.cursor()
    print("[LOG] Connected successfully")
except mysql.connector.Error as err:
    print(f"[ERROR] Connection failed: {err}")
    exit()

cursor.executemany("INSERT IGNORE INTO dim_customer VALUES (%s, %s, %s, %s)", [
    (1001, 'Chennai', 'PREMIUM', '2023-01-10'),
    (1002, 'Mumbai', 'REGULAR', '2024-05-15'),
    (1003, 'Bangalore', 'PREMIUM', '2025-11-20')
])

cursor.executemany("INSERT IGNORE INTO dim_product VALUES (%s, %s, %s, %s)", [
    (501, 'Electronics', 25000.00, 'BrandAlpha'),
    (502, 'Apparel', 800.00, 'BrandBeta'),
    (503, 'Home Appliances', 12000.00, 'BrandGamma')
])

cursor.executemany("INSERT IGNORE INTO dim_store VALUES (%s, %s)", [
    (10, 'T-Nagar Metro Node'),
    (20, 'Velachery Micro Node')
])

cursor.executemany("INSERT IGNORE INTO dim_date VALUES (%s, %s, %s, %s, %s)", [
    (20260610, '2026-06-10', 10, 6, 2026)
])
conn.commit()

sales_records = []
for i in range(20001, 20301):
    order_id = i
    c_id = random.choice([1001, 1002, 1003])
    p_id = random.choices([501, 502, 503], weights=[50, 30, 20], k=1)[0]
    s_id = random.choice([10, 20])
    d_key = 20260610
    qty = random.randint(1, 3)

    if p_id == 501:
        cost = 25000.00
        discount = 4000.00
        coupon = 5000.00
        selling_price = (cost + 5000.00) - (discount + coupon)
        return_flag = 1 if random.random() > 0.7 else 0
        net_profit = (selling_price * qty) - (cost * qty) if return_flag == 0 else 0
    else:
        cost = 800.00 if p_id == 502 else 12000.00
        discount = random.randint(50, 200)
        coupon = 0.00
        selling_price = (cost + 400.00) - discount
        return_flag = 0
        net_profit = (selling_price * qty) - (cost * qty)

    sales_records.append((order_id, c_id, p_id, s_id, d_key, qty, selling_price, discount, coupon, return_flag, net_profit))

cursor.executemany("""INSERT IGNORE INTO fact_sales VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", sales_records)
conn.commit()

print("[SUCCESS] Data inserted Successfully!!")
cursor.close()
conn.close()