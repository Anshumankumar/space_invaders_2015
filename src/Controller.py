import pygame
import time
from copy import copy
from random import randint
from sprites import *

class Controller():
    _score = 0;
    _lives = 3;
    def __init__(self,n,m,screen):
        self._font = pygame.font.SysFont("monospace", 16)
        self.scoretext = self._font.render("Score = "+str(self._score), 1, (0,255,0))
        self.lifetext = self._font.render("Lives = "+str(self._lives), 1, (0,255,0))
        self._screen = screen
        self._rowNo = n;
        self._columnNo = m;
        self.direction ="LEFT"
        self.moveDownFlag = 0
        self.enemyArray = []
        for i in range(self._rowNo):
            self.enemyArray.append([])
            for j in range(self._columnNo):
                enemy1 = Enemy([15,10],[60+i*30,80+j*25],1)
                self.enemyArray[i].append(copy(enemy1))
        self.bullet = []
        for i in range(0,3):
            self.bullet.append(Bullet([0,0],"DOWN"))
    
    def bulletUpdate(self,i):
        if self.bullet[i].bulletFlag == 0:
            random_row = randint(0,self._rowNo-1)
            random_column = randint(0,self._columnNo-1)
            if (self.enemyArray[random_row][random_column]. \
                    enemyFlag != 1):
                return
            bullet_x = self.enemyArray[random_row][random_column].rect.x
            bullet_y = self.enemyArray[random_row][random_column].rect.y
            self.bullet[i] = Bullet([bullet_x,bullet_y],"DOWN")
            self.bullet[i].run()
    
    def blit(self):
        for i in range(0,3):
            self.bulletUpdate(i)
            self._screen.blit(self.bullet[i].image,self.bullet[i].rect)
        self.moveDownFlag =  self.moveDownFlag +1
        self.flipDirection()
        self._screen.blit(self.scoretext,(50,50))
        self._screen.blit(self.lifetext,(450,50))
        for enemylist in self.enemyArray:
            for enemy in enemylist:
                if (enemy.enemyFlag == 1):
                    enemy.updateDirection(self.direction)
                    self._screen.blit(enemy.image,enemy.rect)
                    enemy.update()
                    if (self.moveDownFlag  == 200):
                        enemy.moveDown();
        if (self.moveDownFlag  == 200):
            self.moveDownFlag = 0



    def flipDirection(self):
        for enemylist in self.enemyArray:
            for enemy in enemylist:
                if (enemy.enemyFlag == 1):
                    if (enemy.checkposX() == 1):
                        self.direction = "LEFT"
                    if (enemy.checkposX() == -1):
                        self.direction = "RIGHT";

    def collision(self,bullet):
        for enemylist in self.enemyArray:
            for enemy in enemylist: 
                self.collision_check(enemy,bullet)

    def collision_check(self,enemy,bullet):
        if (enemy.enemyFlag == 1):
            if bullet.bulletFlag and enemy.rect.colliderect(bullet.rect):
                enemy.enemyFlag = 0
                enemy.rect =None
                bullet.bulletFlag = 0
                self._score = self._score + 100;
                self.scoretext = self._font.render("Score = "+str(self._score), 1, (0,255,0))
                self._screen.blit(self.scoretext,(50,50))
    
    def player_collision_check(self,player):
        for cbullet in self.bullet:
            if player.rect.colliderect(cbullet.rect):
                self._lives = self._lives -1;
                self.lifetext = self._font.render(
                        "Lives = "+str(self._lives), 1, (0,255,0))
                cbullet.bulletFlag = 0
    
    def gameover(self):
        if self._lives  < 0:
            return True
        else:
            return False
