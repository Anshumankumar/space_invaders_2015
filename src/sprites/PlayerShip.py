import pygame
from Bullet import Bullet

class PlayerShip(pygame.sprite.Sprite):
    """The player's own ship"""

    def __init__(self, pos):
        """Initializes the player ship.
        
        arguments:
        pos --  a list consisting of x and y coordinate of player ship
        """
        self.image = pygame.image.load("images/player-sprite.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(*pos)
        # The player bullet 
        self.bullet = Bullet([0,0],"UP")
        
    def update(self,keys):
        """ Update the position of player ship based keys pressed

        arguments:
        keys -- A list consisting of keys preseed  
        """
        if ( keys[pygame.K_LEFT] and self.rect.x > 30 ):
            self.rect.move_ip(-8,0)
        if ( keys[pygame.K_RIGHT] and self.rect.x < 550 ):
            self.rect.move_ip(8,0)
        if ( keys[pygame.K_SPACE] and self.bullet.bulletFlag == 0):
            self.bullet = Bullet([self.rect.x+self.rect.width/2,
                                 self.rect.y-10],"UP")
            self.bullet.run()
