import pygame
import thread
import time

bulletcolor = 100,233,233

class Bullet(pygame.sprite.Sprite):
    """Player and opponent weapon"""
    bulletFlag = 0
    def __init__(self, size, pos, direction):
        self.image = pygame.Surface(size)
        self.image.fill(bulletcolor)
        self.rect = self.image.get_rect()
        self._posX = pos[0]
        self._posY = pos[1]
        self._direction = direction
        self.rect = self.rect.move(self._posX,self._posY)
    
    def run(self):
        self.bulletFlag = 1
        thread.start_new_thread(self.update,())

    def update(self):
        while ( self._posY > 10 and self._posY < 400  ):
            if (self.bulletFlag == 0):
                break
            if (self._direction =="UP"):
                self._posY = self._posY -10
                self.rect =  self.rect.move(0,-10)

            if (self._direction =="DOWN"):
                self._posY = self._posY +10
                self.rect =  self.rect.move(0,10)
            time.sleep(0.05)
        self.rect = self.rect.move(-self._posX,-self._posY)
        self.bulletFlag = 0


