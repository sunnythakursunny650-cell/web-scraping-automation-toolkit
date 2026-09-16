from playwright.sync_api import sync_playwright

login_url = "https://quotes.toscrape.com/login"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    print("Logging in once to capture session...")
    page.goto(login_url)

    # Credentials fill karein
    page.fill("#username", "sunny_user")
    page.fill("#password", "sunny_pass_123")
    page.click('input[type="submit"]')

    # Login verify hone ka wait karein
    page.wait_for_selector('a[href="/logout"]')
    print("Logged in successfully!")

    # Yahan magic hota hai: pura session auth.json me dump ho jata hai
    context.storage_state(path="auth.json")
    print("Session state saved securely into 'auth.json'.")

    browser.close()