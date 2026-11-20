import os
import json
import time
import requests
from dotenv import load_dotenv

# 1. โหลด API Key จากไฟล์ .env
load_dotenv()
API_KEY = os.getenv("FREECRYPTO_API_KEY")

# 2. กำหนด URL (Endpoint) และ Parameters
url = "https://api.freecryptoapi.com/v1/getData"

# ส่ง API Key ผ่าน Headers (มาตรฐานความปลอดภัย)
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json"
}

# ระบุชื่อเหรียญที่ต้องการ (เช่น BTC, ETH, SOL)
coins = ["BTC", "ETH", "SOL", "ADA", "XRP", "DOGE", "DOT", "LTC", "BCH", "LINK"]
all_data = []

for coin in coins:
    params = {
        "symbol": coin
    }

    # 3. ยิง Request ไปดึงข้อมูล
    response = requests.get(url, headers=headers, params=params, timeout=10)
        
        # เช็กว่ายิงผ่านไหม (Status Code 200 = สำเร็จ)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ ดึงข้อมูลสำเร็จ: {coin}")
        all_data.append(data)   
    else:
        print(f"❌ เกิดข้อผิดพลาด Status Code: {response.status_code}")
        print("รายละเอียด:", response.text)

    time.sleep(2)  # หน่วงเวลา 2 วินาทีระหว่างการดึงข้อมูลแต่ละเหรียญ

# 4. บันทึกข้อมูลลงไฟล์ JSON
output_file = "crypto_data.json"
with open(output_file, "w") as f:
    json.dump(all_data, f)
print(f"✅ บันทึกข้อมูลลงไฟล์ {output_file} สำเร็จ!")