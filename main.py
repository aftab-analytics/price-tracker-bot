import pandas as pd
import os
import datetime
import schedule
import time

from utils.scraper import scrape_product
from utils.email_alert import send_email
from utils.logger import write_log

# ===========================
# 🔥 AUTO FOLDER SETUP
# ===========================
os.makedirs("output", exist_ok=True)
os.makedirs("data", exist_ok=True)

PRODUCT_FILE = "data/products.csv"
OUTPUT_FILE = "output/price_history.csv"

# ===========================
# 🔴 SAFETY CHECK
# ===========================
if not os.path.exists(PRODUCT_FILE) or os.path.getsize(PRODUCT_FILE) == 0:
    print("❌ products.csv missing or empty")
    exit()

# ===========================
# 🔥 CLEAN PRICE FUNCTION
# ===========================
def clean_price(price):
    return float(''.join(c for c in price if c.isdigit() or c == '.'))

# ===========================
# 🔥 MAIN JOB
# ===========================
def job():
    write_log("Running tracker...")

    products = pd.read_csv(PRODUCT_FILE)

    if not os.path.exists(OUTPUT_FILE):
        pd.DataFrame(columns=["date", "product", "price"]).to_csv(OUTPUT_FILE, index=False)

    history = pd.read_csv(OUTPUT_FILE)

    processed_count = 0

    for url in products["url"]:
        name, price = scrape_product(url)

        if not name:
            continue

        price_clean = clean_price(price)
        date = datetime.datetime.now().strftime("%Y-%m-%d")

        # 🔍 LOG PER PRODUCT
        write_log(f"Checking: {name} | Price: {price_clean}")

        new_row = pd.DataFrame([[date, name, price_clean]], columns=["date", "product", "price"])
        history = pd.concat([history, new_row], ignore_index=True, sort=False)

        product_data = history[history["product"] == name]

        if len(product_data) >= 2:
            old_price = product_data.iloc[-2]["price"]
            new_price = product_data.iloc[-1]["price"]

            if new_price < old_price:
                write_log(f"🔥 Price dropped for {name}")
                send_email(name, old_price, new_price)

        processed_count += 1

    history.to_csv(OUTPUT_FILE, index=False)

    # 📊 FINAL LOGS
    write_log(f"Total products processed: {processed_count}")
    write_log(f"Data saved to {OUTPUT_FILE}")
    write_log("Done.")

# ===========================
# ⏰ SCHEDULER
# ===========================
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    