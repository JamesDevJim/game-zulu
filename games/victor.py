##########################################################################
# Title:        GAME VICTOR
# Description:  5th in the 5 game series. Proof of concept for Perplesso.
# Game Play:    The Escape scene. Must prepare for evacuation and leave ship in escape pods. Engineering. Warp Core. Escape pods.
#
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
from .exceptions import QuitGame, ChangeGame


logger = logging.getLogger(__name__)


def changeGame(mode):
    # if lose, reset back to game zulu
    if mode == "reset":
        raise ChangeGame(new_game="zulu")

    # if win, proceed to next game
    if mode == "next":
        # No more games to play. You Win!
        raise QuitGame("Last game")
    raise QuitGame("Unknown mode: "+str(mode)+" quitting")


def quitgame():
    raise QuitGame

def run():
    # Initialize pygame, pygame sounds, control class, and light classes

    control = Control()
    light = Light()

    clock = pygame.time.Clock()

    pygame.display.set_caption("Game Victor")
    pygame.display.set_icon(gameIcon)

    def success():
        logger.info("Game Success")
        #### DISPLAY ####
        gameDisplay.blit(spaceship5Success, (0, 0))
        pygame.display.update()
        clock.tick(15)

        #### SOUNDS ####

        light.blink(0.2, 6)

        while not control.doorOpen():
            for event in pygame.event.get():
                # Quit game from window screen
                if event.type == pygame.QUIT:
                    quitgame()
                # Quit game from keyboard
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quitgame()

            button(
                "YOU WIN",
                BUTTON_CENTER_HORIZONTAL,
                round(DISPLAY_HEIGHT * 0.4),
                BUTTON_WIDTH,
                BUTTON_HEIGHT,
                GREEN,
                BRIGHT_GREEN,
            )

            pygame.display.update()
            clock.tick(15)


    def fail():
        logger.info("Game Failure")

        #### DISPLAY #####
        gameDisplay.blit(spaceship5Fail, (0, 0))
        pygame.display.update()
        clock.tick(15)

        #### SOUNDS ####

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
        # Go back to game Zulu
        soundGameDoors.play()
        changeGame("reset")



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
            gameDisplay.blit(stars, (0, 0))
            largeText = pygame.font.SysFont("comicsansms", 100)
            TextSurf, TextRect = text_objects("Escape", largeText)
            TextRect.center = ((round(DISPLAY_WIDTH * 0.5)), (round(DISPLAY_HEIGHT * 0.5)))
            gameDisplay.blit(TextSurf, TextRect)

            pygame.display.update()
            clock.tick(15)
        game_loop()


    def gate_1():
        light.buttonOne(1)

        if control.buttonAny():
            if control.back():
                quitgame()

            if (
                control.down()
                or control.up()
                or control.left()
                or control.right()
                or control.three()
            ):
                soundInputNegative.play()

            if control.one():
                global gateSuccess
                soundInputPositive.play()
                light.all(0)

                time.sleep(0.5)
                gateSuccess = [False, True, False, False]
                logger.info("Gate 1: Success.")

            if control.two():
                fail()


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
                logger.info("Gate 2: Success.")

            if control.one():
                fail()

            if (
                control.down()
                or control.up()
                or control.left()
                or control.right()
                or control.three()
            ):
                soundInputNegative.play()


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
                logger.info("Gate 3: Success.")

            if (
                control.one()
                or control.two()
                or control.down()
                or control.left()
                or control.right()
                or control.up()
            ):
                fail()


    def game_loop():
        global gateSuccess
        gateSuccess = [True, False, False, False]

        # Background display
        gameDisplay.blit(spaceship5, (0, 0))
        pygame.display.update()

        # Start the game play music
        pygame.mixer.music.stop()
        soundGameDoors.play()
        time.sleep(3)
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

        # if door is open then go back to the beginning
        soundGameDoors.play()
        changeGame("reset")

    game_intro()
    game_loop()

    raise QuitGame("Quitting game victor")