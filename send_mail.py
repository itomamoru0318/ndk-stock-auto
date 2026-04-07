
import csv
import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

# ===== 設定 =====
CSV_FILE = "ndk_stock.csv"

# GitHub Secrets から環境変数として取得
MAIL_FROM = os.environ["MAIL_FROM"]
MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
MAIL_TO = os.environ["MAIL_TO"]

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
{latest['Date']} 時点のNDK株価情報です。

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
msg["From"] = MAIL_FROM
msg["To"] = MAIL_TO
msg["Date"] = formatdate(localtime=True)

# ===== メール送信 =====
with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.login(MAIL_FROM, MAIL_PASSWORD)
    smtp.send_message(msg)

print("Mail sent successfully")
