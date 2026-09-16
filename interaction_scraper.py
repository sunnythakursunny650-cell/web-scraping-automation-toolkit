import time
from playwright.sync_api import sync_playwright
import pandas as pd

url = "https://quotes.toscrape.com/search.aspx"

scraped_data = []

with sync_playwright() as p:
    # headless=False rakha hai taaki form fill aur clicks live dikhein
    # slow_mo=500 har action ke beech aadhe second ka gap rakhega taaki aap visually dekh sakein
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    print(f"Opening: {url}")
    page.goto(url)

    # 1. Author Dropdown select karna
    print("Selecting Author: Albert Einstein...")
    # <select id="author"> me option select karna
    page.select_option("#author", label="Albert Einstein")

    # Dropdown select hone ke baad tags dynamically update hote hain, thoda wait
    page.wait_for_timeout(1000)

    # 2. Tag Dropdown select karna
    print("Selecting Tag: inspirational...")
    page.select_option("#tag", label="inspirational")

    page.wait_for_timeout(500)

    # 3. Search Button click karna
    print("Clicking Search Button...")
    page.click('input[name="submit_button"]')

    # 4. Filtered results load hone ka wait
    page.wait_for_selector(".quote")

    # 5. Filtered quotes scrape karna
    quotes = page.locator(".quote").all()
    print(f"\nFound {len(quotes)} filtered results!")

    for item in quotes:
        text = item.locator(".content").inner_text().strip()
        author = item.locator(".author").inner_text().strip()
        tags = item.locator(".tag").all_inner_texts()

        scraped_data.append({
            "Author": author,
            "Quote": text,
            "Tags": ", ".join(tags)
        })

    browser.close()

# CSV me save karein
df = pd.DataFrame(scraped_data)
df.to_csv("filtered_quotes.csv", index=False, encoding="utf-8")

print("\nSearch & Interaction Scraping Completed!")
print(df)