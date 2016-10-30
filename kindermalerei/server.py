#!/usr/bin/python3
from bottle import post, get, run, request, static_file, redirect
from send_mail import send_mail
import os
import sys
import shutil

APPLICATION = 'kindermalerei'
APPDATA_ROOT = os.environ.get('APPDATA', '/var')
APPDATA = os.path.join(APPDATA_ROOT, APPLICATION)
HERE = os.path.dirname(__file__) or os.getcwd()
ZIP_PATH = "/" + APPLICATION + ".zip"

@post('/send_to/<emails>')
def send_mail_to(emails):
    """Send the posted content as email."""
    assert all(32 <= ord(letter) <= 127 for letter in emails), emails
    print(emails)
    print(dict(request.headers))
    send_mail(emails, request.body.read(), USERNAME, PASSWORD)

@get('/nixmehr/<email>')
def remove_subscription(email):
    """Never ever send emails to this email address again.

    The database is APPDATA"""
    print(email)

@get('/source')
def get_source_redirect():
    """Download the source of this application."""
    redirect(ZIP_PATH)

@get(ZIP_PATH)
def get_source():
    """Download the source of this application."""
    # from http://stackoverflow.com/questions/458436/adding-folders-to-a-zip-file-using-python#6511788
    path = (shutil.make_archive("/tmp/" + APPLICATION, "zip", HERE))
    return static_file(path, root="/")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("start this program with username and password for gmail as arguments.")
        exit(1)
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    run(host='', port=80, debug=True)
