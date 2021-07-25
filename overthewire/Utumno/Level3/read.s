BITS 32             ; tell nasam we are dealing with 32 bit architecture

; execve("/bin/cat", {"/bin/cat", "/tmp/pas", NULL}, NULL)

xor eax, eax        ; set eax to 0
push eax            ; put a null byte on the stack
push 0x7461632f     ; /cat
push 0x6e69622f     ; /bin
mov ebx, esp        ; the first argument
push eax            ; put a null byte on the stack
push 0x7361702f     ; /pas
push 0x706d742f     ; /tmp
mov ecx, esp        ; preparing the second argv
push eax            ; null byte on the stack 
mov edx, esp        ; set envp, the third argument, to null
push ecx            ; push /tmp/pass on the stack
push ebx            ; push /bin/cat on the stack
mov ecx, esp        ; mov {"/bin/cat", "/tmp/pas", NULL} to the second argument
mov al, 0xb         ; execve syscall number
int 0x80            ; call the function
