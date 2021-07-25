#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {

    if(argc != 2) {
        printf("G ive more arguments\n");
        exit(0);
    }
    
    printf("From main: %s\n", argv[1]);
}
