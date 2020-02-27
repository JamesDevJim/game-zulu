# This file will change between games as players win and lose.

import subprocess, os, platform, webbrowser, sys
from shared.control import *


def openNewGame(fileOpen):
    if platform.system() == "Windows":  # Windows
        os.startfile(fileOpen)
    else:  # linux variants
        subprocess.Popen(["python3", fileOpen])
