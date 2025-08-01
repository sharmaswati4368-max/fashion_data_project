import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hanak@109",  # change this
    database="ecommerce"
)

# Load data
query = "SELECT *, quantity * price_per_unit AS total_amount FROM orders"
df = pd.read_sql(query, conn)

print(df.head())
import mysql.connector
import pandas as pd

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',       # or '127.0.0.1'
    user='root',
    password='hanak@109',
    database='ecommerce'
)

# Load data from 'orders' table into DataFrame
query = "SELECT * FROM orders"
df = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Display first few rows
print("Data Preview:")
print(df.head())
import pandas as pd
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='hanak@109',  # replace with actual
    database='ecommerce'
)

# Load the table into a DataFrame
query = "SELECT * FROM orders"
df = pd.read_sql(query, conn)
conn.close()

# Basic overview
print(df.head())           # First 5 rows
print(df.info())           # Column types and nulls
print(df.describe())       # Numeric summary

# Check for missing values
print(df.isnull().sum())

# Check for duplicates
print("Duplicates:", df.duplicated().sum())

# Convert date column if needed
df['order_date'] = pd.to_datetime(df['order_date'])  # update column name if different

# Drop duplicates (if any)
df.drop_duplicates(inplace=True)
print(df.columns)
total_sales = df['sales'].sum()
print("Total Revenue (₹):", total_sales)
top_products = df.groupby('product_name')['sales'].sum().sort_values(ascending=False).head(5)
print("Top 5 Products by Revenue:\n", top_products)
top_customers = df.groupby('customer_name')['sales'].sum().sort_values(ascending=False).head(5)
print("Top 5 Customers by Spend:\n", top_customers)
df['order_month'] = df['order_date'].dt.to_period('M').astype(str)

monthly_sales = df.groupby('order_month')['sales'].sum()
print("Monthly Sales:\n", monthly_sales)
import pandas as pd

import mysql.connector
from mysql.connector import Error







# Check columns
print(df.columns.tolist())

# Assuming correct column name is 'order_date'
df['order_date'] = pd.to_datetime(df['order_date'])
df['Month'] = df['order_date'].dt.month_name()

df['Sales'] = df['quantity'] * df['price_per_unit']
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

# Export to Excel
with pd.ExcelWriter("ecommerce_report.xlsx") as writer:
    monthly_sales.to_excel(writer, sheet_name="Monthly Sales", index=False)

print("✅ Excel file created successfully!")
# Check columns

