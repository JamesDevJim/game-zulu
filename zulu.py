##########################################################################
# Title:        GAME ZULU: Training Day
# Description:  1st in the 5 game series. Proof of concept for Perplesso.  
# Game Play:    A button or light will illuminate. The player must press the coorosponding button. In the 1st 
#               and 2nd gate other buttons do nothing. In the 3rd other buttons will trigger a fail condition. 
#
##########################################################################

import pygame
import random
import logging
import time
import os
from shared.control import * 
from shared.images import *
from shared.screen import *
from shared.sounds import *
from shared.constants import *
from game_changer import openNewGame

# Initialize pygame, pygame sounds, control class, and light classes
pygame.init()
pygame.mixer.init()
control = Control()
light = Light()

clock = pygame.time.Clock()

pygame.display.set_caption('Game Zulu')
pygame.display.set_icon(gameIcon)

def nextGame():
    openNewGame('yankee.py')
    pygame.quit()
    quit()

def success():
    logging.info("Game Success")
    #### DISPLAY ####
    gameDisplay.blit(spaceship1Success, (0,0))  
    pygame.display.update()     
    clock.tick(15)

    #### SOUNDS ####
    pygame.mixer.music.stop()  
    pygame.mixer.stop()  
    soundVoiceEndSimulation.play()
    time.sleep(2)
    soundVoiceDiagnosticComplete.play()
    pygame.mixer.music.stop()

    light.blink(0.2,6)

    while not control.doorOpen():
        for event in pygame.event.get():
            # Quit game from window screen
            if event.type == pygame.QUIT:
                quitgame()
            # Quit game from keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quitgame()

        button("Push to Proceed",BUTTON_CENTER_HORIZONTAL,round(DISPLAY_HEIGHT * 0.4),BUTTON_WIDTH,BUTTON_HEIGHT,GREEN,BRIGHT_GREEN,nextGame)
        
        pygame.display.update()
        clock.tick(15)

def fail():
    logging.info("Game Failure")

    #### DISPLAY #####
    gameDisplay.blit(spaceship1Fail, (0,0))  
    pygame.display.update()  
    clock.tick(15)       

    #### SOUNDS ####
    pygame.mixer.music.stop()
    pygame.mixer.stop()
    soundVoiceEndSimulation.play()
    time.sleep(2)  
    soundVoiceAccessDenied.play()
    
    light.all(0)

    # Player cannot proceed. Must exit the room.
    while not control.doorOpen():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Quit game from keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quitgame()

def quitgame():
    pygame.quit()
    quit()


def game_intro():
    startMusicPlay = False
    
    while control.doorOpen():
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
        largeText = pygame.font.SysFont("comicsansms",100)
        TextSurf, TextRect = text_objects("Training Day", largeText)
        TextRect.center = ((round(DISPLAY_WIDTH * 0.5)),(round(DISPLAY_HEIGHT * 0.5)))
        gameDisplay.blit(TextSurf, TextRect)
        
        pygame.display.update()
        clock.tick(15)
    game_loop()
        
def gate_1():
    light.buttonOne(1)

    if control.buttonAny():
        if control.back():
            quitgame()

        if control.down() or control.up() or control.left() or control.right() or control.three():
            soundInputNegative.play()
     
        if control.one():      
            global gateSuccess
            soundInputPositive.play()
            light.all(0)  
            
            time.sleep(0.5)
            gateSuccess = [False,True,False, False]
            logging.info('Gate 1: Success.')    

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
            soundInputPositive.play()
            light.all(0)   
            
            time.sleep(0.5)           
            gateSuccess = [False, False, True, False] 
            logging.info('Gate 2: Success.') 

        if control.one():
            fail()
        
        if control.down() or control.up() or control.left() or control.right() or control.three():
            soundInputNegative.play()

    pygame.display.update()
    clock.tick(60)


def gate_3():
    light.LED3(1)
   
    if control.buttonAny():

        if control.back():
            pygame.quit()
            quit()

        if control.three():      
            global gateSuccess
            gateSuccess = [False, False, False, True]            
            
            light.all(0)     
            logging.info('Gate 3: Success.')

        if control.one() or control.two() or control.down() or control.left() or control.right() or control.up():
            fail()
    
    pygame.display.update()
    clock.tick(60)


def game_loop():
    global gateSuccess
    gateSuccess = [True, False, False, False]

    # Background display
    gameDisplay.blit(spaceship1, (0,0))    
    pygame.display.update()   
    
    # Start the game play music
    pygame.mixer.music.stop()
    soundGameDoors.play()
    time.sleep(3)
    soundVoiceWelcomeStarFleet.play()
    pygame.mixer.music.load(gamePlayBridge)
    pygame.mixer.music.play(-1)
  
    # Game lights start at OFF
    light.all(0)

    # Game play loop
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
    game_intro()


game_intro()
game_loop()
pygame.quit()
quit()
