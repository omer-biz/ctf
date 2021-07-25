#include <stdio.h>

int main() {
  char cVar1;
  int usr_chr_inpt;
  char b [24];
  char a [24];
  int c;
  int counter;
  
  counter = 0;
  while( 1 ) {
    usr_chr_inpt = getchar();
    if ((usr_chr_inpt == -1) || (0x17 < counter)) break;
    b[counter] = usr_chr_inpt;
    b[counter] = b[counter] ^ counter * '\x03';
    cVar1 = b[counter];
    usr_chr_inpt = getchar();
    a[cVar1] = usr_chr_inpt;
    counter = counter + 1;
    }

  printf("a: %s\n", a);
  printf("b: %s\n", b);
}
