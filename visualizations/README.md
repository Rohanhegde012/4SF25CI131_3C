# Retail Sales Data Analysis using Python

## Project Overview
This project analyzes a Retail Sales dataset using Python and Pandas. The objective is to perform data transformation, handle missing values, generate meaningful insights, and visualize sales information.

## Dataset Information
- Dataset: Retail Sales Dataset
- Records: 1,200
- Columns: 10 (original dataset)
- Format: CSV
- Year: 2025

## Libraries Used
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Tasks Performed

### 1. Dataset Reading
Read the CSV dataset using Pandas.

### 2. Data Understanding
Examined dataset structure, columns, data types and statistical information.

### 3. Data Transformation
- Converted date columns into datetime format.
- Converted selected columns into categorical types.
- Removed unnecessary columns.
- Created year, month and sales category columns.

### 4. Handling Missing Values
- Used mean imputation for numerical columns.
- Used mode imputation for categorical columns.
- Removed all missing values.

### 5. Insight Generation
- Calculated total and average sales.
- Performed region-wise sales analysis.
- Performed category-wise sales analysis.
- Identified the top 10 products.
- Analyzed monthly sales trends.

### 6. Data Visualization
Created the following charts:
- Region-wise Sales
- Category-wise Sales
- Top 10 Products
- Monthly Sales Trend
- High Sales vs Low Sales

## Key Findings
- Total sales: ₹96,44,244.97
- Highest sales region: Central
- Best-selling category: Electronics
- Top product: Keyboard
- Highest sales month: August

## Project Structure
```text
Retail-Sales-Analysis/
│
├── retail_sales_practice_dataset.csv
├── retail_analysis.py
├── README.md
│
└── visualizations/
    ├── region_sales.png
    ├── category_sales.png
    ├── top_products.png
    ├── monthly_sales.png
    └── sales_category.png
```

## How to Run
1. Install Python.
2. Install the required libraries:
   `pip install pandas numpy matplotlib seaborn`
3. Run:
   `python retail_analysis.py`

## Conclusion
This project demonstrates the use of Python libraries for data cleaning, transformation, analysis and visualization of retail sales data.