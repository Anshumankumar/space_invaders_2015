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
        self._direction = "RIGHT"

    def updateDirection(direction):
        self._direction = direction
    
    def run(self):
        self.enemyFlag = 1
        thread.start_new_thread(self.update,())

    def update(self):
        if  ( self.enemyFlag == 0 ):
            if (self._direction =="RIGHT" and self._posX > 20):
                self._posX = self._posX -self.speed
                self.rect =  self.rect.move(-self.speed,0)

            if (self._direction =="LEFT" and self._posX < 550):
                self._posX = self._posX +self.speed
                self.rect =  self.rect.move(self.speed,0)
    def moveDown(self):
        if ( self.enemyFlag == 0):
            self._posY = self._posY+10
            self.rect = self.rect.move(0,10) 
    
    def checkposX(self):
        if self._posX < 20:
            return 1
        if self._posY > 550:
            return -1
    
