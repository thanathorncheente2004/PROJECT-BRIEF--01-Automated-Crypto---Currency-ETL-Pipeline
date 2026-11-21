import os
import time
from dotenv import load_dotenv
import requests

# 1. โหลด API Key จากไฟล์ .env
load_dotenv()
API_KEY = os.getenv("EXCHANGERATE_API_KEY")  # ตั้งชื่อตัวแปรใน .env ให้ตรงกัน

# 2. ใส่ API_KEY ลงใน URL (ใช้ /latest/USD เพื่อดึงเรตทั้งหมดเทียบ USD)
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"

thb_rate = 0
last_update = ""

try:
  response = requests.get(url, timeout=10)
  response.raise_for_status()

  result = response.json()

  if result.get("result") == "success":
    # ดึงเฉพาะเรต THB ออกมาจาก conversion_rates
    thb_rate = result["conversion_rates"]["THB"]
    last_update = result["time_last_update_utc"]

    print(f"อัปเดตล่าสุด: {last_update}")
    print(f"1 USD = {thb_rate} THB")
  else:
    print("API แจ้งข้อผิดพลาด:", result.get("error-type"))

  time.sleep(1)

except requests.exceptions.RequestException as e:
  print("เกิดข้อผิดพลาดในการเชื่อมต่อ:", e)

