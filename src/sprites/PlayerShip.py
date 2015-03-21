import pygame

white = 255,255,255

class PlayerShip(pygame.sprite.Sprite):
    """The player's own ship"""

    def __init__(self, width, height):
        self.image = pygame.Surface([width, height])
        self.image.fill(white)
        self.rect = self.image.get_rect()
