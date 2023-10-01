import os
import sys

import subprocess

if sys.platform == "win32":
    os.system("powershell Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned")
    p = subprocess.Popen(["powershell.exe", r".\\run.ps1"], stdout=sys.stdout)
    p.communicate()
else:
    os.system("./run.sh")
