##########################################################################
# Title:        GAME ZULU
# Description:  1st in the 5 game series. Proof of concept for Perplesso.  
# Game Play:    A button or light will illuminate. The player must press the coorosponding button. In the 1st 
#               and 2nd gate other buttons do nothing. In the 3rd other buttons will trigger a fail condition. 
#
##########################################################################

import pygame
import random
import logging
import time
from shared.control import * 
from shared.images import *
from shared.screen import *
from shared.sounds import *
from shared.constants import *

# Initialize pygame, pygame sounds, control class, and light classes
pygame.init()
pygame.mixer.init()
control = Control()
light = Light()

clock = pygame.time.Clock()

pygame.display.set_caption('Game Zulu')
pygame.display.set_icon(gameIcon)

def success():
    print('Game is won')
    #### SOUNDS ####
    pygame.mixer.music.stop()    
    soundTrumpet.play()
    pygame.mixer.music.stop()
    logging.info("Game Success")
   
    #### DISPLAY ####
    gameDisplay.blit(spaceship1Success, (0,0))  
    pygame.display.update()     
   
    largeText = pygame.font.SysFont("comicsansms",250)
    TextSurf, TextRect = text_objects("", largeText)
    TextRect.center = ((round(DISPLAY_WIDTH * 0.5)),(round(DISPLAY_HEIGHT * 0.33)))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    clock.tick(15)

    light.blink(0.2,6)

    while True:
        for event in pygame.event.get():
            # Quit game from window screen            
            if event.type == pygame.QUIT:
                quitgame()
            # Quit game from keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quitgame()
        # TODO: Make Proceed only available if game was successful.
        button("Proceed",BUTTON_CENTER_ONE_THIRD,BUTTON_CENTER_VERTICAL,BUTTON_WIDTH,BUTTON_HEIGHT,GREEN,BRIGHT_GREEN,game_intro)
        # TODO: Make Leave go back to main screen with list of games
        button("Leave",BUTTON_CENTER_TWO_THIRD,BUTTON_CENTER_VERTICAL,BUTTON_WIDTH,BUTTON_HEIGHT,RED,BRIGHT_RED,game_intro)
 
        pygame.display.update()
        clock.tick(15) 

def fail():
    print('Game is lost.')
    
    #### SOUNDS ####
    pygame.mixer.music.stop()
    soundMissile.play()
    logging.info("Game Failure")
    
    #### DISPLAY #####
    gameDisplay.blit(spaceship1Fail, (0,0))  
    pygame.display.update()  

    largeText = pygame.font.SysFont("comicsansms",250)
    TextSurf, TextRect = text_objects("", largeText)
    TextRect.center = ((round(DISPLAY_WIDTH * 0.5)),(round(DISPLAY_HEIGHT * 0.33)))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    clock.tick(15)   

    light.all(0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Quit game from keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quitgame()

        # TODO: Make Enter only available if game was successful. Put LOCK symbol for this fail.
        # TODO: Make dead sound if pushed. Make so nothing happens        
        button("Proceed (LOCKED)",BUTTON_CENTER_ONE_THIRD,BUTTON_CENTER_VERTICAL,BUTTON_WIDTH,BUTTON_HEIGHT,GREEN,BRIGHT_GREEN,game_intro)
        # TODO: Make Leave go back to main screen with list of games        
        button("Leave",BUTTON_CENTER_TWO_THIRD,BUTTON_CENTER_VERTICAL,BUTTON_WIDTH,BUTTON_HEIGHT,RED,BRIGHT_RED,game_intro)

        pygame.display.update()
        clock.tick(15)
  
def quitgame():
    pygame.quit()
    quit()

def game_intro():
    #intro = True
    startMusicPlay = False
    while not control.doorOpen:
        # Abilty to quit the game
        for event in pygame.event.get():
            # Quit game from window screen
            if event.type == pygame.QUIT:
                quitgame()

            # Quit game from keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    quitgame()
                    quit()
        
        # Start intro music
        while not startMusicPlay:
            pygame.mixer.music.load(introMusicSpace)
            pygame.mixer.music.play(-1)  
            startMusicPlay = True

        # Background and title
        gameDisplay.blit(stars, (0,0))
        largeText = pygame.font.SysFont("comicsansms",250)
        TextSurf, TextRect = text_objects("Zulu", largeText)
        TextRect.center = ((round(DISPLAY_WIDTH * 0.5)),(round(DISPLAY_HEIGHT * 0.3)))
        gameDisplay.blit(TextSurf, TextRect)

        # button("Enter",BUTTON_CENTER_HORIZONTAL,round(DISPLAY_HEIGHT * 0.6),BUTTON_WIDTH,BUTTON_HEIGHT,GREEN,BRIGHT_GREEN,game_loop)
        
        pygame.display.update()
        clock.tick(15)
    
    soundGameDoors.play()
    time.sleep(3)
    
    gameloop()
        
def gate_1():
    light.buttonOne(1) 

    if control.buttonAny():
        if control.back():
            quitgame()

        if control.down() or control.up() or control.left() or control.right() or control.three():
            soundButtonDead.play()
     
        if control.one():      
            global gateSuccess
            soundGateSuccess.play()
            light.all(0)  
            
            time.sleep(0.5)
            gateSuccess = [False,True,False, False]
            print('Gate 1 Success. ...Entering Gate 2.')    

        if control.two():
            fail()

    pygame.display.update()
    clock.tick(60)
   
def gate_2():
    light.buttonTwo(1)

    if control.buttonAny():

        if control.back():
            quitgame()
            quit()

        if control.two():      
            global gateSuccess
            soundGateSuccess.play()
            light.all(0)   
            
            time.sleep(0.5)           
            gateSuccess = [False, False, True, False] 
            print('Gate 2 Success. ...Entering Gate 3.') 

        if control.one():
            fail()
        
        if control.down() or control.up() or control.left() or control.right() or control.three():
            soundButtonDead.play()

    pygame.display.update()
    clock.tick(60)

def gate_3():
    light.LED1(1)
    light.LED2(1)  
   
    if control.buttonAny():

        if control.back():
            pygame.quit()
            quit()

        if control.up():      
            global gateSuccess
            light.all(0)     
            
            gateSuccess = [False, False, False, False]
            print('Gate 3 Success.')
            success()

        if control.one() or control.two() or control.down() or control.left() or control.right() or control.three():
            fail()
    
    pygame.display.update()
    clock.tick(60)

def game_loop():
    global gateSuccess

    # Start the game play music
    pygame.mixer.music.stop()
    pygame.mixer.music.load(gamePlayMusic)
    pygame.mixer.music.play(-1)

    # Background display
    gameDisplay.blit(spaceship1, (0,0))    
    pygame.display.update()

    # gameExit = False
    gateSuccess = [True, False, False, False]
  
    while not control.doorOpen():
        
        # Ability to quit from screen or keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    quitgame()
                    quit()

        #Make game assign random LED on to determine which one wins the gate.
        if gateSuccess[0]:
            gate_1()

        if gateSuccess[1]:
            gate_2()

        if gateSuccess[2]:
            gate_3()

        if gateSuccess[3]:
            success()

        pygame.display.update()
        clock.tick(60)
    
    # if door is not closed then go back to the game intro
    soundGameDoors.play()
    time.sleep(3)
    game_intro()

game_intro()
game_loop()
pygame.quit()
quit()