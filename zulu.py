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
<<<<<<< Updated upstream
import os
from shared.control import * 
=======
from shared.control import *
>>>>>>> Stashed changes
from shared.images import *
from shared.screen import *
from shared.sounds import *
from shared.constants import *
from game_changer import openNewGame

<<<<<<< Updated upstream
# Initialize pygame, pygame sounds, control class, and light classes
=======
# Game Zulu
# This game is the first game of the series.
# Game Play: A button will light up. The player must hit a coorosponding button. Other buttons will trigger a fail condition.

>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
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
=======
    #### SOUNDS ####
    pygame.mixer.music.stop()
    soundTrumpet.play()
    pygame.mixer.music.stop()
    logging.info("Game Success")

    #### DISPLAY ####
    gameDisplay.blit(spaceShipSuccess, (0, 0))
    pygame.display.update()

    largeText = pygame.font.SysFont("comicsansms", 250)
    TextSurf, TextRect = text_objects("", largeText)
    TextRect.center = ((round(DISPLAY_WIDTH * 0.5)),
                       (round(DISPLAY_HEIGHT * 0.33)))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    clock.tick(15)

    light.blink(0.2, 6)
>>>>>>> Stashed changes

    while not control.doorOpen():
        for event in pygame.event.get():
            # Quit game from window screen
            if event.type == pygame.QUIT:
                quitgame()
            # Quit game from keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quitgame()
<<<<<<< Updated upstream

        button("Push to Proceed",BUTTON_CENTER_HORIZONTAL,round(DISPLAY_HEIGHT * 0.4),BUTTON_WIDTH,BUTTON_HEIGHT,GREEN,BRIGHT_GREEN,nextGame)
        
=======
        # TODO: Make Proceed only available if game was successful.
        button("Proceed", BUTTON_CENTER_ONE_THIRD, BUTTON_CENTER_VERTICAL,
               BUTTON_WIDTH, BUTTON_HEIGHT, GREEN, BRIGHT_GREEN, game_intro)
        # TODO: Make Leave go back to main screen with list of games
        button("Leave", BUTTON_CENTER_TWO_THIRD, BUTTON_CENTER_VERTICAL,
               BUTTON_WIDTH, BUTTON_HEIGHT, RED, BRIGHT_RED, game_intro)

>>>>>>> Stashed changes
        pygame.display.update()
        clock.tick(15)

def fail():
    logging.info("Game Failure")

    #### DISPLAY #####
<<<<<<< Updated upstream
    gameDisplay.blit(spaceship1Fail, (0,0))  
    pygame.display.update()  
    clock.tick(15)       

    #### SOUNDS ####
    pygame.mixer.music.stop()
    pygame.mixer.stop()
    soundVoiceEndSimulation.play()
    time.sleep(2)  
    soundVoiceAccessDenied.play()
    
=======
    gameDisplay.blit(spaceShipFail, (0, 0))
    pygame.display.update()

    largeText = pygame.font.SysFont("comicsansms", 250)
    TextSurf, TextRect = text_objects("", largeText)
    TextRect.center = ((round(DISPLAY_WIDTH * 0.5)),
                       (round(DISPLAY_HEIGHT * 0.33)))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    clock.tick(15)

>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
=======
        # TODO: Make Enter only available if game was successful. Put LOCK symbol for this fail.
        # TODO: Make dead sound if pushed. Make so nothing happens
        button("Proceed (LOCKED)", BUTTON_CENTER_ONE_THIRD, BUTTON_CENTER_VERTICAL,
               BUTTON_WIDTH, BUTTON_HEIGHT, GREEN, BRIGHT_GREEN, game_intro)
        # TODO: Make Leave go back to main screen with list of games
        button("Leave", BUTTON_CENTER_TWO_THIRD, BUTTON_CENTER_VERTICAL,
               BUTTON_WIDTH, BUTTON_HEIGHT, RED, BRIGHT_RED, game_intro)

        pygame.display.update()
        clock.tick(15)


>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
                    quit()
        
=======

>>>>>>> Stashed changes
        # Start intro music
        while not startMusicPlay:
            pygame.mixer.music.load(introMusicSpace)
            pygame.mixer.music.play(-1)
            startMusicPlay = True

        # Background and title
<<<<<<< Updated upstream
        gameDisplay.blit(stars, (0,0))
        largeText = pygame.font.SysFont("comicsansms",100)
        TextSurf, TextRect = text_objects("Training Day", largeText)
        TextRect.center = ((round(DISPLAY_WIDTH * 0.5)),(round(DISPLAY_HEIGHT * 0.5)))
        gameDisplay.blit(TextSurf, TextRect)
        
        pygame.display.update()
        clock.tick(15)
    game_loop()
        
=======
        gameDisplay.blit(stars, (0, 0))
        largeText = pygame.font.SysFont("comicsansms", 250)
        TextSurf, TextRect = text_objects("Zulu", largeText)
        TextRect.center = ((round(DISPLAY_WIDTH * 0.5)),
                           (round(DISPLAY_HEIGHT * 0.3)))
        gameDisplay.blit(TextSurf, TextRect)

        button("Enter", BUTTON_CENTER_HORIZONTAL, round(DISPLAY_HEIGHT * 0.6),
               BUTTON_WIDTH, BUTTON_HEIGHT, GREEN, BRIGHT_GREEN, game_loop)

        pygame.display.update()
        clock.tick(15)


>>>>>>> Stashed changes
def gate_1():
    light.buttonOne(1)

<<<<<<< Updated upstream
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
=======
    # print('gate 1')
    # print(control.one())
    print(control.down())
    if control.back():
        quitgame()

    # HELP: How to I make this if statement change gate0Success and gate1Success states and not require to put gate_2() funtion?
    if control.one():
        global gateSuccess
        gateSuccess = [False, True, False]

        soundGateSuccess.play()
        light.buttonOne(0)
        time.sleep(0.3)
        gate_2()

    if control.two():
        fail()
>>>>>>> Stashed changes

        if control.two():
            fail()

    pygame.display.update()
    clock.tick(60)


def gate_2():
    light.buttonTwo(1)
<<<<<<< Updated upstream

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
=======
    print('gate 2')
    print(control.one())
    if control.back():
        quitgame()
        quit()

    # HELP: How to I make this if statement change gate0Success and gate1Success states and not require to put gate_2() funtion?
    if control.two():
        global gateSuccess
        gateSuccess = [False, False, True]
        soundGateSuccess.play()
        light.buttonTwo(0)
        time.sleep(0.3)
        gate_3()

    if control.one():
        fail()

    if control.down() or control.up() or control.left() or control.right() or control.three():
        soundButtonDead.play()
>>>>>>> Stashed changes

    pygame.display.update()
    clock.tick(60)


def gate_3():
<<<<<<< Updated upstream
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
    
=======
    light.LED1(1)
    light.LED2(1)

    if control.back():
        pygame.quit()
        quit()

    # HELP: How to I make this if statement change gate0Success and gate1Success states and not require to put gate_2() funtion?
    if control.up():
        global gateSuccess
        gateSuccess = [False, False, False]
        light.LED1(1)
        light.LED2(1)
        time.sleep(0.3)
        success()

    if control.one() or control.two() or control.down() or control.left() or control.right() or control.three():
        fail()

>>>>>>> Stashed changes
    pygame.display.update()
    clock.tick(60)


def game_loop():
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
  
    # Game lights start at OFF
    light.all(0)

    # Game play loop
    while not control.doorOpen():
        
=======

    # Background display
    gameDisplay.blit(spaceShip, (0, 0))
    pygame.display.update()

    gameExit = False

    gateSuccess = [True, False, False]

    while not gameExit:

>>>>>>> Stashed changes
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
