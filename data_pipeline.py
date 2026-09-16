import os
import pandas as pd

# Pipeline input and output files
input_file = "books_catalog.csv"
report_file = "catalog_summary_report.txt"

print("--- AUTOMATED DATA PROCESSING PIPELINE ---")

if not os.path.exists(input_file):
    print(f"Error: {input_file} not found. Please run book_scraper.py first.")
    exit()

print(f"Loading scraped data from '{input_file}'...")
df = pd.read_csv(input_file)

# 1. Pipeline Transformations & Cleaning
total_books = len(df)
avg_price = df["Price_GBP"].mean()
max_price = df["Price_GBP"].max()
min_price = df["Price_GBP"].min()

# Rating-wise breakdown
rating_distribution = df["Rating"].value_counts().sort_index(ascending=False)

# Top 3 most expensive books
top_expensive = df.sort_values(by="Price_GBP", ascending=False).head(3)

# 2. Automated Text Report Generation
report_content = f"""==================================================
    SCRAPED DATA EXECUTIVE SUMMARY
==================================================
Total Products Processed : {total_books}
Average Book Price       : £{avg_price:.2f}
Price Range              : £{min_price:.2f} - £{max_price:.2f}

Rating Distribution:
{rating_distribution.to_string()}

Top 3 Most Expensive Books:
"""
for _, row in top_expensive.iterrows():
    report_content += f"- {row['Title']} (£{row['Price_GBP']}) [Rating: {row['Rating']}/5]\n"

report_content += "==================================================\n"

# Save summary report
with open(report_file, "w", encoding="utf-8") as f:
    f.write(report_content)

print(f"\nPipeline execution successful!")
print(f"Summary report auto-generated: '{report_file}'\n")
print(report_content)