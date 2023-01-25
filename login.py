#!/usr/bin/env python3

'''
Code derived from following TA demo on Jan 23, 2023 lab
'''

import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import os
import secret
from http.cookies import SimpleCookie


s = cgi.FieldStorage()
username= s.getfirst("username")
password= s.getfirst("password")


cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get('username'):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

cookie_ok = cookie_username = secret.username and cookie_password == secret.password
form_ok = username = secret.username and password == secret.password

if cookie_ok:
    username = cookie_username
    password = cookie_password


print("Content-Type: text/html")

if form_ok:
    print("Set-Cookie: username = {username}")
    print("Set-Cookie: password = {password}")

if not username and not password:
    print(login_page())
elif username== secret.username and password==secret.password:
    print(secret_page(username,password))
else:
    print(login_page())
    print("username and password")
