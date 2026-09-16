import httpx
from datetime import datetime

def send_discord_alert(webhook_url: str, message: str, status: str = "SUCCESS"):
    if not webhook_url:
        print("[!] Webhook URL not configured. Simulating alert:")
        print(f"[{status}] Alert Payload: {message}")
        return

    color = 3066993 if status == "SUCCESS" else 15158332
    payload = {
        "embeds": [
            {
                "title": f"Scraper Notification: {status}",
                "description": message,
                "color": color,
                "timestamp": datetime.utcnow().isoformat()
            }
        ]
    }
    try:
        res = httpx.post(webhook_url, json=payload, timeout=5.0)
        print(f"[+] Alert sent successfully: HTTP {res.status_code}")
    except Exception as e:
        print(f"[!] Alert dispatch failed: {e}")

if __name__ == "__main__":
    send_discord_alert(
        webhook_url="",
        message="Daily catalog sync complete: 200 books upserted with zero duplicates.",
        status="SUCCESS"
    )