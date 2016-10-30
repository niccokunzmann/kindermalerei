from bottle import post, get, run, request
from send_mail import send_mail
import os

APPLICATION = 'kindermalerei'
APPDATA_ROOT = os.environ.get('APPDATA', '/var')
APPDATA = os.path.join(APPDATA_ROOT, APPLICATION)

@post('/send_to/<emails>')
def send_mail_to(emails):
    assert all(32 <= ord(letter) <= 127 for letter in emails), emails
    print(emails)
    print(dict(request.headers))
    send_mail(emails, request.body.read())

@get('/nixmehr/<email>')
def remove_subscription(email):
    

run(host='', port=80, debug=True)
