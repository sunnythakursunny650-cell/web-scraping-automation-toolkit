import sqlite3
import pandas as pd

def inspect():
    with sqlite3.connect("scraped_warehouse.db") as conn:
        df = pd.read_sql_query("SELECT id, title, price_gbp, rating, scraped_at FROM books LIMIT 10", conn)
        total_count = pd.read_sql_query("SELECT COUNT(*) as total FROM books", conn).iloc[0]["total"]
        avg_price = pd.read_sql_query("SELECT AVG(price_gbp) as avg_price FROM books", conn).iloc[0]["avg_price"]
        
    print(f"Total Rows in SQLite: {total_count}")
    print(f"Average Price: £{avg_price:.2f}\n")
    print("Sample Records:")
    print(df.to_string(index=False))

if __name__ == "__main__":
    inspect()