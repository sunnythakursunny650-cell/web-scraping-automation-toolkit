# 🕸️ Web Scraping & Browser Automation Toolkit

An end-to-end Python repository demonstrating modular web scraping architectures, dynamic headless browser automation, authentication workflows, and automated reporting pipelines.

---

## 🚀 Key Modules & Architecture

* **`scraper.py`**: Static HTML multi-page pagination crawler with rate-limiting using `requests` and `BeautifulSoup4`.
* **`book_scraper.py`**: E-commerce data harvesting, price formatting, and star rating conversion.
* **`deep_scraper.py`**: Nested crawler resolving catalog hyperlinks into individual product pages for UPC code extraction.
* **`dynamic_scraper.py`**: Client-side JavaScript rendering handling via `Playwright` headless Chromium engine.
* **`scroll_scraper.py`**: Infinite scroll automation using dynamic JavaScript DOM event execution.
* **`interaction_scraper.py`**: Form inputs, dynamic author/tag select dropdowns, and button click automation.
* **`login_scraper.py` & `save_session.py`**: Authentication form submission and `storage_state` cookie persistence to bypass re-authentication.
* **`fast_scraper.py`**: Direct authorized data scraping leveraging cached session states.
* **`data_pipeline.py`**: Automated data transformation and executive text summary generator.
* **`app.py`**: Interactive Streamlit web dashboard for live scraped data exploration and analytics.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Scraping & Automation:** Playwright, BeautifulSoup4, Requests
* **Data Engineering:** Pandas
* **Dashboarding:** Streamlit

---

## ⚡ Quickstart Setup

1. **Clone the repository:**
   ```bash
   git clone <YOUR-REPO-URL>
   cd web_scraping_project