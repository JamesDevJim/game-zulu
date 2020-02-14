import pygame
from shared.constants import *

# Use this screen size for testing purposes 
# SCREEN_SIZE = (1200, 800)   #James work PC is 1920 1080
# gameDisplay = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)

# Set screen to full and get screen size to scale buttons
gameDisplay = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
SCREEN_SIZE = gameDisplay.get_size()   #James work PC is 1920 1080 # Uncomment this once testing is complete.

DISPLAY_WIDTH = SCREEN_SIZE[0]
DISPLAY_HEIGHT = SCREEN_SIZE[1]

# Button position, configuration, and action
BUTTON_WIDTH = round(DISPLAY_WIDTH * 0.25)   # Number is a scaling factor. On 1920 screen this is a 300mm button
BUTTON_HEIGHT = round(DISPLAY_HEIGHT * 0.17)    # Number is a scaling factor. On 1080 screen this is a 150mm button
BUTTON_CENTER_HORIZONTAL = round((DISPLAY_WIDTH*0.5)-(BUTTON_WIDTH/2))
BUTTON_CENTER_ONE_THIRD = round((DISPLAY_WIDTH*0.33)-(BUTTON_WIDTH/2))
BUTTON_CENTER_TWO_THIRD = round((DISPLAY_WIDTH*0.66)-(BUTTON_WIDTH/2))
BUTTON_CENTER_VERTICAL = round((DISPLAY_HEIGHT*0.5)-(BUTTON_HEIGHT/2))

##### BUTTONS #####
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()



# Changes images to full screen
def fullScreenImage(path):
  return pygame.transform.scale(pygame.image.load(path), SCREEN_SIZE)