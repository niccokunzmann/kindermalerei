#
# Send an E-Mail
# from https://docs.python.org/2/library/email-examples.html
#
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import urlencode
from cgi import escape as html_escape
from secrets import *

PROGRAM_DESCRIPTION = "Send emails with pictures by children."
SUBJECT = "Bild vom Kind"
TO = 'niccokunzmann@gmail.com'

# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = SUBJECT
msg['From'] = from_mail = FROM
msg['To'] = to_mail = TO
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


file = 'zange.jpg'
with open(file, 'rb') as fp:
    # Open the files in binary mode.  Let the MIMEImage class automatically
    # guess the specific image type.
    img = MIMEImage(fp.read())

msg.attach(img)
msg.attach(msg_text)

# Send the email via our own SMTP server.
# with gmail, see
#   https://www.nixtutor.com/linux/send-mail-through-gmail-with-python/
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
username = from_mail
password = PASSWORD
s.login(username, password)
s.sendmail(from_mail, to_mail, msg.as_string())
s.quit()
