import os
import sys

if sys.platform == "win32":
    os.system("powershell run.ps1")
else:
    os.system("./run.sh")
