import pygame
import thread
import time

BULLETCOLOR = 100,233,233
SIZE = [4,10]

class Bullet(pygame.sprite.Sprite):
    """Player and opponent weapon"""
    bulletFlag = 0
    def __init__(self, pos, direction):
        self.image = pygame.Surface(SIZE)
        self.image.fill(BULLETCOLOR)
        self.rect = self.image.get_rect()
        self._direction = direction
        pos[0] -= SIZE[0]/2
        self.rect.move_ip(*pos)

    def run(self):
        self.bulletFlag = 1
        thread.start_new_thread(self.update,())

    def update(self):
        while ( self.rect.y > 10 and self.rect.y < 400 ):
            if (self.bulletFlag == 0):
                break
            if (self._direction =="UP"):
                self.rect.move_ip(0,-10)
            if (self._direction =="DOWN"):
                self.rect.move_ip(0,10)
            time.sleep(0.05)
        #Remove bullet from screen
        self.bulletFlag = 0
