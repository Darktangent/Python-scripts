import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Rohan Ganguly'
email['to'] = 'rohanganguly@icloud.com'
email['subject'] = "You won 1,000,000 dollars"

email.set_content(html.substitute({"name": "Rohan"}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('c1ph3r9@gmail.com', '****')
    smtp.send_message(email)
    print("all done")
