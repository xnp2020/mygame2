import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """描述子弹的类"""

    def __init__(self,bo_es):
        super().__init__()
        self.screen = bo_es.screen
        self.settings = bo_es.settings
        self.color = self.settings.bullet_color
        

        self.rect = pygame.Rect(0,0,bo_es.settings.bullet_width,bo_es.settings.bullet_height)
        self.rect.midtop = bo_es.boat.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)