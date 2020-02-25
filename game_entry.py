import pygame
from games import whiskey, victor, zulu, xray, yankee

from games import LAST_GAME, FIRST_GAME

from games.exceptions import QuitGame

game_sequence = [zulu, yankee, xray, whiskey, victor]

current_game = zulu

logging.basicConfig(filename="example.log", filemode="w", level=logging.INFO)

pygame.init()
pygame.mixer.init()

try:
    while current_game is not LAST_GAME:
        current_game = current_game.run()
        if current_game is FIRST_GAME:
            current_game = zulu
except QuitGame:
    print("Quitting game via exception...")

pygame.quit()