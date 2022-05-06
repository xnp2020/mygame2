
import pygame


class Boat:
    """描述船的类"""

    def __init__(self, bo_es):
        self.screen = bo_es.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/boat.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #移动速度
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.boat_speed = bo_es.settings.boat_speed

    def boat_blit(self):
        self.screen.blit(self.image, self.rect)

    def boat_moving(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.boat_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.boat_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.boat_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.boat_speed 
        self.rect.x = self.x
        self.rect.y = self.y

    def to_center(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)