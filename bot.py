import os, requests
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
print("NEW_BOT_V2_START")
msg = "🔔 مناقصة جديدة\n🏢 AADL - توريد مكاتب\n📍 الجزائر\n📍 https://www.google.com/maps/search/?api=1&query=Zone+Industrielle+Alger"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
r = requests.post(url, data={"chat_id": CHAT_ID, "text": msg}, timeout=20)
print(f"RESULT:{r.text}")
