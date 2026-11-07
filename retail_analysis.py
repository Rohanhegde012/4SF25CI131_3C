# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV dataset
df = pd.read_csv("retail_sales_practice_dataset.csv")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())


# Display number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Display data types
print("\nData Types:")
print(df.dtypes)

# Convert order_date column to datetime format
df['order_date'] = pd.to_datetime(df['order_date'])

# Convert region and category into categorical data types
df['region'] = df['region'].astype('category')
df['category'] = df['category'].astype('category')

print("Updated Data Types:")
print(df.dtypes)

# Drop order_id column
df = df.drop('order_id', axis=1)

print("Dataset after dropping unnecessary column:")
print(df.head())

print("\nUpdated Dataset Shape:")
print(df.shape)

# Extract year and month from order_date
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month_name()

# Create a new column for sales category
df['sales_category'] = np.where(
    df['sales_amount'] >= 10000,
    'High Sales',
    'Low Sales'
)

print("Dataset after adding new columns:")
print(df.head())

# Check missing values in each column
print("Missing Values in Each Column:")
print(df.isnull().sum())

# Calculate total missing values
print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

# Identify numerical columns
numeric_columns = ['quantity', 'unit_price',
                   'discount_pct', 'sales_amount']

# Replace missing values with column mean
for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

print("Missing values after mean imputation:")
print(df[numeric_columns].isnull().sum())

# Fill missing categorical values using mode
df['region'] = df['region'].fillna(df['region'].mode()[0])

df['payment_method'] = df['payment_method'].fillna(
    df['payment_method'].mode()[0]
)

# Check missing values again
print("Final Missing Values:")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

# Update sales category after handling missing values
df['sales_category'] = np.where(
    df['sales_amount'] >= 10000,
    'High Sales',
    'Low Sales'
)

# Calculate total sales
total_sales = df['sales_amount'].sum()

# Calculate average sales
average_sales = df['sales_amount'].mean()

# Find maximum sales
maximum_sales = df['sales_amount'].max()

# Find minimum sales
minimum_sales = df['sales_amount'].min()

print("Overall Sales Analysis")
print("Total Sales:", round(total_sales, 2))
print("Average Sales:", round(average_sales, 2))
print("Maximum Sales:", round(maximum_sales, 2))
print("Minimum Sales:", round(minimum_sales, 2))

# Calculate sales in each region
region_sales = df.groupby('region', observed=True)['sales_amount'].sum()

print("Region-wise Sales:")
print(region_sales)

# Find region with highest sales
print("\nRegion with Highest Sales:")
print(region_sales.idxmax())

# Calculate sales for each product category
category_sales = df.groupby('category', observed=True)['sales_amount'].sum()

print("Category-wise Sales:")
print(category_sales)

# Find best-selling category
print("\nBest Selling Category:")
print(category_sales.idxmax())

# Calculate total sales for each product
product_sales = df.groupby('product')['sales_amount'].sum()

# Display top 10 products
top_products = product_sales.sort_values(ascending=False).head(10)

print("Top 10 Products by Sales:")
print(top_products)

# Extract month from order date
df['month_number'] = df['order_date'].dt.month

# Calculate monthly sales
monthly_sales = df.groupby('month_number')['sales_amount'].sum()

print("Monthly Sales Analysis:")
print(monthly_sales)

# Find month with highest sales
print("\nMonth with Highest Sales:")
print(monthly_sales.idxmax())

# Create visualizations folder
import os
os.makedirs("visualizations", exist_ok=True)

# Region-wise sales bar chart
plt.figure(figsize=(9, 5))

region_sales.plot(kind='bar')

plt.title("Region-wise Sales Analysis")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("visualizations/region_sales.png")
plt.show()
plt.close()

# Category-wise sales bar chart
plt.figure(figsize=(10, 5))

category_sales.plot(kind='bar')

plt.title("Category-wise Sales Analysis")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=20)
plt.tight_layout()

plt.savefig("visualizations/category_sales.png")
plt.show()
plt.close()

# Top 10 products horizontal bar chart
plt.figure(figsize=(10, 6))

top_products.sort_values().plot(kind='barh')

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")
plt.tight_layout()

plt.savefig("visualizations/top_products.png")
plt.show()
plt.close()

# Monthly sales line chart
plt.figure(figsize=(10, 5))

monthly_sales.plot(kind='line', marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month Number")
plt.ylabel("Total Sales")
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()

plt.savefig("visualizations/monthly_sales.png")
plt.show()
plt.close()

# Count high and low sales orders
sales_count = df['sales_category'].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    sales_count,
    labels=sales_count.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("High Sales vs Low Sales")
plt.tight_layout()

plt.savefig("visualizations/sales_category.png")
plt.show()
plt.close()