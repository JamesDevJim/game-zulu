##########################################################################
# Title:        GAME XRAY
# Description:  3rd in the 5 game series. Proof of concept for Perplesso.  
# Game Play:    Players must push buttons 1, 2, and 3 in the correct sequence. Lights 1, 2, 3, 4, 5 with 
#               consequitively illuminate when correct sequence is pushed. When an incorrect sequence is pushed. The 
#               lights turn off and the play must start over. The player has X amount of attempts. 
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

pygame.display.set_caption('Game Xray')
pygame.display.set_icon(gameIcon)

def success():
    #### SOUNDS ####
    pygame.mixer.music.stop()    
    soundTrumpet.play()
    pygame.mixer.music.stop()
    logging.info("Game Success")
   
    #### DISPLAY ####
    gameDisplay.blit(spaceship3Success, (0,0))  
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
    #### SOUNDS ####
    pygame.mixer.music.stop()
    soundMissile.play()
    logging.info("Game Failure")
    
    #### DISPLAY #####
    gameDisplay.blit(spaceship3Fail, (0,0))  
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
    intro = True
    startMusicPlay = False
    while intro:
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
        gameDisplay.blit(galaxy3, (0,0))
        largeText = pygame.font.SysFont("comicsansms",250)
        TextSurf, TextRect = text_objects("XRAY", largeText)
        TextRect.center = ((round(DISPLAY_WIDTH * 0.5)),(round(DISPLAY_HEIGHT * 0.3)))
        gameDisplay.blit(TextSurf, TextRect)

        button("Enter",BUTTON_CENTER_HORIZONTAL,round(DISPLAY_HEIGHT * 0.6),BUTTON_WIDTH,BUTTON_HEIGHT,GREEN,BRIGHT_GREEN,game_loop)
        
        pygame.display.update()
        clock.tick(15)
        
def gate_1():
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

    # Lights to illuminate players progress
    lights = [light.LED1(1), light.LED2(1), light.LED3(1)]
    light.all(0)

    # What step of the sequence is the player currently on? Initialize with 0 for first number in list.
    currentStep = 0

    # Players attempts. Initialize as 1st attempt.
    attempts = 1

    # Leave game loop when players beat the game or maximum # of trys are reached.
    print('Enter while loop')
    while currentStep < len(correctSteps) and attempts <= MAX_TRYS:
        
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
            # These buttons do not do anything
            if control.down() or control.up() or control.left() or control.right():
                print('Dead Button')
                soundButtonDead.play()
            
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
                    if currentStep == 0:
                        light.LED2(1)
                    if currentStep == 1:
                        light.LED3(1)
                    if currentStep == 2:
                        light.LED4(1)         
                    currentStep += 1
                    soundGateSuccess.play()
                    print('Correct input')    
                
                # If the guess does not equal the correct step, then turn off all lights
                else:
                    currentStep = 0
                    attempts += 1
                    guesses = [0,0,0]
                    light.all(0)
                    # TODO: Insert negative sound here
                    soundButtonDead.play()
                    print('Incorrect input. Back to the beginning!')

            print('Guess Array: ',guesses)
            print('Attempts: ', attempts) 
            print('Current Step: ', currentStep)
            time.sleep(0.5)   
    
    # Check whether the puzzle has been solved
    print('Exit while loop')
    if currentStep == len(correctSteps):
        print('Solved! Running success.')
        success()
    else:
        print('Fail Condition')
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

    # Start the game play music
    pygame.mixer.music.stop()
    pygame.mixer.music.load(gamePlayMusic)
    pygame.mixer.music.play(-1)

    # Background display
    gameDisplay.blit(spaceship3, (0,0))    
    pygame.display.update()

    gameExit = False
 
    gateSuccess = [True, False, False]
  
    while not gameExit:
        
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

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()