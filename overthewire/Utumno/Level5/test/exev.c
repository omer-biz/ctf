#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    int i;
    int len;
    char buffer[100];

    if (argc != 2) {
        printf("Usage: %s <number of input>\n", argv[0]);
        exit(0);
    }

    len = atoi(argv[1]);
    for(i = 0; i < len; ++i)
        buffer[i] = 'a';

    buffer[i] = '\0';
    
    printf("debug: buffer: %s\n", buffer);

     char *envp[] = {
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        buffer,
    };


     char *ar[] = {
        "./main",
        buffer,
        NULL,
     };
    execve("./main",ar, NULL);
}

