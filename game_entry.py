import logging

import pygame
from games import whiskey, victor, zulu, xray, yankee

from games import LAST_GAME, FIRST_GAME

from games.exceptions import QuitGame, ChangeGame

game_sequence = [zulu, yankee, xray, whiskey, victor]
game_names = {
    "zulu": zulu,
    "yankee": yankee,
    "xray": xray,
    "whiskey": whiskey,
    "victor": victor,
}

current_game = zulu


LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(filename="example.log", filemode="w", level=logging.INFO, format=LOG_FORMAT)

pygame.init()
pygame.mixer.init()

try:
    while current_game is not LAST_GAME:
        try:
            current_game = current_game.run()
        except ChangeGame as ex:
            next_game = ex.new_game
            if isinstance(next_game, str):
                current_game = game_names[next_game]
            elif hasattr(next_game, "run"):
                current_game = next_game
        else:
            if current_game is FIRST_GAME:
                current_game = zulu
except QuitGame:
    print("Quitting game via exception...")

pygame.quit()
