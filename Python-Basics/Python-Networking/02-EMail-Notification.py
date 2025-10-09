from email import mime
import smtplib
from email.mime.text import MIMEText

subject = "This is Sample EMail Template"
body = "Hello I am Learning Python Hence Sending this email"
receiver= 'setuphari@gmail.com'
sender = 'setuphari@gmail.com'
password = '544088'
def send_email(sender,receiver,body,password,subject):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['FROM'] = sender
    msg['To'] = receiver
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp_server:
        smtp_server.login(sender,password)
        smtp_server.sendmail(sender,receiver,msg.as_string())
    print("Email Sent")

send_email(sender,receiver,body,password,subject)