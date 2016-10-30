#!/usr/bin/python3
from bottle import post, get, run, request
from send_mail import send_mail
import os
import sys

APPLICATION = 'kindermalerei'
APPDATA_ROOT = os.environ.get('APPDATA', '/var')
APPDATA = os.path.join(APPDATA_ROOT, APPLICATION)

@post('/send_to/<emails>')
def send_mail_to(emails):
    assert all(32 <= ord(letter) <= 127 for letter in emails), emails
    print(emails)
    print(dict(request.headers))
    send_mail(emails, request.body.read(), USERNAME, PASSWORD)

@get('/nixmehr/<email>')
def remove_subscription(email):
    


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("start this program with username and password for gmail as arguments.")
        exit(1)
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    run(host='', port=80, debug=True)
