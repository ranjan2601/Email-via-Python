import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['From'] = 'name'
email['to'] = 'to_mailid@gmail.com'
email['subject']= 'test'

email.set_content('i am a python beginner')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your_mail_id@gmail.com' , 'your_password')
    smtp.send_message(email)
    print('all good')
