#include <stdio.h>
#include <stdlib.h>

struct a {
    char *p;
    int table[10];
};

int main(int argc, char **argv) {
    struct a b;

    b.p = (char *)malloc(32);
    
    b.table[strtoul(argv[1], NULL, 10)] = strtoul(argv[2], NULL, 16);

    printf("%08x\n", b.p);
}

