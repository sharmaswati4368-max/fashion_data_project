import mysql.connector
import pandas as pd

# Step 1: Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='hanak@109',  # Add password here if you use one
    database='fashion_retail_db1'
)

# Step 2: Get table names
cursor = conn.cursor()
cursor.execute("SHOW TABLES")
tables = [table[0] for table in cursor.fetchall()]

# Step 3: Fetch each table, clean it, and store in dictionary
dfs = {}
for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", conn)
    df_cleaned = df.drop_duplicates()  # Remove duplicates
    dfs[table] = df_cleaned

# Step 4: Export each table to a separate sheet in Excel
excel_writer = pd.ExcelWriter('final_retail_data.xlsx', engine='xlsxwriter')

for sheet_name, data in dfs.items():
    # Limit sheet name to 31 characters (Excel max limit)
    safe_sheet_name = sheet_name[:31]
    data.to_excel(excel_writer, sheet_name=safe_sheet_name, index=False)

excel_writer.close()

# Step 5: Done
print("✅ All data exported to 'final_retail_data.xlsx' successfully.")

# Close connection
conn.close()
import pandas as pd

# Load Excel file
file_path = 'final_retail_data.xlsx'
xls = pd.ExcelFile(file_path)

# Load sheets
customers = pd.read_excel(xls, 'customers')
orders = pd.read_excel(xls, 'orders')
products = pd.read_excel(xls, 'products')
order_items = pd.read_excel(xls, 'order_items')
returns = pd.read_excel(xls, 'returns')
inventory = pd.read_excel(xls, 'inventory')
# Merge orders with customers
orders_customers = pd.merge(orders, customers, on='customer_id', how='left')

# Merge order_items with products
items_products = pd.merge(order_items, products, on='product_id', how='left')

# Final full data: merge both above
full_data = pd.merge(orders_customers, items_products, on='order_id', how='left')

# Preview
print("Final Combined Data:")
print(full_data.head())
# Remove duplicates
full_data.drop_duplicates(inplace=True)

# Check for missing values
print("Missing values:\n", full_data.isnull().sum())

# Fill any missing discounts or prices with 0 (if needed)
full_data['discount'] = full_data['discount'].fillna(0)
full_data['price'] = full_data['price'].fillna(0)
full_data['quantity'] = full_data['quantity'].fillna(1)

# Create total_price
full_data['total_price'] = (full_data['price'] - full_data['discount']) * full_data['quantity']

# Check data again
print("Cleaned and enriched data preview:\n", full_data[['customer_id', 'order_id', 'product_name', 'price', 'discount', 'quantity', 'total_price']].head())
# Export to CSV
full_data.to_csv('clean_fashion_data.csv', index=False)

print("✅ Cleaned data exported to 'clean_fashion_data.csv'")