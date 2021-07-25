#include <dirent.h>
#include <sys/types.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv) {
    DIR *d;
    struct dirent *f;

    if( argc < 2 ) {
        exit(0);
    }

    d = opendir(argv[1]);

    f = readdir(d);
    printf("%s\n", f->d_name + 3);

    f = readdir(d);
    printf("%s\n", f->d_name + 3);

    f = readdir(d);
    printf("%s\n", f->d_name + 3);

    f = readdir(d);
    printf("%s\n", f->d_name + 3);

    f = readdir(d);
    printf("%s\n", f->d_name + 3);


    return 0;
}
