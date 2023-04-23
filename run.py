import os
import sys

if sys.platform == "win32":
    os.system(".\\run.bat")
else:
    os.system("./run.sh")
