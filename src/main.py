#!/usr/bin/env python

import pygame, time
import sys

from sprites import *

pygame.init()

clock = pygame.time.Clock()

size = width, height = 600, 400
black = 0,0,0

screen = pygame.display.set_mode(size)

#Init objects: playerShip, battalion of enemyShips
playerShip = PlayerShip([25, 20],[290,320])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    keys = pygame.key.get_pressed() 
    playerShip.update(keys)
    screen.fill(black)
    screen.blit(playerShip.bullet.image,playerShip.bullet.rect)
    screen.blit(playerShip.image,playerShip.rect)
    #TODO: Get a better way to do this
    # Update objects on screen

    pygame.display.flip()
    clock.tick(30)
