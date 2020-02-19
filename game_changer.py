# This file will change between games as players win and lose.

import subprocess, os, platform, webbrowser, sys
from shared.control import*

# openOnce = False

# if not openOnce:
#     fileOpen = 'zulu.py'    
#     if platform.system() == 'Windows':    # Windows
#         os.startfile(fileOpen)
#     else:  
#         subprocess.Popen(["python3", fileOpen])
#     openOnce = True

# print(openOnce)

# while True:

def openNewGame(fileOpen):
    
    if platform.system() == 'Windows':    # Windows
        os.startfile(fileOpen)
    else:                                   # linux variants
        #subprocess.call(('cmd', '/C', 'start', fileOpen))
        #subprocess.call(('open', fileOpen))
        # webbrowser.open(fileOpen)
        #opener ="open" if sys.platform == "darwin" else "xdg-open"
        #subprocess.call([opener, fileOpen])
        subprocess.Popen(["python3", fileOpen])

# def openNewGame(fileClose, fileOpen):
#     #Close current file
#     try:
#         os.startfile(fileClose)
#     except Exception, e:
#         print str(e)        


#     # Open new subsequent file
#     try:
#         os.startfile(fileOpen)
#     except:
#         print str(e)










