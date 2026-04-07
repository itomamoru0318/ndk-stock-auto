
import csv
import os
import smtplib
from email.mime.text import MIMEText

CSV_FILE = "ndk_stock.csv"

# GitHub Secrets から取得
MAIL_FROM = os.environ["ndk20240318@gmail.com"]
MAIL_PASSWORD = os.environ["zixq ygbz blaa qewx"]
MAIL_TO = os.environ["ito.mamoru@ndk.com"]

# CSV の最新行を取得
with open(CSV_FILE, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
    latest = rows[-1]

body = f"""\
{latest['Date']} 時点のNDK株価情報です。

株価
Open  : {latest['Open']}
High  : {latest['High']}
Low   : {latest['Low']}
Close : {latest['Close']}

出来高
{latest['Volume']} 株
"""

msg = MIMEText(body)
msg["Subject"] = "【自動配信】NDK 株価情報"
msg["From"] = MAIL_FROM
msg["To"] = MAIL_TO

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(ndk20240318@gmail.com,zixq ygbz blaa qewx )
    smtp.send_message(msg)
