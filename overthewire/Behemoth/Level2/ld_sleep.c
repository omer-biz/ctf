#define _GNU_SOURCE

#include <dlfcn.h>
#include <unistd.h>
#include <stdio.h>

unsigned int sleep(unsigned int se) {
    printf("Custom sleep function");

    unsigned int (*original_sleep)(unsigned int);
    original_sleep = dlsym(RTLD_NEXT, "sleep");
    return (*original_sleep)(se);
}

