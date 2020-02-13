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

pygame.display.set_caption('Game Whiskey')
pygame.display.set_icon(gameIcon)

def success():
    #### SOUNDS ####
    pygame.mixer.music.stop()    
    soundTrumpet.play()
    pygame.mixer.music.stop()
    logging.info("Game Success")
   
    #### DISPLAY ####
    gameDisplay.blit(spaceship4Success, (0,0))  
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
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    quitgame()
                    quit()
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
    gameDisplay.blit(spaceship4Fail, (0,0))  
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
    global gateSuccess
    intro = True
    startMusicPlay = False
    gateSuccess = [True, False, False, False]
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
        gameDisplay.blit(galaxy4, (0,0))
        largeText = pygame.font.SysFont("comicsansms",250)
        TextSurf, TextRect = text_objects("XRAY", largeText)
        TextRect.center = ((round(DISPLAY_WIDTH * 0.5)),(round(DISPLAY_HEIGHT * 0.3)))
        gameDisplay.blit(TextSurf, TextRect)

        button("Enter",BUTTON_CENTER_HORIZONTAL,round(DISPLAY_HEIGHT * 0.6),BUTTON_WIDTH,BUTTON_HEIGHT,GREEN,BRIGHT_GREEN,game_loop)
        
        pygame.display.update()
        clock.tick(15)
        
def gate_1():

    requiredButtonPushes = 4
    buttonPushes = 0
    buttonOneLight = True
    buttonTwoLight = False 

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
                print('Dead Button')
                soundButtonDead.play()
                time.sleep(0.3)

            if buttonOneLight and control.one():
                # TODO: Put BETTER SOUND HERE....
                soundGateSuccess.play()
                print('Correct button')
                print('button pushes', buttonPushes)
                buttonOneLight = not buttonOneLight
                buttonTwoLight = not buttonTwoLight     
                buttonPushes += 1
                time.sleep(0.3)

            if not buttonOneLight and control.one():
                fail()     

            if buttonTwoLight and control.two():
                soundGateSuccess.play()
                print('Correct button')
                print('button pushes', buttonPushes)
                buttonOneLight = not buttonOneLight
                buttonTwoLight = not buttonTwoLight     
                buttonPushes += 1
                time.sleep(0.3)

            if not buttonTwoLight and control.two():
                fail()   

# Check whether the gate has been solved
    print('Exit while loop')
    if buttonPushes ==  requiredButtonPushes:
        global gateSuccess
        print('Solved! Entering Gate 2')
        light.all(0)
        gateSuccess = [False, True, False, False]
        soundGateSuccess.play()
        time.sleep(0.5)
    else:
        print('Fail Condition')
        fail()

    
    pygame.display.update()
    clock.tick(60)

def gate_2():
    # Incoming Attack! Get Down!

    # Play incoming attack sound
    soundWarningMissile.play()

    #Decoy light
    light.buttonOne(1)
    
    # Give players time to respond
    time.sleep(8)
    # Insert Flyby sound of attack
    
    attackTime = 3000   # 5 secs
    setTime = pygame.time.get_ticks()

    releaseTime = setTime + attackTime
    print(control.motion())
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
            print('Detected Motion')
            fail()   
    
    # Check whether the gate has been solved
    print('Exit while loop')
    if setTime >= releaseTime:
        global gateSuccess
        print('Solved! On to gate 3')
        soundGateSuccess.play()
        light.all(0)
        gateSuccess = [False, False, True, False]
        time.sleep(0.5)
    else:
        print('Fail Condition')
        fail()
         
        



    pygame.display.update()
    clock.tick(60)

def gate_3():

    requiredButtonPushes = 4
    buttonPushes = 0
    buttonOneLight = True
    buttonTwoLight = False 

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
                print('Dead Button')
                soundButtonDead.play()
                time.sleep(0.3)

            if buttonOneLight and control.one():
                # TODO: Put BETTER SOUND HERE....
                soundGateSuccess.play()
                print('Correct button')
                print('button pushes', buttonPushes)
                buttonOneLight = not buttonOneLight
                buttonTwoLight = not buttonTwoLight     
                buttonPushes += 1
                time.sleep(0.3)

            if not buttonOneLight and control.one():
                fail()     

            if buttonTwoLight and control.two():
                soundGateSuccess.play()
                print('Correct button')
                print('button pushes', buttonPushes)
                buttonOneLight = not buttonOneLight
                buttonTwoLight = not buttonTwoLight     
                buttonPushes += 1
                time.sleep(0.3)

            if not buttonTwoLight and control.two():
                fail()   
        time.sleep(0.1) 
    # Check whether the gate has been solved
    print('Exit while loop 3')
    if buttonPushes ==  requiredButtonPushes:
        global gateSuccess
        print('Solved! Running success.')
        gateSuccess = [False, False, False, True]
        soundGateSuccess.play()
        time.sleep(0.5)
    else:
        print('Fail Condition')
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
    gameDisplay.blit(spaceship4, (0,0))    
    pygame.display.update()

    gameExit = False
   
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
        
        if gateSuccess[3]:
            success()


        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()


