import pygame
from Bullet import Bullet
shipcolor = 255,233,0

class PlayerShip(pygame.sprite.Sprite):
    """The player's own ship"""

    def __init__(self, size, pos):
        self.image = pygame.Surface(size)
        self.image.fill(shipcolor)
        self.rect = self.image.get_rect()
        self._posX = pos[0]
        self._posY = pos[1]
        self.rect = self.rect.move(self._posX,self._posY)
        self.bullet = Bullet([4,10],[0,0],"UP")
        
    def update(self,keys):
        if ( keys[pygame.K_LEFT] and self._posX > 30 ):
            self._posX = self._posX -8
            self.rect =  self.rect.move(-8,0)
        if ( keys[pygame.K_RIGHT] and self._posX < 550 ):
            self._posX = self._posX +8
            self.rect =  self.rect.move(8,0)
        if ( keys[pygame.K_SPACE] and self.bullet.bulletFlag == 0):
            self.bullet = Bullet([4,10],[self._posX+10,self._posY-10],"UP")
            self.bullet.run()
