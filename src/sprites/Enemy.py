import pygame
import thread
import time

enemycolor = 0,255,0

class Enemy(pygame.sprite.Sprite):
    """Player and opponent weapon"""

    #This flag see wether a enemy is alive
    enemyFlag = 0
    
    def __init__(self, size, pos, speed):
        """ Intialises the  enemy

        arguments:
        size --  A  list consisiting of length and breadth of enemy
        pos -- A list consisting the position in x and y
        speed -- The speed with which the enemy move in x direction
        """
        self.enemyFlag = 1
        self.image = pygame.Surface(size)
        self.image.fill(enemycolor)
        self.rect = self.image.get_rect()
        self.speed  = speed
        self.rect.move_ip(*pos)
        self._direction = "RIGHT"

    def updateDirection(self,direction):
        self._direction = direction
    
    def run(self):
        self.enemyFlag = 1
        thread.start_new_thread(self.update,())

    def update(self):
        if  ( self.enemyFlag == 1 ):
            if (self._direction =="RIGHT" and self.rect.x > 20):
                self.rect.move_ip(-self.speed,0)

            if (self._direction =="LEFT" and self.rect.x < 550):
                self.rect.move_ip(self.speed,0)
    
    def moveDown(self):
        if ( self.enemyFlag == 1):
            self.rect.y = self.rect.y+10
            self.rect = self.rect.move(0,10) 
    
    def checkposX(self):
        if self.rect.x < 40:
            return 1
        if self.rect.x > 540:
            return -1
        else:
            return 0
    
