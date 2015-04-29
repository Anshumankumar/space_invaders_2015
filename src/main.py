#!/usr/bin/env python

import pygame, time
import sys

from sprites import *
from Controller import Controller
pygame.init()

clock = pygame.time.Clock()

size = width, height = 600, 400
black = 0,0,0

#Init objects: playerShip, battalion of enemyShips
def play():
    screen = pygame.display.set_mode(size)
    myfont = pygame.font.SysFont("monospace", 30)
    keys = pygame.key.get_pressed()
    while (not keys[pygame.K_SPACE]):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        textmain = myfont.render(
               "SPACE INVADER" , 1, (0,255,0))
        starttext = myfont.render(
               "Press space to start" , 1, (0,255,0))
        screen.blit(starttext,(200,200))
        screen.blit(textmain,(210,50))
        pygame.display.flip()
        clock.tick(5)
        screen.fill(black)
        screen.blit(textmain,(210,50))

        pygame.display.flip()
        clock.tick(5)
        screen.fill(black)
        keys = pygame.key.get_pressed()

    playerShip = PlayerShip([320,350])
    controller = Controller(14,6,screen)
    while not controller.gameover():
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
        controller.player_collision_check(playerShip)
        #TODO: Get a better way to do this
        # Update objects on screen
        pygame.display.flip()
        clock.tick(30)
    return

if __name__ == '__main__':
    play()
