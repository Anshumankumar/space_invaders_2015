#!/usr/bin/env python

import pygame, time
import sys

from sprites import *
from Controller import Controller
pygame.init()

clock = pygame.time.Clock()

size = width, height = 600, 400
black = 0,0,0

screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont("monospace", 16)
#Init objects: playerShip, battalion of enemyShips
playerShip = PlayerShip([320,350])
controller = Controller(14,6,screen)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    keys = pygame.key.get_pressed() 
    playerShip.update(keys)
    playerShip.maybeShoot(keys)
    screen.fill(black)
    if playerShip.bullet.bulletFlag: screen.blit(playerShip.bullet.image,playerShip.bullet.rect)
    screen.blit(playerShip.image,playerShip.rect)
    controller.blit()
    controller.collision(playerShip.bullet)
    #TODO: Get a better way to do this
    # Update objects on screen

    pygame.display.flip()
    clock.tick(30)
