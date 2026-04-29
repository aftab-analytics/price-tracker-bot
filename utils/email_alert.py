import smtplib
from email.message import EmailMessage
from config import EMAIL, PASSWORD, TO_EMAIL

def send_email(product, old_price, new_price):
    msg = EmailMessage()
    msg['Subject'] = "🔥 Price Dropped Alert!"
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL

    msg.set_content(f"""
Price Dropped!

Product: {product}
Old Price: {old_price}
New Price: {new_price}
""")

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)