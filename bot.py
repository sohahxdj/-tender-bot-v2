import requests

# التوكن والايدي مركبين
TOKEN = "8897615937:AAFQPxTdg6TeSmIhctrUPYe-W81hzlr28OE"
CHAT_ID = "8471894675"

print("NEW_BOT_V2_START")
print(f"TOKEN_LEN:{len(TOKEN)} CHAT:{CHAT_ID}")

# رسالة تجريبية مع خريطة جوجل
text = """🔔 مناقصة جديدة تجريبية ✅
🏢 AADL - توريد أثاث مكتبي
📍 الجزائر - المنطقة الصناعية
📍 الخريطة: https://www.google.com/maps/search/?api=1&query=Zone+Industrielle+Alger
💰 القيمة: 500 مليون
📅 آخر أجل: 15/08/2026"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {"chat_id": CHAT_ID, "text": text}

r = requests.post(url, data=data, timeout=20)
print(f"RESULT:{r.text}")

if r.json().get("ok"):
    print("SUCCESS - الرسالة وصلت تليجرام!")
else:
    print("FAILED")
