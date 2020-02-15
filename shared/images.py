import pygame
from shared.screen import *

###### IMAGES #####

gameIcon = pygame.image.load('images/space_ship_2.png')     # This broke the code when trying to load to big an image...

# Game Zulu
stars = fullScreenImage('images/galaxy1.jpg')
spaceship1 = fullScreenImage('images/game_play1.jpg')
spaceship1Fail = fullScreenImage('images/game_play1_fail.jpg')
spaceship1Success = fullScreenImage('images/game_play1_success.jpg')

# Game Yankee
galaxy2 = fullScreenImage('images/galaxy2.jpg')
spaceship2 = fullScreenImage('images/spaceship2.jpg')
spaceship2Fail = fullScreenImage('images/spaceship2_fail.jpg')
spaceship2Success = fullScreenImage('images/spaceship2_success.jpg')

# Game Xray
galaxy3 = fullScreenImage('images/galaxy3.jpg')
spaceship3 = fullScreenImage('images/game_play3.jpg')
spaceship3Fail = fullScreenImage('images/game_play3_fail.jpg')
spaceship3Success = fullScreenImage('images/game_play3_success.jpg')

# Game Whiskey
galaxy4 = fullScreenImage('images/galaxy4.jpg')
spaceship4 = fullScreenImage('images/spaceship4.png')
spaceship4Fail = fullScreenImage('images/spaceship4_fail.png')
spaceship4Success = fullScreenImage('images/spaceship4_success.png')

# Game Victor
galaxy5 = fullScreenImage('images/galaxy5.jpg')
spaceship5 = fullScreenImage('images/spaceship5.jpg')
spaceship5Fail = fullScreenImage('images/spaceship5_fail.jpg')
spaceship5Success = fullScreenImage('images/spaceship5_success.jpg')



