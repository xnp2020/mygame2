import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """描述外星人的类"""

    def __init__(self,bo_es):
        super().__init__()
        self.screen = bo_es.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = bo_es.settings
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        if self.rect.right >= self.screen_rect.right or self.rect.left <= self.screen_rect.left:
            return True