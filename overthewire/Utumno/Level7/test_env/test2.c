#include <stdio.h>

int g_var;

void func();

int main() {
    func();

    printf("%d\n", g_var);
}

void func() {
    g_var = 10;
}
