import os
import sys

import subprocess

if sys.platform == "win32":
    file = "run.ps1"
    os.system("powershell Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned")
    p = subprocess.Popen(["powershell.exe", 
              f".\{file}"], 
              stdout=sys.stdout)
    p.communicate()
else:
    os.system("./run.sh")
