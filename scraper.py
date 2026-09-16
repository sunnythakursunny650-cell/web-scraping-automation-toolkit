import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

all_quotes = []

# Page 1 se Page 5 tak loop chalayenge
for page_num in range(1, 6):
    url = f"https://quotes.toscrape.com/page/{page_num}/"
    print(f"Scraping Page {page_num}...")

    try:
        response = requests.get(url, headers=headers, timeout=10)

        # Agar page exist nahi karta ya end aa gaya
        if response.status_code != 200:
            print(f"Page {page_num} load nahi hua (Status: {response.status_code}). Stopping loop.")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        quotes_blocks = soup.find_all("div", class_="quote")

        # Agar kisi page par quotes hi na bache ho
        if not quotes_blocks:
            print(f"No quotes found on Page {page_num}. Ending scrape.")
            break

        for item in quotes_blocks:
            quote_text = item.find("span", class_="text").text.strip()
            author_name = item.find("small", class_="author").text.strip()
            
            tag_elements = item.find_all("a", class_="tag")
            tags = ", ".join([tag.text for tag in tag_elements])

            all_quotes.append({
                "Page": page_num,
                "Quote": quote_text,
                "Author": author_name,
                "Tags": tags
            })

        # Har request ke baad 1 second ka pause (Best Practice)
        time.sleep(1)

    except requests.exceptions.RequestException as e:
        print(f"Network error on Page {page_num}: {e}")
        break

# DataFrame create karke save karein
df = pd.DataFrame(all_quotes)
df.to_csv("all_quotes_data.csv", index=False, encoding="utf-8")

print("\nAll done!")
print(f"Total {len(df)} records scraped across pages.")
print(f"File saved as 'all_quotes_data.csv'.")
