#!/usr/bin/env python

import pygame, time
pygame.init()

size = width, height = 600, 400
black = 0,0,0

screen = pygame.display.set_mode(size)

#Init objects: playerShip, battalion of enemyShips

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    # Update objects on screen

    time.sleep(0.5)
    pygame.display.flip()
