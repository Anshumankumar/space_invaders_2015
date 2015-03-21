import pygame

white = 255,255,255

class PlayerShip(pygame.sprite.Sprite):
    """The player's own ship"""

    def __init__(self, size, pos):
        self.image = pygame.Surface(size)
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self._posX = pos[0]
        self._posY = pos[1]
        self.rect = self.rect.move(self._posX,self._posY)
        
    def update(self,keys):
        if ( keys[pygame.K_LEFT] and self._posX > 30 ):
            self._posX = self._posX -8
            self.rect =  self.rect.move(-8,0)
        if ( keys[pygame.K_RIGHT] and self._posX < 570 ):
            self._posX = self._posX +8
            self.rect =  self.rect.move(8,0)
        
