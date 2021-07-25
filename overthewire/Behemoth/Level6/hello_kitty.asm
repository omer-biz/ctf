BITS 32

call shellcode
db "HelloKitty"

shellcode:
    pop ecx
    mov eax, 4
    mov ebx, 1
    mov edx, 10
    int 0x80

    mov eax, 1
    mov ebx, 0
    int 0x80
