Write your own ELF file which will set the following condition true and 
compile it using nasm.

```c
if ((phdr.p_paddr == ehdr.e_ident[8] * ehdr.e_ident[7]) && (st.st_size < 0x78)) {
    puts("valid file, executing");
    execv(argv[1],0x0);
}
```

```sh
nasm -f bin <file>
```

maze5:ishipaeroo
