import pygame
from Bullet import Bullet
shipcolor = 255,233,0

class PlayerShip(pygame.sprite.Sprite):
    """The player's own ship"""

    def __init__(self, pos):
        self.image = pygame.image.load("images/player-sprite.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(*pos)
        self.bullet = Bullet([0,0],"UP")
        
    def update(self,keys):
        if ( keys[pygame.K_LEFT] and self.rect.x > 30 ):
            self.rect.move_ip(-8,0)
        if ( keys[pygame.K_RIGHT] and self.rect.x < 550 ):
            self.rect.move_ip(8,0)
        if ( keys[pygame.K_SPACE] and self.bullet.bulletFlag == 0):
            self.bullet = Bullet([self.rect.x+self.rect.width/2,self.rect.y-10],"UP")
            self.bullet.run()
