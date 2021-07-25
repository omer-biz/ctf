#include <stdio.h>
#include <stdlib.h>
#include <setjmp.h>

void jmpfunction(jmp_buf);

int main() {
    int val;
    jmp_buf env_buffer;

    val = setjmp(env_buffer);

    if(val != 0) {
        printf("Returned from a longjmp() with value = %s\n", val);
        exit(0);
    }

    printf("Jump function call\n");
    jmpfunction(env_buffer);
}

void jmpfunction(jmp_buf env_buffer) {
    longjmp(env_buffer, "hello");
}
