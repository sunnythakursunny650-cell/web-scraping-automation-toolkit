import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Rating word ko integer number me convert karne ke liye dictionary
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

books_data = []

# Pehle 3 pages scrape karenge (Har page par 20 books hoti hain = 60 books)
for page in range(1, 4):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    print(f"Scraping Catalogue Page {page}...")

    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        print(f"Failed to fetch Page {page}")
        break

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Har book ek <article class="product_pod"> container me hoti hai
    book_cards = soup.find_all("article", class_="product_pod")

    for card in book_cards:
        # 1. Book Title: <h3 title="..."> tag se nikalna (full title yahi hota hai)
        title = card.find("h3").find("a")["title"]

        # 2. Price Clean-up: '£51.77' me se '£' hatakar float banana
        raw_price = card.find("p", class_="price_color").text.strip()
        clean_price = float(raw_price.replace("£", "").replace("Â", ""))

        # 3. Rating Extract: class attribute me se word nikalna (e.g. ['star-rating', 'Three'])
        rating_classes = card.find("p", class_="star-rating")["class"]
        rating_word = rating_classes[1]  # Dusra class name rating word hota hai
        rating_number = rating_map.get(rating_word, 0)

        # 4. Stock Availability
        availability = card.find("p", class_="instock availability").text.strip()

        books_data.append({
            "Title": title,
            "Price_GBP": clean_price,
            "Rating": rating_number,
            "In_Stock": availability
        })

    time.sleep(1)

# DataFrame aur CSV Export
df = pd.DataFrame(books_data)
df.to_csv("books_catalog.csv", index=False, encoding="utf-8")

print("\nScraping complete!")
print(f"Total {len(df)} books successfully saved in 'books_catalog.csv'.\n")

# Quick pandas summary print karein
print("Data Preview:")
print(df.head(5))
print("\nAverage Book Price: £", round(df["Price_GBP"].mean(), 2))