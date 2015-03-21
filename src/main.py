#!/usr/bin/env python

import pygame, time
import sys

from sprites import *

pygame.init()

size = width, height = 600, 400
black = 0,0,0

screen = pygame.display.set_mode(size)

#Init objects: playerShip, battalion of enemyShips
playerShip = PlayerShip(20, 16)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    #TODO: Get a better way to do this
    screen.blit(playerShip.image, [290, 320])
    # Update objects on screen

    pygame.display.flip()
    time.sleep(0.1)
