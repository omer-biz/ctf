            ; DATA XREF from entry0 @ 0x8048487
┌ 233: int main (char **argv);
│           ; var void *buf @ ebp-0x88
│           ; var char *string @ ebp-0x24
│           ; var int32_t var_20h @ ebp-0x20
│           ; var char *path @ ebp-0x10
│           ; var int32_t var_ch @ ebp-0xc
│           ; var int32_t var_8h @ ebp-0x8
│           ; arg char **argv @ esp+0xa4
│           0x0804856b      8d4c2404       lea ecx, [argv]
│           0x0804856f      83e4f0         and esp, 0xfffffff0
│           0x08048572      ff71fc         push dword [ecx - 4]
│           0x08048575      55             push ebp
│           0x08048576      89e5           mov ebp, esp
│           0x08048578      53             push ebx
│           0x08048579      51             push ecx
│           0x0804857a      83c480         add esp, 0xffffff80
│           0x0804857d      e87efeffff     call sym.imp.getpid         ; int getpid(void)
│           0x08048582      8945f4         mov dword [var_ch], eax
│           0x08048585      8d45dc         lea eax, [string]
│           0x08048588      83c006         add eax, 6
│           0x0804858b      8945f0         mov dword [path], eax
│           0x0804858e      83ec04         sub esp, 4
│           0x08048591      ff75f4         push dword [var_ch]
│           0x08048594      6810870408     push str.touch__d           ; 0x8048710 ; "touch %d" ; const char *format
│           0x08048599      8d45dc         lea eax, [string]
│           0x0804859c      50             push eax                    ; char *s
│           0x0804859d      e89efeffff     call sym.imp.sprintf        ; int sprintf(char *s, const char *format, ...)
│           0x080485a2      83c410         add esp, 0x10
│           0x080485a5      83ec08         sub esp, 8
│           0x080485a8      8d8578ffffff   lea eax, [buf]
│           0x080485ae      50             push eax                    ; void *buf
│           0x080485af      ff75f0         push dword [path]           ; const char *path
│           0x080485b2      e819010000     call sym.lstat              ; void lstat(const char *path, void *buf)
│           0x080485b7      83c410         add esp, 0x10
│           0x080485ba      2500f00000     and eax, 0xf000
│           0x080485bf      3d00800000     cmp eax, 0x8000
│       ┌─< 0x080485c4      7436           je 0x80485fc
│       │   0x080485c6      83ec0c         sub esp, 0xc
│       │   0x080485c9      ff75f0         push dword [path]           ; const char *path
│       │   0x080485cc      e81ffeffff     call sym.imp.unlink         ; int unlink(const char *path)
│       │   0x080485d1      83c410         add esp, 0x10
│       │   0x080485d4      e807feffff     call sym.imp.geteuid        ; uid_t geteuid(void)
│       │   0x080485d9      89c3           mov ebx, eax
│       │   0x080485db      e800feffff     call sym.imp.geteuid        ; uid_t geteuid(void)
│       │   0x080485e0      83ec08         sub esp, 8
│       │   0x080485e3      53             push ebx
│       │   0x080485e4      50             push eax
│       │   0x080485e5      e836feffff     call sym.imp.setreuid
│       │   0x080485ea      83c410         add esp, 0x10
│       │   0x080485ed      83ec0c         sub esp, 0xc
│       │   0x080485f0      8d45dc         lea eax, [string]
│       │   0x080485f3      50             push eax                    ; const char *string
│       │   0x080485f4      e817feffff     call sym.imp.system         ; int system(const char *string)
│       │   0x080485f9      83c410         add esp, 0x10
│       │   ; CODE XREF from main @ 0x80485c4
│       └─> 0x080485fc      83ec0c         sub esp, 0xc
│           0x080485ff      68d0070000     push 0x7d0                  ; 2000 ; int s
│           0x08048604      e8c7fdffff     call sym.imp.sleep          ; int sleep(int s)
│           0x08048609      83c410         add esp, 0x10
│           0x0804860c      8d45dc         lea eax, [string]
│           0x0804860f      c70063617420   mov dword [eax], 0x20746163 ; 'cat '
│                                                                      ; [0x20746163:4]=-1
│           0x08048615      c6400400       mov byte [eax + 4], 0
│           0x08048619      c645e020       mov byte [var_20h], 0x20    ; 32
│           0x0804861d      e8befdffff     call sym.imp.geteuid        ; uid_t geteuid(void)
│           0x08048622      89c3           mov ebx, eax
│           0x08048624      e8b7fdffff     call sym.imp.geteuid        ; uid_t geteuid(void)
│           0x08048629      83ec08         sub esp, 8
│           0x0804862c      53             push ebx
│           0x0804862d      50             push eax
│           0x0804862e      e8edfdffff     call sym.imp.setreuid
│           0x08048633      83c410         add esp, 0x10
│           0x08048636      83ec0c         sub esp, 0xc
│           0x08048639      8d45dc         lea eax, [string]
│           0x0804863c      50             push eax                    ; const char *string
│           0x0804863d      e8cefdffff     call sym.imp.system         ; int system(const char *string)
│           0x08048642      83c410         add esp, 0x10
│           0x08048645      b800000000     mov eax, 0
│           0x0804864a      8d65f8         lea esp, [var_8h]
│           0x0804864d      59             pop ecx
│           0x0804864e      5b             pop ebx
│           0x0804864f      5d             pop ebp
│           0x08048650      8d61fc         lea esp, [ecx - 4]
└           0x08048653      c3             ret
