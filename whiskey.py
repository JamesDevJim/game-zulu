##########################################################################
# Title:        GAME WHISKEY
# Description:  4th in the 5 game series. Proof of concept for Perplesso.  
# Game Play:    Get Down! Play must man their station doing simple task (click each light button 1, button 2 x3). When 
#               prompted player must duck and not be detected  from motion sensor. When cost is clear player must resume task.
#               Difficulty level increase. Player must turn off (button down) their station before ducking, and turn on 
#               (button up) station before resuming task.
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

pygame.display.set_caption('Game Whiskey')
pygame.display.set_icon(gameIcon)

def nextGame():
    openNewGame('victor.py')
    pygame.quit()
    quit()

def success():
    logging.info("Game Success")
    #### DISPLAY ####
    gameDisplay.blit(spaceship4Success, (0,0))  
    pygame.display.update()     
    clock.tick(15)

    #### SOUNDS ####
    time.sleep(1)
    pygame.mixer.stop()
    soundVoiceWarpEnergyIncrease.play()
    time.sleep(2)
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
    gameDisplay.blit(spaceship4Fail, (0,0))  
    pygame.display.update()  
    clock.tick(15)       

    #### SOUNDS ####
    time.sleep(1)
    pygame.mixer.stop()
    soundExplodeLarge.play()
    time.sleep(2)
    soundVoiceLifeSupportTerminated.play()
    pygame.mixer.music.stop() 

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
        TextSurf, TextRect = text_objects("Jeffrey Tube Repair", largeText)
        TextRect.center = ((round(DISPLAY_WIDTH * 0.5)),(round(DISPLAY_HEIGHT * 0.5)))
        gameDisplay.blit(TextSurf, TextRect)
        
        pygame.display.update()
        clock.tick(15)
    game_loop()
        
def gate_1():

    requiredButtonPushes = 4
    buttonPushes = 0
    buttonOneLight = True
    buttonTwoLight = False 
    playSoundFX1 = True

    while buttonPushes < requiredButtonPushes:
        
        # Ability to exit game        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    quitgame()
                    quit()                
 
        if control.back():
            pygame.quit()
            quit()           
        
        # If door opens then stop the game
        if control.doorOpen():
            game_intro()    

        light.buttonOne(buttonOneLight)
        light.buttonTwo(buttonTwoLight) 

        if control.buttonAny(): 
            # These buttons do not do anything
            if control.down() or control.up() or control.left() or control.right() or control.three():
                soundInputNegative.play()
                time.sleep(0.3)

            if buttonOneLight and control.one():
                soundInputPositive.play()
                logging.info('Correct button. Button push count: ', buttonPushes)
                buttonOneLight = not buttonOneLight
                buttonTwoLight = not buttonTwoLight     
                buttonPushes += 1
                time.sleep(0.3)

            if not buttonOneLight and control.one():
                fail()     

            if buttonTwoLight and control.two():
                soundInputPositive.play()
                logging.info('Correct button')
                logging.info('button pushes', buttonPushes)
                buttonOneLight = not buttonOneLight
                buttonTwoLight = not buttonTwoLight     
                buttonPushes += 1
                time.sleep(0.3)

            if not buttonTwoLight and control.two():
                fail()  

            # Sound FXs
            if buttonPushes == 2 and playSoundFX1:
                soundVoiceDilithiumAdjustmentsComplete.play()
                playSoundFX1 = False

 # Check whether the gate has been solved
    logging.info('Gate 1: Exit while loop')
    if buttonPushes ==  requiredButtonPushes:
        global gateSuccess
        gateSuccess = [False, True, False, False]        
        logging.info('Gate 1: Solved! Entering Gate 2')
        light.all(0)
        time.sleep(0.5)
    else:
        fail()
    
def gate_2():
    #Decoy light
    light.buttonOne(1)
    
    # Play panel explosion sounds. Players must get down!
    soundExplodeConsole1.play() 
    time.sleep(1)  
    soundVoiceWarning.play()
    time.sleep(1)     
    soundExplodeConsole2.play() 
    time.sleep(1)      
    soundExplodeConsole2.play() 
    time.sleep(2)        

    soundExplodeConsole3.play()
    time.sleep(2)
    soundExplodeConsole1.play() 
    time.sleep(3)
    soundExplodeConsole2.play()     
    
    attackTime = 2000   # 2 secs
    setTime = pygame.time.get_ticks()

    releaseTime = setTime + attackTime
    logging.info(control.motion())
    while setTime < releaseTime:
        setTime = pygame.time.get_ticks()
        
        # Ability to exit game        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    quitgame()
                    quit()                
        
        if control.back():
            pygame.quit()
            quit()      

        if control.buttonAny():
            fail()

        if control.motion():
            logging.info('Detected Motion')
            fail()   
    
    # Check whether the gate has been solved
    logging.info('Exit while loop')
    if setTime >= releaseTime:
        global gateSuccess
        gateSuccess = [False, False, True, False]        
        logging.info('Gate 2: Solved')
        soundVoiceReloadCircuitsInitializing.play()
        
        light.all(0)
        time.sleep(0.5)
    else:
        logging.info('Fail Condition')
        fail()
         
def gate_3():

    requiredButtonPushes = 4
    buttonPushes = 0
    buttonOneLight = True
    buttonTwoLight = False 
    playSoundFX2 = True

    while buttonPushes < requiredButtonPushes:
        
        # Ability to exit game        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    quitgame()
                    quit()                
        
        if control.back():
            pygame.quit()
            quit()        
       
        light.buttonOne(buttonOneLight)
        light.buttonTwo(buttonTwoLight) 

        if control.buttonAny(): 
            # These buttons do not do anything
            if control.down() or control.up() or control.left() or control.right() or control.three():
                soundInputNegative.play()
                time.sleep(0.3)

            if buttonOneLight and control.one():
    
                soundInputPositive.play()
                buttonOneLight = not buttonOneLight
                buttonTwoLight = not buttonTwoLight     
                buttonPushes += 1
                time.sleep(0.3)

            if not buttonOneLight and control.one():
                fail()     

            if buttonTwoLight and control.two():
                soundInputPositive.play()
                logging.info('Correct button')
                logging.info('button pushes', buttonPushes)
                buttonOneLight = not buttonOneLight
                buttonTwoLight = not buttonTwoLight     
                buttonPushes += 1
                time.sleep(0.3)

            if not buttonTwoLight and control.two():
                fail()   

            # Sound FXs
            if buttonPushes == 2 and playSoundFX2:
                soundVoiceInitiatingUpdate.play()
                playSoundFX2 = False  

        time.sleep(0.1) 
    
    # Check whether the gate has been solved
    logging.info('Exit while loop 3')
    if buttonPushes ==  requiredButtonPushes:
        global gateSuccess
        logging.info('Solved! Running success.')
        gateSuccess = [False, False, False, True]
        time.sleep(0.5)
    else:
        logging.info('Fail Condition')
        fail()

def game_loop():
    global gateSuccess
    gateSuccess = [True, False, False, False]  

    # Background display
    gameDisplay.blit(spaceship4, (0,0))    
    pygame.display.update()   
    
    # Start the game play music
    pygame.mixer.music.stop()
    soundGameDoors.play()
    time.sleep(3)
    soundAlertCritical.play(-1)    
    soundVoiceShieldFailureRadiation.play()

    pygame.mixer.music.load(gamePlayShip2)
    pygame.mixer.music.play(-1)

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
    time.sleep(1)
    game_intro()

game_intro()
game_loop()
pygame.quit()
quit()


