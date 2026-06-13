import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:manoj123@localhost/retail_profit_intelligence")

query = """
    SELECT p.category, f.discount_amount, f.coupon_amount, f.net_profit 
    FROM fact_sales f 
    JOIN dim_product p ON f.product_id = p.product_id
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='discount_amount', y='net_profit', hue='category', style='category', s=100)

plt.title('Impact of Discounts on Net Profit by Category', fontsize=14, fontweight='bold')
plt.xlabel('Discount Amount (INR)', fontsize=12)
plt.ylabel('Net Profit (INR)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

plt.savefig('profit_impact_chart.png')
print("[SUCCESS] Chart saved as 'profit_impact_chart.png'!")

plt.show()