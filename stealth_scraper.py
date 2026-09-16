import asyncio
from playwright.async_api import async_playwright
from fake_useragent import UserAgent

ua = UserAgent()

async def run_stealth_crawler():
    random_user_agent = ua.random
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # Context spoofing: masking automated browser fingerprints
        context = await browser.new_context(
            user_agent=random_user_agent,
            viewport={"width": 1920, "height": 1080},
            locale="en-US",
            timezone_id="America/New_York"
        )
        
        page = await context.new_page()

        # Stealth JS script injection: removes `navigator.webdriver` flag
        await page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
            window.chrome = {
                runtime: {}
            };
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5]
            });
        """)

        test_url = "https://bot.sannysoft.com/"
        print(f"[*] Navigating to bot-detection testbed with User-Agent: {random_user_agent[:45]}...")
        await page.goto(test_url, wait_until="networkidle")

        # Extract detection result from page DOM
        webdriver_flag = await page.evaluate("navigator.webdriver")
        print(f"[+] navigator.webdriver is spoofed to: {webdriver_flag} (Expected: None/Undefined)")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_stealth_crawler())