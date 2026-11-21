import pandas as pd

print("=======================================")
print(" E-COMMERCE SALES DATA ANALYSIS")
print("=======================================")

# Reading CSV File
df = pd.read_csv("ecommerce_sales_data.csv")

# Basic Information
print("\n========== FIRST 5 ORDERS ==========")
print(df.head().to_string(index=False))

print("\nTotal Orders:", len(df))

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Sales Analysis
print("\n========== SALES ANALYSIS ==========")
print("Total Sales: Rs.", df["Total_Amount"].sum())
print("Average Order Value: Rs.", round(df["Total_Amount"].mean(), 2))
print("Maximum Order Value: Rs.", df["Total_Amount"].max())
print("Minimum Order Value: Rs.", df["Total_Amount"].min())

# Highest Order
print("\n========== HIGHEST ORDER ==========")
highest = df.loc[df["Total_Amount"].idxmax()]
print(highest)

# Top 5 Best Selling Products (by quantity)
print("\n========== TOP 5 BEST SELLING PRODUCTS ==========")
top_products = df.groupby("Product_Name")["Quantity"].sum()
print(top_products.sort_values(ascending=False).head(5))

# Revenue by Product
print("\n========== PRODUCT-WISE REVENUE ==========")
product_sales = df.groupby("Product_Name")["Total_Amount"].sum()
print(product_sales.sort_values(ascending=False))

# Category Analysis
print("\n========== CATEGORY-WISE SALES ==========")
category_sales = df.groupby("Category")["Total_Amount"].sum()
print(category_sales.sort_values(ascending=False))

# City Analysis
print("\n========== CITY-WISE SALES ==========")
city_sales = df.groupby("City")["Total_Amount"].sum()
print(city_sales.sort_values(ascending=False))

# Payment Analysis
print("\n========== PAYMENT METHOD ANALYSIS ==========")
print(df["Payment_Method"].value_counts())

# Monthly Sales (in calendar order)
print("\n========== MONTHLY SALES ==========")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Month"] = df["Order_Date"].dt.month
monthly_sales = df.groupby("Month")["Total_Amount"].sum()
monthly_sales.index = pd.to_datetime(monthly_sales.index, format="%m").month_name()
print(monthly_sales)

# Final Conclusion
print("\n========== FINAL CONCLUSION ==========")
print("Top Category:", category_sales.idxmax())
print("Top City:", city_sales.idxmax())
print("Most Popular Payment Method:", df["Payment_Method"].mode()[0])
print("Best Month:", monthly_sales.idxmax())

print("\nAnalysis Completed Successfully!")
