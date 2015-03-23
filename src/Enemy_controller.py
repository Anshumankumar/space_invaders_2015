import pygame
import time
from sprites import *

class Enemy_controller():
    def __init__(self,n,m,screen):
        self._screen = screen
        self._rowNo = n;
        self._columnNo = m;
        self.enemyArray = []
        for i in range(self._rowNo):
            self.enemyArray.append([])
            for j in range(self._columnNo):
                enemy1 = Enemy([15,10],[60+i*20,80+j*15],2)
                self.enemyArray[0].append(enemy1)
              #  self.enemyArray[i].append(1)
    
    def blit(self):
        for enemylist in self.enemyArray:
            for enemy in enemylist:
                self._screen.blit(enemy.image,enemy.rect)
