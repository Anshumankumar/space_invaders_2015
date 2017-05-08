import pygame
import _thread
import time
from random import randint

BULLETCOLOR = 100,233,233
SIZE = [4,10]

class Bullet(pygame.sprite.Sprite):
    """Player and opponent weapon"""
    bulletFlag = 0
    def __init__(self, pos, direction, isEnemyBullet=True):
        self.image = pygame.Surface(SIZE)
        self.image.fill(BULLETCOLOR)
        self.rect = self.image.get_rect()
        self._direction = direction
        pos[0] -= SIZE[0]/2
        self.rect.move_ip(*pos)
        self.isEnemyBullet = isEnemyBullet

    def run(self):
        self.bulletFlag = 1
        _thread.start_new_thread(self.update,())

    def update(self):
        while ( self.rect.y > 10 and self.rect.y < 380 ):
            if (self.bulletFlag <= 0):
                return
            if (self._direction =="UP"):
                self.rect.move_ip(0,-10)
            if (self._direction =="DOWN"):
                self.rect.move_ip(0,8)
            time.sleep(0.05)

        #For resurrecting bullets
        if self.isEnemyBullet:
            self.bulletFlag = randint(-20, 0)
            while self.bulletFlag < 0:
                time.sleep(0.1)
                self.bulletFlag += 1
        else:
            self.bulletFlag = 0
