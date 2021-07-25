#!/usr/bin/python2

import tempfile

bts = [chr(i) for i in range(256)]

def execute_payload(payload):
    with tempfile.TemporaryDirectory() as temp_dir:
        open(f"{temp_dir.name}/sh_{payload}").close()


def main():
    execute_payload("\x41\x41\x41\x41")

if __name__ == "__main__":
    main()
