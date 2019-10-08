import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()

"""
Load game images
"""

"""
Create an initialize variables
"""

while 1:

    """
    This is where you blit your images
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if jumping:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            jumping = False

    """
    Add key triggers here
    """

    pygame.display.update()
    clock.tick(60)