import os, requests
TOKEN = os.getenv("TELEGRAM_TOKEN","").strip()
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID","").strip()
print(f"NEW_BOT_V2_START LEN:{len(TOKEN)}")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
r = requests.post(url, data={"chat_id": CHAT_ID, "text": "🔔 البوت عاد يشتغل ✅ التجربة نجحت!\n📍 https://maps.google.com/?q=Alger"}, timeout=20)
print(f"RESULT:{r.text}")
