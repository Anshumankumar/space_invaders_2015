import pygame
import thread
import time

enemycolor = 0,255,0

class Enemy(pygame.sprite.Sprite):
    """Player and opponent weapon"""
    enemyFlag = 0
    def __init__(self, size, pos, speed):
        self.image = pygame.Surface(size)
        self.image.fill(enemycolor)
        self.rect = self.image.get_rect()
        self._posX = pos[0]
        self._posY = pos[1]
        self.speed  = speed
        self.rect = self.rect.move(self._posX,self._posY)
    
    def run(self):
        self.enemyFlag = 1
        thread.start_new_thread(self.update,())

    def update(self):
        if  ( self.enemyFlag == 0 ):
            if (self._direction =="RIGHT"):
                self._posX = self._posX -speed
                self.rect =  self.rect.move(-speed,0)

            if (self._direction =="LEFT"):
                self._posX = self._posX +speed
                self.rect =  self.rect.move(speed,0)
            time.sleep(0.1)
