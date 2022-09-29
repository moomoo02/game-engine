#cli build
#cli run
#cli gen
#cli version
#cli gen build run

import os
import sys
import subprocess

TOOLS_DIR = "tools"

def runCommand(cmd):
    subprocess.call(["python3", "{}/{}/{}.py".format(".", TOOLS_DIR, cmd)])

for cmd in range(1, len(sys.argv)):
    cmd = sys.argv[1]

    print("\n----------------------------------")
    print("Executing: ", cmd)

    
    runCommand(cmd)
