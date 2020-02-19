# This file will change between games as players win and lose.

import subprocess, os, platform

def openNewGame(fileOpen):
    
    if platform.system() == 'Windows':    # Windows
        os.startfile(fileOpen)
    else:                                   # linux variants
        #subprocess.call(('cmd', '/C', 'start', fileOpen))
        subprocess.call(['open', fileOpen])

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










