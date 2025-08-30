import pandas as pd
import mysql.connector
from datetime import datetime

# Step 1: Ingest raw sales data
df = pd.read_csv("data/raw_sales_data.csv")

# Step 2: Clean & Transform
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# Save transformed dataset
df.to_csv("data/transformed_sales.csv", index=False)

# Step 3: Load into MySQL warehouse
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="sales_db"
)
cursor = conn.cursor()

# Create fact & dimension tables
cursor.execute(open("scripts/db_setup.sql", "r").read())

# Insert data into fact table
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO fact_sales (OrderID, CustomerID, ProductID, OrderDate, Revenue, Quantity)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (row['OrderID'], row['CustomerID'], row['ProductID'],
          row['OrderDate'], row['Revenue'], row['Quantity']))

conn.commit()
cursor.close()
conn.close()

print("✅ ETL Pipeline completed and data loaded into MySQL.")
