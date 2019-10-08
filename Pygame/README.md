# [Installing Pygame](https://www.pygame.org/wiki/GettingStarted)
## Navigate to root director (`cd`)
```python 
python -m pip install -U pygame --user
```
## Test it out
```python
python3 -m pygame.examples.aliens
```
# Starting your file
## Create `jumpingMan.py`
```python
import pygame
from pygame.locals import *
```
## Start with the basics
```python
X = 720
Y = 480
CH = 66
CW = 90
FLOOR = Y-CH-100
```
```python
pygame.init()
screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
background = pygame.image.load('background.png').convert()
player = pygame.image.load('player.png')
ground = pygame.image.load('ground.png')
```
## Add other variables you'll need
```python
speed = 10 # speed of character
playerx = 10 #starting position
playery = FLOOR
```
## Start your game loop
```python
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
```
## Draw your art
```python
    screen.blit(background, (0, 0))
    screen.blit(ground, (0,380))
    screen.blit(player, (playerx,playery))
```
## Add in left/right movement
```python
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        x += speed
    elif key[pygame.K_LEFT]:
        x -= speed
```
## Update and tick to the next frame
```python
    pygame.display.update()
    clock.tick(60)
```
# Spice time (adding jump)
## Need more variables
```python
jumping = False
jumpCount = 10
```
## Also need to assign keybindings
```python
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        jumping = True
    if key[pygame.K_RIGHT]:
        x += speed
    elif key[pygame.K_LEFT]:
        x -= speed
```
## Jumping mechanics
```python
    if jumping:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            jumping = False
```

