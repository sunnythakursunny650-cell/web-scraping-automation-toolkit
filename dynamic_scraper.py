import time
from playwright.sync_api import sync_playwright
import pandas as pd

# Target: Quotes site ka dynamic JavaScript version
url = "https://quotes.toscrape.com/js/"

print("Launching automated headless browser...")

with sync_playwright() as p:
    # Browser launch karein (headless=True background me bina window khole chalta hai)
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    print(f"Navigating to {url}...")
    page.goto(url)

    # Wait karein jab tak dynamic content render na ho jaye
    page.wait_for_selector(".quote")

    quotes_data = []

    # Sabhi quote elements locate karein
    quotes = page.locator(".quote").all()
    print(f"Found {len(quotes)} dynamically loaded quotes.")

    for item in quotes:
        text = item.locator(".text").inner_text().strip()
        author = item.locator(".author").inner_text().strip()
        tags = item.locator(".tags .tag").all_inner_texts()

        quotes_data.append({
            "Quote": text,
            "Author": author,
            "Tags": ", ".join(tags)
        })

    browser.close()

# Save to CSV
df = pd.DataFrame(quotes_data)
df.to_csv("dynamic_quotes.csv", index=False, encoding="utf-8")

print("\nDynamic Scraping Successful!")
print(df.head(3))