import pygame

speed = 1

class BossEnemy(pygame.sprite.Sprite):
    """A rare but highly valuable enemy ship"""

    def __init__(self, pos):
        self.image = pygame.image.load('images/boss-sprite.png')
        self.rect = self.image.get_rect()
        self.rect.move_ip(*pos)

    def update(self):
        self.rect.move_ip(speed, 0)
