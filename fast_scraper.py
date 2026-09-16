from playwright.sync_api import sync_playwright
import pandas as pd

# Notice: Hum login page par nahi ja rahe, direct home page par ja rahe hain
target_url = "https://quotes.toscrape.com/"

with sync_playwright() as p:
    # Headless background me chalega
    browser = p.chromium.launch(headless=True)

    # Browser ko bataya ki pehle se saved auth.json use kare
    context = browser.new_context(storage_state="auth.json")
    page = context.new_page()

    print("Navigating directly to site using saved session...")
    page.goto(target_url)

    # Check karein ki kya site ne hume directly logged in mana:
    logout_btn = page.locator('a[href="/logout"]')
    if logout_btn.count() > 0:
        print("Verified: Already Logged In via saved cookies! Zero login overhead.")
    else:
        print("Session expired or not logged in.")

    # Data extract karein
    quotes_elements = page.locator(".quote").all()
    data = []
    for item in quotes_elements:
        data.append({
            "Quote": item.locator(".text").inner_text().strip(),
            "Author": item.locator(".author").inner_text().strip()
        })

    browser.close()

df = pd.DataFrame(data)
df.to_csv("fast_extracted_quotes.csv", index=False)
print(f"Instantly scraped {len(df)} records using saved session!")