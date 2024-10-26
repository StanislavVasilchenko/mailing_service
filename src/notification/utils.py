import smtplib
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from private_keys import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_PORT
from .constants import BASE_URL_TELEGRAM
from private_keys import BOT_TOKEN


def send_mail(receiver_email, message_text):
    smtp_server = EMAIL_HOST
    smtp_port = EMAIL_PORT
    sender_email = EMAIL_HOST_USER
    password = EMAIL_HOST_PASSWORD

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = message_text[:30]
    message.attach(MIMEText(message_text, "plain"))

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, password)
        server.send_message(msg=message)


def send_to_telegram(telegram_id, message_text):
    params = {"chat_id": telegram_id, "text": message_text}
    requests.post(url=f"{BASE_URL_TELEGRAM}{BOT_TOKEN}/sendMessage", params=params)
