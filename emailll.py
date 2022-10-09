import smtplib, ssl
import stuff
port = 465  # For SSL
password = "gpwvxoisdgvmffkm"
smtp_server = "smtp.gmail.com"
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.ehlo()
    server.login("yourvpschedule@gmail.com", password)
    # TODO: Send email here
    sender_email = "yourvpschedule@gmail.com"
    receiver_email = "a.williams23@viewpoint.org"
    message = f'''Subject: Schedule For Today
To: {','.join(receiver_email)}
Your schedule for today is {stuff.todaysDay}'''
    server.sendmail(sender_email, receiver_email, message)