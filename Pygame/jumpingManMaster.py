import pygame
from pygame.locals import *

X = 720
Y = 480
CH = 66
CW = 90
FLOOR = Y-CH-100

pygame.init()
screen = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
background = pygame.image.load('background.png').convert()
player = pygame.image.load('player.png')
ground = pygame.image.load('ground.png')

speed = 10 # speed of character
playerx = 10 #starting position
playery = FLOOR
jumping = False
jumpCount = 10

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    screen.blit(background, (0, 0))
    screen.blit(ground, (0,380))
    screen.blit(player, (playerx,playery))

    if jumping:
        if jumpCount >= -10:
            playery -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            jumping = False

    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        jumping = True
    if key[pygame.K_RIGHT]:
        playerx += speed
    elif key[pygame.K_LEFT]:
        playerx -= speed

    pygame.display.update()
    clock.tick(60)