import os
import smtplib	
from email.mime.text import MIMEText	
from email.mime.multipart import MIMEMultipart	

email = os.environ.get('BTCEmail')	
password = os.environ.get('BTCPassword')	
sms_gateway = os.environ.get('SMSGateway')
smtp = "smtp.gmail.com"	
port = 587		

def sendsms(price):	

    server = smtplib.SMTP(smtp, port)
    server.starttls()	
    server.login(email, password)	

    msg = MIMEMultipart()	
    msg['From'] = email	
    msg['To'] = sms_gateway	
    sms = "BTC = $" + price	

    server.sendmail(email, sms_gateway, sms)	

    server.quit() 
