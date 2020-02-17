# This file will change between games as players win and lose.

import os


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


def openNewGame(fileOpen):

    # Open new subsequent file
    try:
        os.startfile(fileOpen)
    except:
        pass







