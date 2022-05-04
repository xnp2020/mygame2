
import pygame


class Boat:
    """描述船的类"""

    def __init__(self, bo_es):
        self.screen = bo_es.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/boat.bmp')
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen_rect.center

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def boat_blit(self):
        self.screen.blit(self.image, self.image_rect)

    def boat_moving(self):
        if self.moving_right:
            self.image_rect.x += 1
        if self.moving_left:
            self.image_rect.x -= 1
        if self.moving_down:
            self.image_rect.y += 1
        if self.moving_up:
            self.image_rect.y -= 1 