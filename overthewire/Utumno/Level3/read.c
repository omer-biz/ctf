#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

int main() {
    int fd;
    char buff[10];

    fd = open("./abc", O_RDONLY);
    read(fd, buff, 10);

    printf("%s\n", buff);

    close(fd);

    return 0;
}
