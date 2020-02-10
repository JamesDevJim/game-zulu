##########################################################################
# TEST PROGRAM
# Purpose: Use this to test button box button functionality (buttons & lights) and keyboard presses.
##########################################################################

import pygame
import time
from shared.control import * 
from shared.constants import *
from shared.screen import *

# Initialize pygame and control & light classes
pygame.init()
control = Control()
light = Light()

###### DISPLAY #####
display_width = 1200
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Button Box Test')
clock = pygame.time.Clock()  

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def quitgame():
    pygame.quit()
    quit()

def testLoop():
    gameDisplay.fill(WHITE)        
    largeText = pygame.font.SysFont("comicsansms",200) 
    TextSurf, TextRect = text_objects("Start", largeText)
    TextRect.center = ((round(display_width/2)),(round(display_height/2)))
    gameDisplay.blit(TextSurf, TextRect)           
    pygame.display.update()
    clock.tick(60)

    gameExit = False
 
    while not gameExit:

        # Enabled ability to exit game
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if control.buttonAny():
            if control.one():
                gameDisplay.fill(WHITE)  
                TextSurf, TextRect = text_objects("ONE", largeText)
                light.buttonOne(1)
            else:            
                light.buttonOne(0) 

            if control.two():
                gameDisplay.fill(WHITE)  
                TextSurf, TextRect = text_objects("TWO", largeText) 
                light.buttonTwo(1)
            else:            
                light.buttonTwo(0) 


            if control.three():
                gameDisplay.fill(WHITE)  
                TextSurf, TextRect = text_objects("THREE", largeText) 
                light.blink(0.3,4)
            else:            
                light.all(0) 

            if control.up():
                gameDisplay.fill(WHITE)  
                TextSurf, TextRect = text_objects("UP", largeText) 
                light.LED1(1)
                light.LED2(1)            
            else:            
                light.LED1(0) 
                light.LED2(0) 

            if control.down():
                gameDisplay.fill(WHITE)  
                TextSurf, TextRect = text_objects("DOWN", largeText) 
                light.LED1(1)           
            else:            
                light.LED1(0) 

            if control.left():
                gameDisplay.fill(WHITE)  
                TextSurf, TextRect = text_objects("LEFT", largeText) 
                light.LED4(1)           
            else:            
                light.LED4(0) 

            if control.right():
                gameDisplay.fill(WHITE)  
                TextSurf, TextRect = text_objects("RIGHT", largeText)
                light.all(1)          
            else:            
                light.all(0)

            if control.back():
                gameDisplay.fill(WHITE)  
                TextSurf, TextRect = text_objects("BACK", largeText)  
                quitgame()                      
        
        TextRect.center = ((round(display_width * 0.5)),(round(display_height * 0.5)))
        gameDisplay.blit(TextSurf, TextRect)    
        pygame.display.update()
        clock.tick(60)

testLoop()
pygame.quit()
quit()

