#from email import message
import smtplib
from email.mime import multipart
from email.mime import text
#import logging
import logging.handlers

# import config

handler = logging.handlers
smtp_host = 'smtp_live.com'
smtp_port = 587
from_email = 'ggsudjfg@gfdskh.com'
to_email = 'fgskfhuskjicc@fghdsj.com'
username = 'hsdihvsdlc@gjchivh.com'
password = 'agsdjfgjakh'

logger = logging.getLogger('email')
logger.setLevel(logging.CRITICAL)

logger.addHandler(logging.handlers.SMTPHandler(
    (smtp_host, smtp_port), from_email, to_email,
    subject='Admin test log',
    credentials=(username, password),
    secure=(None, None, None),
    timeout=20
))

msg = multipart.MIMEMultipart()
msg.set_content('Contents of mail')
msg['Subject'] = 'Test Email sub'
msg['From'] = from_email
msg['To'] = to_email
msg.attach(text.MIMEText('Test email', 'plain'))

with open('main.py', 'r') as file:
    attachment = text.MIMEText(file.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment',
        filename='main.txt'
    )
    msg.attach(attachment)

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()
