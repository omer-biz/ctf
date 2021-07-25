0x0804a032

Looks for a file starting with `sh_` and executes whats after the `sh_` in the filename.

Normal shellcode won't work

The 0x2f which translates to '/' prevents us from create the malicious file

encoded shell code from: https://lastlistener.github.io/Courses--SLAE--4_Shellcode_Encoding_Scheme.html

utumno1:ceewaceiph
