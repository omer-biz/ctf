#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    int table[10];
    char *p;

    table[strtoul(argv[1], NULL, 10)] = strtoul(argv[2], NULL, 16);
    /* table[-1] = "AAAA"; */

    printf("%08x\n", p);

    return 0;
}
