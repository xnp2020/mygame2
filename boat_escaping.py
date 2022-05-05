import pygame

import sys

from boat import Boat
from bullet import Bullet
from settings import Settings

class Boat_escaping:
    """boat escaping主类"""

    def __init__(self):
        pygame.init()
        self.settings = Settings(self)

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.bg_color = self.settings.bg_color

        pygame.display.set_caption("Boat escaping")

        self.boat = Boat(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.boat.boat_moving()
            self._update_bullets()
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.boat.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.boat.moving_left = True
                elif event.key == pygame.K_UP:
                    self.boat.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.boat.moving_down = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.boat.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.boat.moving_left = False
                elif event.key == pygame.K_UP:
                    self.boat.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.boat.moving_down = False

    def _fire_bullet(self):
        #创建子弹列表
        if len(self.bullets) < self.settings.bullets_allowed:  #限制子弹数量
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        #删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0 :
                self.bullets.remove(bullet)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.boat.boat_blit()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

if __name__ == '__main__':
    boes = Boat_escaping()
    boes.run_game()