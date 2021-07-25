b = ["" for _ in range(0, 24)]
a = ["" for _ in range(0, 24)]

cv = 'a'

for i in range(0, 24):
    usr_chr_inpt = input()
    b[i] = usr_chr_inpt
    b[i] = str(ord(b[i]) ^ i * 0x03)
    cv = b[i]
    usr_chr_inpt = input()
    a[ord(cv)]

