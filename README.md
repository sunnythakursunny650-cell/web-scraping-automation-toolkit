# 🕸️ Web Scraping & Browser Automation Toolkit

A high-performance, asynchronous web scraping and automated ETL data pipeline built with Python, Playwright, HTTPX, SQLite, and Streamlit. Orchestrated via dual automation layers: Cloud Serverless (GitHub Actions) and Local OS-Level Automation (Windows Task Scheduler).

---

## 🚀 Key Modules & Architecture

* **`async_scraper.py`**: High-concurrency non-blocking crawler utilizing `httpx` and `asyncio` for multi-page batch extraction directly synced to SQLite.
* **`proxy_manager.py`**: Dynamic proxy cycling engine featuring round-robin rotation, latency evaluation, and auto-failover against IP rate limits.
* **`run_scraper.bat`**: Headless batch runner script configured for local background orchestration and automated output logging.
* **`scraper.py` & `book_scraper.py`**: Static HTML multi-page pagination crawlers with structured parsing, pricing sanitation, and rating mapping.
* **`deep_scraper.py`**: Nested crawler traversing catalog hyperlinks into individual product pages for detailed UPC metadata extraction.
* **`dynamic_scraper.py` & `scroll_scraper.py`**: Client-side JavaScript rendering and infinite scroll automation powered by headless `Playwright`.
* **`interaction_scraper.py`**: Form inputs, dynamic author/tag select dropdowns, and button click automation workflows.
* **`login_scraper.py` & `save_session.py`**: Automated auth submission with state persistence via `storage_state` to reuse session tokens.
* **`fast_scraper.py`**: High-speed authenticated extraction utilizing cached browser sessions.
* **`data_pipeline.py`**: Automated data transformation, sanitization, and executive text reporting.
* **`streamlit_app.py`**: Interactive analytical dashboard for querying warehouse records, metric evaluation, and direct CSV export.

---

## 📌 Production Features

* **Dual-Tier Automation Pipeline:**
  * **Cloud CI/CD:** Serverless recurring extraction via GitHub Actions cron triggers.
  * **Local OS Scheduling:** Automated daily runs via Windows Task Scheduler (`DailyWebScraper`) writing logs to `scheduler_log.txt`.
* **Strict Schema Enforcement:** Runtime schema validation and data type verification using `Pydantic`.
* **Relational Deduplication:** SQLite database storage with primary key conflict-handling (`upsert`) preventing duplicate records.
* **Anti-Bot Mitigation:** Playwright stealth evasion techniques combined with dynamic User-Agent and proxy rotation.

---

## 🛠️ Tech Stack

* **Language:** Python 3.12+
* **Scraping & Networking:** Playwright, HTTPX, BeautifulSoup4, Requests, Fake-Useragent
* **Data Engineering & Storage:** SQLite3, Pydantic, Pandas
* **UI & Dashboarding:** Streamlit
* **Automation & CI/CD:** GitHub Actions, Windows Task Scheduler, Batch Scripting

---

## ⚡ Quickstart Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sunnythakursunny650-cell/web-scraping-automation-toolkit.git](https://github.com/sunnythakursunny650-cell/web-scraping-automation-toolkit.git)
   cd web-scraping-automation-toolkit

---

## 👨‍💻 Author

**Sunny Thakur**
* **Live Dashboard:** [Launch Web Scraper App](https://web-scraping-automation-toolkit-cmcuo2c74tq9yjtbahq7cv.streamlit.app/)
* **Streamlit Profile:** [sunnythakursunny650-cell](https://share.streamlit.io/user/sunnythakursunny650-cell)
* **GitHub:** [@sunnythakursunny650-cell](https://github.com/sunnythakursunny650-cell)
* **Email:** [sunnythakursunny650@gmail.com](mailto:sunnythakursunny650@gmail.com)