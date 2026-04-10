import pandas as pd

# 📌 STEP 1: Load dataset (your path)
df = pd.read_csv(r"C:\Users\Dell\Downloads\sales_data.csv")

# 📌 STEP 2: Clean column names (VERY IMPORTANT)
df.columns = df.columns.str.strip().str.lower()

print("📊 COLUMN NAMES:", df.columns)

# 📌 STEP 3: Rename columns if needed (auto-fix common cases)
if 'qty' in df.columns:
    df.rename(columns={'qty': 'quantity'}, inplace=True)

if 'product_name' in df.columns:
    df.rename(columns={'product_name': 'product'}, inplace=True)

# 📌 STEP 4: Display first rows
print("\n📊 FIRST 5 ROWS:")
print(df.head())

# 📌 STEP 5: Data info
print("\n📊 DATA INFO:")
print(df.info())

print("\n📊 SHAPE:", df.shape)

# 📌 STEP 6: Handle missing values
if 'quantity' in df.columns:
    df['quantity'] = df['quantity'].fillna(df['quantity'].mean())
else:
    print("❌ 'quantity' column not found!")

# 📌 STEP 7: Remove duplicates
df = df.drop_duplicates()

# 📌 STEP 8: Create Total Sales column
df['total_sales'] = df['quantity'] * df['price']

# 📌 STEP 9: Analysis
total_revenue = df['total_sales'].sum()
average_sales = df['total_sales'].mean()
highest_sale = df['total_sales'].max()

# Best selling product
best_product = df.groupby('product')['total_sales'].sum().idxmax()

# 📊 STEP 10: Report
print("\n📊 SALES ANALYSIS REPORT")
print("=" * 40)

print(f"💰 Total Revenue: ₹{total_revenue:,.2f}")
print(f"📈 Average Sale: ₹{average_sales:,.2f}")
print(f"🏆 Highest Sale: ₹{highest_sale:,.2f}")
print(f"🔥 Best Selling Product: {best_product}")

print("=" * 40)

# 📌 STEP 11: Save cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)

print("\n✅ Cleaned data saved as 'cleaned_sales_data.csv'")