# Input2 | Pwnable.kr

## stdio

On the command line 

https://unix.stackexchange.com/questions/574086/reading-from-stderr-in-c
https://blog.eldruin.com/inter-process-communication-pipe-fork-cpp-stl-like-streams/
```bash
echo "Hell" | ./test 2<<< "Venm"
```

To run this "exploit"

```bash
# Compile it
gcc -o exploit exploit.c

# Copy it to the server, but first make sure there is a folder called abcd
# inside tmp
scp -P 2222 ./exploit input2@pwnable.kr:/tmp/abcd

# link some files since you can't write to the home directory, in the abdd dir
ln -s ~/input input
ln -s ~/flag flag

# then run the exploit
./exploit
```
