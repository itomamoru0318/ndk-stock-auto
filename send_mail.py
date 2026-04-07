
import csv
import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

# ===== 設定 =====
CSV_FILE = "ndk_stock.csv"

# GitHub Secrets から取得
MAIL_FROM = os.environ["ndk20240318@gmail.com"]
MAIL_PASSWORD = os.environ["zixq ygbz blaa qewx"]
MAIL_TO = os.environ["ito.mamoru@ndk.com"]

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# ===== CSVから最新行を取得 =====
with open(CSV_FILE, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
    if not rows:
        raise RuntimeError("CSVにデータがありません")
    latest = rows[-1]

# ===== メール本文作成 =====
body = f"""
{latest['Date']} 時点のNDK株価情報をお送りします。

【株価】
Open  : {latest['Open']}
High  : {latest['High']}
Low   : {latest['Low']}
Close : {latest['Close']}

【出来高】
{latest['Volume']} 株
"""

msg = MIMEText(body, _charset="utf-8")
msg["Subject"] = "【自動配信】NDK 株価情報"
msg["From"] = ndk20240318@gmail.com
msg["To"] = ito.mamoru@ndk.com
msg["Date"] = formatdate(localtime=True)

# ===== メール送信 =====
with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.login(ndk20240318@gmail.com, zixq ygbz blaa qewx)
    smtp.send_message(msg)

print("Mail sent successfully")
