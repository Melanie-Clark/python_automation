import subprocess
import os

# get the folder of this file
base_dir = os.path.dirname(os.path.abspath(__file__))

# search for file in same folder above
hello_path = os.path.join(base_dir, "hello_world.py")

# check_call waits until process is finished - opens file 8 times
for i in range(8):
    subprocess.check_call(["python3", hello_path])
