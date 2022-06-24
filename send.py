import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

email_sender = "Your login"
email_password = "Your password"

email_getter = "Recipient's email"

smtp_server = smtplib.SMTP("smtp.your_domain", port="")  # Port - 465 or 587
smtp_server.starttls()

msg = MIMEMultipart()
msg["From"] = "Your name"
msg['Subject'] = "Topic"
msg.attach(MIMEText("Hello"))

with open("message.txt", "rb") as f:
    file = MIMEApplication(f.read(), Name=basename("message.txt"))

msg.attach(file)

smtp_server.login(email_sender, email_password)
smtp_server.sendmail(email_sender, email_getter, "Text")  # msg.as_string() or "Text"
