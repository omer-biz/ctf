#!/usr/bin/env python
import requests
import base64
import urllib.parse
import struct

url        = "http://natas28.natas.labs.overthewire.org/index.php"
url_search = "http://natas28.natas.labs.overthewire.org/search.php"

proxyDict = {
        "http": "http://127.0.0.1:8080"
        }

def encrypt(s: requests.Session, tok: str):
    res = s.post(url, data = {"query": f"{tok}"}, allow_redirects = False) #proxies=proxyDict)
    param = res.headers['Location'].split('=')[1]
    base64ed = urllib.parse.unquote(param)

    hexed = base64.b64decode(base64ed)
    return hexed
            

    # return res.text

# the ugliest function I have ever written
def p(data: bytes):
    for i in range(0, len(data)):
        print(str(hex(data[i])).split('x')[1].zfill(2), end='')
        print(' ', end='')
        if (i+1) % 16 == 0:
            print()



with requests.Session() as s:
    s.auth = (u'natas28', 'JWwR438wkgTsNKBbcJoowyysdM82YjeF')

    # req = s.get(url)
    a = encrypt(s, 'a')

    p(a)
    print()
    mod = a[:-2] + struct.pack("B", 1) + struct.pack("B", 112)
    p(mod)

    # for i in range(0, 256):
    #     mod = base64.b64encode(a[:-2] + struct.pack("B", i) + struct.pack("B", 112))
    #     res = s.get(url_search, params = {"query": mod}) #proxies=proxyDict)

    #     if "PKCS" not in res.text:
    #         print(res.text)
    #         print(f"found: {hex(i)}")
    #         break
    #     print("trying " + str(hex(i)).zfill(2))



    # for i in range(1, 17):
    #     p(encrypt(s, 'a'*i))
    #     print()


    # print(req.text)

