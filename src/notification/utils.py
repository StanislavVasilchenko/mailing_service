import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from private_keys import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_PORT


def send_mail(receiver_email, message_text):
    smtp_server = EMAIL_HOST
    smtp_port = EMAIL_PORT
    sender_email = EMAIL_HOST_USER
    password = EMAIL_HOST_PASSWORD

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Тема письма"
    message.attach(MIMEText(message_text, "plain"))

    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(sender_email, password)
    server.send_message(message)
