#include <unistd.h>

int main(int argc, char **argv) {

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
        "Hello",
        NULL,
    };

    execve("./ut", NULL, envp);
}
