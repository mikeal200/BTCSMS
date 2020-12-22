import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "myemail"
password = "mypassword"
sms_gateway = "mynumber@vtext.com"
smtp = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(smtp, port)

server.starttls()
server.login(email, password)

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = sms_gateway
body = "bitcoin price"
msg.attach(MIMEText(body, 'plain'))

sms = msg.as_string()

server.sendmail(email, sms_gateway, sms)

server.quit()