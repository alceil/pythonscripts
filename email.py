import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('senders_email','senders_password')
message = "message to be send"
s.sendmail("smail","spass",message)
s.quit()