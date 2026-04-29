# 🚀 Automated Price Tracker Bot (Python)

## 📌 Overview

This project is a **fully automated price tracking system** built using Python.
It monitors product prices from websites, logs historical data, and sends alerts when prices drop.

---

## 🔥 Features

* ✅ Web scraping using BeautifulSoup
* ✅ Automated scheduling (runs every minute/day)
* ✅ Price history tracking (CSV storage)
* ✅ Email alerts on price drop 📧
* ✅ Clean logging system
* ✅ Scalable for multiple products

---

## ⚙️ Tech Stack

* Python
* Pandas
* Requests
* BeautifulSoup
* Schedule

---

## 📂 Project Structure

```
price-tracker-bot/
│
├── main.py
├── config.py
├── requirements.txt
├── .gitignore
│
├── utils/
│   ├── scraper.py
│   ├── email_alert.py
│   ├── logger.py
│
├── data/
│   └── products.csv
```

---

## 🚀 How It Works

1. Reads product URLs from `products.csv`
2. Scrapes product name & price
3. Stores data in `price_history.csv`
4. Compares latest price with previous
5. Sends email alert if price drops

---

## ▶️ Installation

```bash
git clone https://github.com/aftab-analytics/price-tracker-bot.git
cd price-tracker-bot
pip install -r requirements.txt
```

---

## ▶️ Run the Bot

```bash
python main.py
```

---

## 📊 Example Output

```
Running tracker...
Checking: A Light in the Attic | Price: 51.77
Total products processed: 1
Data saved to output/price_history.csv
Done.
```

---

## ⚠️ Important Notes

* Do NOT upload `.env` file (contains sensitive data)
* Add your email credentials securely
* Make sure `products.csv` contains valid URLs

---

## 💡 Future Improvements

* 📈 Price history visualization (graphs)
* 🌐 Web dashboard (Streamlit)
* 📲 Telegram alerts
* ☁️ Cloud deployment

---

## 👨‍💻 Author

**Aftab Ahmed**

---

## 💼 Freelance Services

I can build:

* Web scraping bots
* Automation systems
* Data pipelines
* Custom Python scripts

📩 Available for freelance work
