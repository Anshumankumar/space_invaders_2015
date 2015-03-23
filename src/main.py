#!/usr/bin/env python

import pygame, time
import sys

from sprites import *
from Enemy_controller import Enemy_controller
pygame.init()

clock = pygame.time.Clock()

size = width, height = 600, 400
black = 0,0,0

screen = pygame.display.set_mode(size)

#Init objects: playerShip, battalion of enemyShips
playerShip = PlayerShip([25, 20],[320,290])
enemy_controller = Enemy_controller(14,6,screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    keys = pygame.key.get_pressed() 
    playerShip.update(keys)
    screen.fill(black)
    screen.blit(playerShip.bullet.image,playerShip.bullet.rect)
    screen.blit(playerShip.image,playerShip.rect)
    enemy_controller.blit()
    enemy_controller.collision(playerShip.bullet)
    #TODO: Get a better way to do this
    # Update objects on screen

    pygame.display.flip()
    clock.tick(30)
