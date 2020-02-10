import pygame
import random
import logging
import time
from shared.control import * 
from shared.images import *
from shared.screen import *
from shared.sounds import *
from shared.constants import *

#Game Details:
# lights1,2,3,4,5 will sequence when won
# Must push button1,2,3 in the correct sequence
# lights1,2,3,4,5 will come on consequitively when correct sequence is pushed.

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
    gameDisplay.blit(spaceShipSuccess, (0,0))  
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
    gameDisplay.blit(spaceShipFail, (0,0))  
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
                if event.key == pygame.K_q:
                    quitgame()
        
        # Start intro music
        while not startMusicPlay:
            pygame.mixer.music.load(introMusicSpace)
            pygame.mixer.music.play(-1)  
            startMusicPlay = True

        # Background and title
        gameDisplay.blit(spaceship2, (0,0))
        largeText = pygame.font.SysFont("comicsansms",250)
        TextSurf, TextRect = text_objects("XRAY", largeText)
        TextRect.center = ((round(DISPLAY_WIDTH * 0.5)),(round(DISPLAY_HEIGHT * 0.3)))
        gameDisplay.blit(TextSurf, TextRect)

        button("Enter",BUTTON_CENTER_HORIZONTAL,round(DISPLAY_HEIGHT * 0.6),BUTTON_WIDTH,BUTTON_HEIGHT,GREEN,BRIGHT_GREEN,game_loop)
        
        pygame.display.update()
        clock.tick(15)
        
def gate_1():
    # Possible number of trys. Decrease this nuymber to increase difficulty.
    MAX_TRYS = 3

    # COMMENTING OUT FOR TESTING
    # Number of steps in the sequence that the player must follow. Add numbers to increase difficulty.
    #correctSteps = [1,1,1]
    #stepList = [control.one(), control.two(), control.three()]
    # for i in range(2):
    #     correctSteps[i] = random.choice(stepList)
        
    # Temporary Permanent Steps for testing
    correctSteps = [1,1,1]

    # Initialize the guess list
    guesses = [0,0,0]

    # Lights to illuminate players progress
    lights = [light.LED1(1), light.LED2(1), light.LED3(1)]

    # What step of the sequence is the player currently on? Initialize with 0 for first number in list.
    currentStep = 0

    # Players attempts. Initialize as 1st attempt.
    attempts = 1

    # Leave game loop when players beat the game or maximum # of trys are reached.
    while currentStep < 3 and attempts <= MAX_TRYS:
        # User enters their guess and it stores in the list as a number
        print('Attempts: ', attempts) 
        print('Current Step: ', currentStep)
        if control.buttonAny(): 
            # If the number equals the correct step, then add a light
            if  correctSteps[currentStep] == True:
                lights[currentStep]         
                currentStep += 1    
            # If the number does not equal correct step, then turn off all lights
            else:
                currentStep = 0
                attempts += 1
                light.all(0)
                print('Incorrect input. Back to the beginning!')     
    
    # Check whether the puzzle has been solved
    if currentStep == 4:
        success()
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

    # Start the game play music
    pygame.mixer.music.stop()
    pygame.mixer.music.load(gamePlayMusic)
    pygame.mixer.music.play(-1)

    # Background display
    gameDisplay.blit(spaceShip, (0,0))    
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
                if event.key == pygame.K_q:
                    pygame.quit()
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