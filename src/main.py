#!/usr/bin/env python

import pygame, time
import sys

pygame.init()
pygame.mixer.init(11025, 8, 1)

from sprites import *
from Controller import Controller
from Audio import audio

clock = pygame.time.Clock()

size = width, height = 600, 400
black = 0,0,0

#Init objects: playerShip, battalion of enemyShips
def play(speed):
    screen = pygame.display.set_mode(size)
    myfont = pygame.font.SysFont("monospace", 30)
    keys = pygame.key.get_pressed()
    
    #Pre Run
    blinkflag = 0
    while (not keys[pygame.K_SPACE]):
        blinkflag = blinkflag + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        textmain = myfont.render(
               "SPACE INVADER" , 1, (0,255,0))
        starttext = myfont.render(
               "Press space to start" , 1, (0,255,0))
        if (blinkflag < 20):
            screen.blit(starttext,(200,200))
        if (blinkflag > 30):
            blinkflag = 0
        screen.blit(textmain,(210,50))
        pygame.display.flip()
        clock.tick(30)
        screen.fill(black)
        keys = pygame.key.get_pressed()

    #Main Run
    playerShip = PlayerShip([320,350])
    controller = Controller(14,6,screen,speed)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        keys = pygame.key.get_pressed() 
        playerShip.update(keys)
        playerShip.maybeShoot(keys)
        screen.fill(black)
        if playerShip.bullet.bulletFlag > 0: screen.blit(playerShip.bullet.image,playerShip.bullet.rect)
        screen.blit(playerShip.image,playerShip.rect)
        controller.blit()
        controller.collision(playerShip.bullet)
        controller.player_collision_check(playerShip)
        pygame.display.flip()
        clock.tick(30)
        if (controller.gameover()):
            flag = 0
            break
    audio.gameOver()
    
    # Post run
    blinkflag = 0
    while (not keys[pygame.K_SPACE]):
        blinkflag = blinkflag + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        textmain = myfont.render(
               "SPACE INVADER" , 1, (0,255,0))
        starttext = myfont.render(
               "GAME OVER" , 1, (0,255,0))
        if (blinkflag < 20):
            screen.blit(starttext,(230,200))
        if (blinkflag > 30):
            blinkflag = 0
        screen.blit(textmain,(210,50))
        pygame.display.flip()
        clock.tick(30)
        screen.fill(black)
        keys = pygame.key.get_pressed()
    return flag


if __name__ == '__main__':
    speed = 1
    while True:
        flag = play(speed)
        if (flag == 0):
            speed = 1
        else:
            speed = speed+1
