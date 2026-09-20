@echo off
cd /d "C:\sunny-project\web_scraping_project"
call "C:\sunny-project\web_scraping_project\venv\Scripts\activate.bat"
python async_scraper.py >> "C:\sunny-project\web_scraping_project\scheduler_log.txt" 2>&1