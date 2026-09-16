import time
from playwright.sync_api import sync_playwright
import pandas as pd

login_url = "https://quotes.toscrape.com/login"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=400)
    page = browser.new_page()

    print("Navigating to login page...")
    page.goto(login_url)

    # 1. Credentials enter karna
    print("Filling credentials...")
    page.fill("#username", "my_automation_user")
    page.fill("#password", "supersecretpassword")

    # 2. Login button dabana
    print("Submitting login form...")
    page.click('input[type="submit"]')

    # 3. Post-login verification: Login ke baad site par 'Logout' link aati hai
    page.wait_for_selector('a[href="/logout"]')
    print("Authentication successful! Now on authenticated dashboard.\n")

    # 4. Protected page se quotes extract karna
    quotes_elements = page.locator(".quote").all()
    logged_in_data = []

    for item in quotes_elements:
        quote = item.locator(".text").inner_text().strip()
        author = item.locator(".author").inner_text().strip()
        logged_in_data.append({
            "Author": author,
            "Quote": quote
        })

    browser.close()

# CSV save
df = pd.DataFrame(logged_in_data)
df.to_csv("logged_in_quotes.csv", index=False, encoding="utf-8")

print(f"Extraction complete! Saved {len(df)} records into 'logged_in_quotes.csv'.")
print(df.head(3))