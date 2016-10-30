
#
# Send an E-Mail
# from https://docs.python.org/2/library/email-examples.html
#
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import urlencode
from html import escape as html_escape
from secrets import *

PROGRAM_DESCRIPTION = "Send emails with pictures drawn by children."
SUBJECT = "Bild vom Kind"

def send_mail(to_mail, file, username, password):
    """
    
    :param str to_mail: The email address to send the file to
    :param bytes file: the content of the file to send
    :param str username: the username of a gmail account
    :param str password: the password to the username
    """

    # Create the container (outer) email message.
    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = username
    msg['To'] = to_mail = to
    msg.preamble = PROGRAM_DESCRIPTION

    removelink = 'https://kindermalerei.quelltext.eu/nixmehr/' + to_mail

    # alternative texts, see
    #    https://docs.python.org/2/library/email-examples.html
    text = "Um keine solchen E-Mails von dieser Adresse zu erhalten, rufen Sie " \
           "bitte diesen Link auf: " + removelink
    html = """
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
           Um keine solchen E-Mails von dieser Adresse zu erhalten, rufen Sie
           bitte diesen Link auf: <br/>
           <a href="{removelink}">{removelink}</a>
        </p>
      </body>
    </html>
    """.format(removelink = html_escape(removelink))

    msg_text = MIMEMultipart('alternative')
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg_text.attach(part1)
    msg_text.attach(part2)

    img = MIMEImage(file)
    msg.attach(img)
    msg.attach(msg_text)

    # Send the email via our own SMTP server.
    # with gmail, see
    #   https://www.nixtutor.com/linux/send-mail-through-gmail-with-python/
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(username, password)
    s.sendmail(from_mail, to_mail, msg.as_string())
    s.quit()
