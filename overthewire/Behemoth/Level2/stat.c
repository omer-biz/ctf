#include <fcntl.h>
#include <sys/stat.h>

int main(int argc, char **argv) {
    struct stat buff;

    int i = lstat(argv[1], &buff);

    
}
