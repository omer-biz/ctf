
all: install execve

install:
	gcc -fno-stack-protector -m32 -no-pie -z norelro -z execstack -o main main.c
execve:
	gcc -fno-stack-protector -m32 -no-pie -z norelro -z execstack -o execve exev.c
