import smtplib
from email.mime.text import MIMEText

from config import *


def send_email(message: str) -> str:

    sender = f"{SENDER}"
    password = f"{PASSWORD}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Work"
        server.sendmail(sender, sender, msg.as_string())
    except Exception as e:
        return f"{e}, Error"
