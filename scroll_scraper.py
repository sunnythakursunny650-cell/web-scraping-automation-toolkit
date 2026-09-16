import time
from playwright.sync_api import sync_playwright
import pandas as pd

# Official infinite scroll sandbox site
target_url = "https://quotes.toscrape.com/scroll"

quotes_data = []

with sync_playwright() as p:
    # headless=False se aap live browser window ko scroll hote dekh payenge
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()

    print(f"Navigating to {target_url}...")
    page.goto(target_url)

    # Initial content load hone ka wait
    page.wait_for_selector(".quote")

    # Scroll loop: 4 baar bottom tak scroll karenge
    scroll_count = 4
    for i in range(1, scroll_count + 1):
        print(f"Scrolling down... ({i}/{scroll_count})")
        
        # JavaScript run karke page ko bottom par bhejna
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        
        # 1.5 seconds wait taaki browser network se naya batch load kar le
        time.sleep(1.5)

    # Scroll complete hone ke baad saare loaded quotes pick karna
    quotes = page.locator(".quote").all()
    print(f"\nTotal elements loaded on page after scroll: {len(quotes)}")

    for item in quotes:
        text = item.locator(".text").inner_text().strip()
        author = item.locator(".author").inner_text().strip()
        tag_elements = item.locator(".tag").all_inner_texts()

        quotes_data.append({
            "Quote": text,
            "Author": author,
            "Tags": ", ".join(tag_elements)
        })

    browser.close()

# Pandas DataFrame & CSV Export
df = pd.DataFrame(quotes_data)
df.to_csv("infinite_scroll_data.csv", index=False, encoding="utf-8")

print("\nScraping successful!")
print(f"Saved {len(df)} quotes to 'infinite_scroll_data.csv'.")
print("\nPreview:")
print(df.head(4))