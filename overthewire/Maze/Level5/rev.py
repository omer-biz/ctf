p_base = "printlol"

username = "printlol"
new_str = ["" for _ in range(len(p_base))]

for i in range(len(p_base)):
    new_str[i] = chr(ord(p_base[i]) - (ord(username[i]) - 0x41 + i * 0x02))

print("".join(new_str))
