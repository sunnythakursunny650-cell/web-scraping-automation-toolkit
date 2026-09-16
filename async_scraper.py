import asyncio
import httpx
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.parse import urljoin
from models import BookRecord
from db_pipeline import ScraperDatabase

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
ua = UserAgent()
db = ScraperDatabase()

async def fetch_page(client: httpx.AsyncClient, page_num: int):
    url = BASE_URL.format(page_num)
    headers = {
        "User-Agent": ua.random,
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    
    try:
        response = await client.get(url, headers=headers, timeout=10.0)
        if response.status_code == 200:
            parse_books(response.text)
            print(f"[+] Page {page_num} processed successfully.")
        else:
            print(f"[-] Page {page_num} skipped with status: {response.status_code}")
    except Exception as exc:
        print(f"[!] Error on page {page_num}: {exc}")

def parse_books(html_content: str):
    soup = BeautifulSoup(html_content, "html.parser")
    articles = soup.find_all("article", class_="product_pod")

    for article in articles:
        try:
            title = article.h3.a["title"]
            relative_url = article.h3.a["href"]
            full_url = urljoin("https://books.toscrape.com/catalogue/", relative_url)
            price_text = article.find("p", class_="price_color").text
            rating_class = article.p["class"][1]
            availability = article.find("p", class_="instock availability").text.strip()

            record = BookRecord(
                title=title,
                price_gbp=price_text,
                rating=rating_class,
                availability=availability,
                url=full_url
            )
            db.upsert_book(record.model_dump())
        except Exception as err:
            print(f"[!] Parsing/Validation failure: {err}")

async def main():
    limits = httpx.Limits(max_keepalive_connections=10, max_connections=20)
    async with httpx.AsyncClient(limits=limits) as client:
        # Ek sath 10 pages parallel me scrape honge
        tasks = [fetch_page(client, page) for page in range(1, 11)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    print("Starting high-speed async scraping with DB upsert...")
    asyncio.run(main())
    print("Done! Scraped data stored directly inside scraped_warehouse.db")