##########################################################################
# Title:        GAME XRAY: Authorization Required
# Description:  3rd in the 5 game series. Proof of concept for Perplesso.  
# Game Play:    Players must push buttons 1, 2, and 3 in the correct sequence. Lights 1, 2, 3, 4, 5 with 
#               consequitively illuminate when correct sequence is pushed. When an incorrect sequence is pushed. The 
#               lights turn off and the play must start over. The player has X amount of attempts. 
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

# Initialize pygame, pygame sounds, control class, and light classes
pygame.init()
pygame.mixer.init()
control = Control()
light = Light()

clock = pygame.time.Clock()

pygame.display.set_caption('Game Xray')
pygame.display.set_icon(gameIcon)

def nextGame():
    # os.system('xray.py')
    time.sleep(2)
    pygame.quit()
    quit()

def success():
    logging.info('Game Success')
    #### DISPLAY ####
    gameDisplay.blit(spaceship3Success, (0,0))     
    pygame.display.update()
    clock.tick(15) 
    
    #### SOUNDS ####
    pygame.mixer.music.stop()    
    soundVoiceAuthorizationAccepted.play()
    pygame.mixer.music.stop()
   
    # Ability to quit game
    while not control.doorOpen():
        for event in pygame.event.get():          
            if event.type == pygame.QUIT:
                quitgame()

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
    soundVoiceNotAuthorized.play()
    
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

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
        gameDisplay.blit(galaxy3, (0,0))
        largeText = pygame.font.SysFont("comicsansms",100)
        TextSurf, TextRect = text_objects("Authorization Required", largeText)
        TextRect.center = ((round(DISPLAY_WIDTH * 0.5)),(round(DISPLAY_HEIGHT * 0.5)))
        gameDisplay.blit(TextSurf, TextRect)
        
        pygame.display.update()
        clock.tick(15)
    game_loop()    

def gate_1():
    light.all(0)   

    # Decrease this number to increase difficulty.
    MAX_TRYS = 4
    
    # Initialize correctSteps. Number of steps in the sequence that the player must follow. Increase list to increase difficulty.
    correctSteps = [0,0,0]

    # Select buttons to include in the game. Randomly assigns correct button order
    # numberChoices = [1,2,3]
    # for i in range(len(correctSteps)):
    #      correctSteps[i] = random.choice(numberChoices)
    # print(correctSteps)    

    #Comment line below and uncomment block above to randomly assign numbers and make game harderpygame.examples.aliens.main()
    correctSteps = [2,3,2]

    # Initialize the guess list
    guesses = [0,0,0]

    # What step of the sequence is the player currently on? Initialize with 0 for first number in list.
    currentStep = 0

    # Players attempts. Initialize as 1st attempt.
    attempts = 1

    # Leave game loop when players beat the game or maximum # of trys are reached.
    logging.info('Gate 1: Enter while loop')
    while currentStep < len(correctSteps) and attempts <= MAX_TRYS:# and not control.doorOpen():
              
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

        if control.buttonAny(): 
            # These buttons do not do anything
            if control.down() or control.up() or control.left() or control.right():
                soundInputNegative.play()
            
            # These buttons are in gameplay
            if control.one() or control.two() or control.three():

                # User enters their guess and it stores in the guess list            
                if control.one():
                    guesses[currentStep] = 1
                if control.two(): 
                    guesses[currentStep] = 2
                if control.three():
                    guesses[currentStep] = 3                        
                # TODO: Make class control able to return which button was pressed

                # If the correct step equals the guess, then add a light
                if  correctSteps[currentStep] == guesses[currentStep]:
                    logging.info('Gate 1: Correct Input')
                    soundInputPositive.play() 

                    if currentStep == 0:
                        light.LED2(1)
                    if currentStep == 1:
                        light.LED3(1)
                    if currentStep == 2:
                        light.LED4(1)         
                    currentStep += 1 
                
                # If the guess does not equal the correct step, then turn off all lights
                else:
                    logging.info('Gate 1: Incorrect Input')
                    currentStep = 0
                    attempts += 1
                    guesses = [0,0,0]
                    light.all(0)
                    
                    soundInputDeny.play()
                    time.sleep(1)
                    # TODO: Change to "code incorrect"
                    soundVoiceAuthorizationDenied.play()

            logging.info('Guess Array: ',guesses)
            logging.info('Attempts: ', attempts) 
            logging.info('Current Step: ', currentStep)
            time.sleep(0.3)   
    
    # Check whether the puzzle has been solved
    logging.info('Exit while loop')
    if currentStep == len(correctSteps):      
        global gateSuccess
        gateSuccess = [False, False, False, True]
    
    else:
        fail()
        
    pygame.display.update()
    clock.tick(60)

def gate_2():

    pass
    # Do something here.

    pygame.display.update()
    clock.tick(60)

def gate_3():

    pass
    # Do something here.
    
    pygame.display.update()
    clock.tick(60)

def game_loop():
    global gateSuccess
    gateSuccess = [True, False, False, False]

    # Background display
    gameDisplay.blit(spaceship3, (0,0))    
    pygame.display.update()

    # Start the game play music
    pygame.mixer.music.stop()
    soundGameDoors.play()
    time.sleep(4)
    soundVoiceEnterAuthorizationCode.play()
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