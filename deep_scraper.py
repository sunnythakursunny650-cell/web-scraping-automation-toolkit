import time
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/"
start_url = "https://books.toscrape.com/catalogue/page-1.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print("Fetching main page...")
response = requests.get(start_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 1. Pehle page se saari books ke detail page links nikalna
book_cards = soup.find_all("article", class_="product_pod")

book_links = []
for card in book_cards[:5]:  # Testing ke liye abhi sirf pehli 5 books depth me scrape karenge
    relative_link = card.find("h3").find("a")["href"]
    # Relative URL ko full URL me convert karna
    full_url = urljoin(base_url, relative_link)
    book_links.append(full_url)

print(f"Collected {len(book_links)} product links. Now scraping deep details...\n")

detailed_books = []

# 2. Har book ke detail page par jakar data nikalna
for index, link in enumerate(book_links, 1):
    print(f"[{index}/{len(book_links)}] Visiting: {link}")
    
    res = requests.get(link, headers=headers)
    if res.status_code != 200:
        continue
        
    page_soup = BeautifulSoup(res.text, "html.parser")

    # Title
    title = page_soup.find("h1").text.strip()

    # Price
    price = page_soup.find("p", class_="price_color").text.strip()

    # Product Description (aksar ek particular div ke p tag me hoti hai)
    desc_tag = page_soup.find("div", id="product_description")
    description = ""
    if desc_tag:
        # Description header ke turant baad wala <p> tag
        description = desc_tag.find_next_sibling("p").text.strip()

    # Table me se UPC (Unique Product Code) nikalna
    table = page_soup.find("table", class_="table-striped")
    upc = table.find("td").text.strip() if table else "N/A"

    detailed_books.append({
        "Title": title,
        "Price": price,
        "UPC": upc,
        "Description": description[:100] + "..."  # Preview ke liye pehle 100 characters
    })

    # Har detail page ke baad halka delay taaki request rate normal rahe
    time.sleep(1)

# 3. CSV me save karein
df = pd.DataFrame(detailed_books)
df.to_csv("deep_books_data.csv", index=False, encoding="utf-8")

print("\nDeep Scraping Complete! Saved in 'deep_books_data.csv'")
print(df[["Title", "UPC", "Price"]])