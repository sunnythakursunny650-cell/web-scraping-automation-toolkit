import sqlite3
from typing import Dict, Any

class ScraperDatabase:
    def __init__(self, db_name: str = "scraped_warehouse.db"):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    price_gbp REAL NOT NULL,
                    rating INTEGER NOT NULL,
                    availability TEXT NOT NULL,
                    url TEXT UNIQUE NOT NULL,
                    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    def upsert_book(self, book: Dict[str, Any]):
        query = """
            INSERT INTO books (title, price_gbp, rating, availability, url)
            VALUES (:title, :price_gbp, :rating, :availability, :url)
            ON CONFLICT(url) DO UPDATE SET
                price_gbp = excluded.price_gbp,
                rating = excluded.rating,
                availability = excluded.availability,
                scraped_at = CURRENT_TIMESTAMP
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, book)
            conn.commit()

if __name__ == "__main__":
    db = ScraperDatabase()
    print("Database & schema initialized successfully.")