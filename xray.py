##########################################################################
# Title:        GAME XRAY: Dog Fight
# Description:  2nd in the 5 game series. Proof of concept for Perplesso.  
# Game Play:    Player needs to launch torpedos based on visual clues from the lights
##########################################################################

# Sean - Do not touch. : )

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

# Initialize pygame, pygame sounds, control class, and light classes
pygame.init()
pygame.mixer.init()
control = Control()
light = Light()

clock = pygame.time.Clock()

pygame.display.set_caption('Game Yankee')
pygame.display.set_icon(gameIcon)

# Set time limit for game
timeLimit = 3   # minutes
setTime = pygame.time.get_ticks()
timeLoss = setTime + timeLimit*1000*60   

def nextGame():
    # os.system('whiskey.py')
    # TODO: Figureout how to make next game play. If lose game subsequent game then go back to first game.
    pass

def success():
    logging.info("Game Success")
    #### DISPLAY ####
    gameDisplay.blit(spaceship3Success, (0,0))  
    pygame.display.update()     
    clock.tick(15)

    #### SOUNDS ####
    pygame.mixer.music.stop()
    pygame.mixer.stop()    
    soundVoiceAutoDefenseInitiated
    pygame.mixer.stop()

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
    gameDisplay.blit(spaceship3Fail, (0,0))  
    pygame.display.update()  
    clock.tick(15)       

    #### SOUNDS ####
    pygame.mixer.music.stop()
    pygame.mixer.stop()
    soundVoiceWarning.play() 
    soundMissile.play()
    
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
        TextSurf, TextRect = text_objects("Dog Fight", largeText)
        TextRect.center = ((round(DISPLAY_WIDTH * 0.5)),(round(DISPLAY_HEIGHT * 0.5)))
        gameDisplay.blit(TextSurf, TextRect)
        
        pygame.display.update()
        clock.tick(15)
    game_loop()
        
def gate_1():
    # Player must move light ('missle') to (torpedo bay) position 2
    light.all(0)    
    light.LED2(1)
    time.sleep(2)
    light.LED2(0)

    # light position
    lightPosition = 6 # hidden to right of LED5
    lightPositionChange = 0
    lightPositionCorrect = 2
    loaded = False # TODO: must move this outside function so it does not keep replaying... 
    gate1Success = False 
    
    while not gate1Success:
        # Ability to quit
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
        
        if control.doorOpen():
            game_intro()        
        
        # Game play controls
        if control.buttonAny():
            if control.back():
                quitgame()

            if control.right():
                lightPositionChange = 1
                soundInputPositive.play()
                time.sleep(0.3)

            if control.left():
                lightPositionChange = -1
                soundInputPositive.play()
                time.sleep(0.3)

            if control.down() or control.one() or control.two():
                soundInputNegative.play()
                time.sleep(0.3)
            
            if lightPosition != lightPositionCorrect and control.up():
                soundVoiceUnableToComply.play()
                time.sleep(0.3)
            
            if lightPosition == lightPositionCorrect and control.up():
                loaded = True
                soundTorpedoLoad.play()
                time.sleep(0.3)

            print ('Light Position: ', lightPosition)
            
        else:
            lightPositionChange = 0

        # Change light position based on change
        lightPosition += lightPositionChange   

        # Bounding the light position to the board
        if lightPosition > 6:
            lightPosition = 1
        if lightPosition < 1:
            lightPosition = 6

        # Assign light position
        light.all(0)
        if lightPosition == 1:
            light.LED1(1)
        if lightPosition == 2:
            light.LED2(1)
        if lightPosition == 3:
            light.LED3(1)
        if lightPosition == 4:
            light.LED4(1)
        if lightPosition == 5:
            light.LED5(1)
        if lightPosition == 6:
            light.all(0)        

        # Check time for timeLoss
        if pygame.time.get_ticks() > timeLoss:
            fail()

        if loaded == True and control.three():
            global gateSuccess
            gateSuccess = [False,True,False, False]        
            soundTordedoFire.play()
            light.all(0)  
            time.sleep(0.5)
            print('Gate 1: Success') 
            gate1Success = True

    time.sleep(0.1)       
 
def gate_2():
    # Player must move light ('missle') to (torpedo bay) position 2
    time.sleep(1)
    light.all(0)    
    light.LED4(1)
    time.sleep(2)
    light.LED4(0)

    # light position
    lightPosition = 6 # hidden to right of LED5
    lightPositionChange = 0
    lightPositionCorrect = 4
    loaded = False 
    gate2Success = False

    while not gate2Success:
        
        # Ability to quit
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
        
        if control.doorOpen():
            game_intro()        
        
        # Game play controls
        if control.buttonAny():
            if control.back():
                quitgame()

            if control.right():
                lightPositionChange = 1
                soundInputPositive.play()
                time.sleep(0.3)

            if control.left():
                lightPositionChange = -1
                soundInputPositive.play()
                time.sleep(0.3)

            if control.down() or control.one() or control.two():
                soundInputNegative.play()
                time.sleep(0.3)
            
            if lightPosition != lightPositionCorrect and control.up():
                soundVoiceUnableToComply.play()
                time.sleep(0.3)
            
            if lightPosition == lightPositionCorrect and control.up():
                loaded = True
                soundTorpedoLoad.play()
                time.sleep(0.3)

            print ('Light Position: ',lightPosition)
            
        else:
            lightPositionChange = 0

        # Change light position based on change
        lightPosition += lightPositionChange   

        
        # Bounding the light position to the board
        if lightPosition > 6:
            lightPosition = 1
        if lightPosition < 1:
            lightPosition = 6

        # Assign light position
        light.all(0)
        if lightPosition == 1:
            light.LED1(1)
        if lightPosition == 2:
            light.LED2(1)
        if lightPosition == 3:
            light.LED3(1)
        if lightPosition == 4:
            light.LED4(1)
        if lightPosition == 5:
            light.LED5(1)
        if lightPosition == 6:
            light.all(0)        

        # Check time for timeLoss
        if pygame.time.get_ticks() > timeLoss:
            fail()

        if loaded == True and control.three():
            global gateSuccess
            gateSuccess = [False,False,True, False]        
            soundTordedoFire.play()
            light.all(0)  
            time.sleep(0.5)
            print('Gate 2: Success') 
            gate2Success = True  

    time.sleep(0.1)       

def gate_3():
    # Player must move light ('missle') to (torpedo bay)
    time.sleep(1)
    light.all(0)    
    light.LED3(1)
    time.sleep(1)
    light.LED3(0)

    # light position
    lightPosition = 6 # hidden to right of LED5
    lightPositionChange = 0
    lightPositionCorrect = 3
    loaded = False 
    gate3Success = False   

    while not gate3Success:
        
        # Ability to quit
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
        
        if control.doorOpen():
            game_intro()        
        
        # Game play controls
        if control.buttonAny():
            if control.back():
                quitgame()

            if control.right():
                lightPositionChange = 1
                soundInputPositive.play()
                time.sleep(0.3)

            if control.left():
                lightPositionChange = -1
                soundInputPositive.play()
                time.sleep(0.3)

            if control.down() or control.one() or control.two():
                soundInputNegative.play()
                time.sleep(0.3)
            
            if lightPosition != lightPositionCorrect and control.up():
                soundVoiceUnableToComply.play()
                time.sleep(0.3)
            
            if lightPosition == lightPositionCorrect and control.up():
                loaded = True
                soundTorpedoLoad.play()
                time.sleep(0.3)

            print ('Light Position: ',lightPosition)
            
        else:
            lightPositionChange = 0

        # Change light position based on change
        lightPosition += lightPositionChange   

        
        # Bounding the light position to the board
        if lightPosition > 6:
            lightPosition = 1
        if lightPosition < 1:
            lightPosition = 6

        # Assign light position
        light.all(0)
        if lightPosition == 1:
            light.LED1(1)
        if lightPosition == 2:
            light.LED2(1)
        if lightPosition == 3:
            light.LED3(1)
        if lightPosition == 4:
            light.LED4(1)
        if lightPosition == 5:
            light.LED5(1)
        if lightPosition == 6:
            light.all(0)        

        # Check time for timeLoss
        if pygame.time.get_ticks() > timeLoss:
            fail()
            
        if loaded == True and control.three():
            global gateSuccess
            gateSuccess = [False,False,False, True]        
            soundTordedoFire.play()
            light.all(0)  
            time.sleep(0.5)
            print('Gate 3: Success')  
            gate3Success = True

    time.sleep(0.1)      

def game_loop():
    global gateSuccess
    gateSuccess = [True, False, False, False]

    # Background display
    gameDisplay.blit(spaceship3, (0,0))    
    pygame.display.update()   
    
    # Start the game play music
    pygame.mixer.music.stop()
    soundGameDoors.play()
    time.sleep(0.5)
    soundShipFlyBy.play()
    time.sleep(5)
    soundVoiceWarning.play()
    soundExplodeSmall.play()
    soundAlertRedAlarm.play(-1)

    pygame.mixer.music.load(gamePlayBridge)
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