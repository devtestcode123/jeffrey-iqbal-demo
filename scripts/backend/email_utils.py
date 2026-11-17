import smtplib
from email.message import EmailMessage


def send_email_smtp(host, port, username, password, subject, html_content, to_emails, from_email):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg.set_content(html_content, subtype='html')

    with smtplib.SMTP(host, port, timeout=10) as server:
        server.starttls()
        if username and password:
            server.login(username, password)
        server.send_message(msg)
