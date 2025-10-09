from email import mime
from http import server
import smtplib
from email.mime.message import MIMEMessage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = smtplib.SMTP('smtp.gmail.com',25)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('setuphari@gmail.com',password)


msg = MIMEMultipart()
msg['FROM'] =  'setuphari@gmail.com'
msg['TO'] = 'setuphari@gmail.com'
msg['SUBJECT'] = 'JUST A SMALL MESSAGE'

with open('message.txt','r') as f:
    message = f.read()
msg.attach(MIMEText(message,'plain'))


