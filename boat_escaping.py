import pygame

import sys
from time import sleep
import json

from boat import Boat
from bullet import Bullet
from settings import Settings
from alien import Alien
from game_stats import Gamestats
from button import Button
from scoreboard import Scoreboard

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
        self.aliens = pygame.sprite.Group()
        self.stats = Gamestats(self)
        self.sb = Scoreboard(self)

        self._create_fleet()

        self.play_button = Button(self, "play")

    def _create_fleet(self):
        #根据屏幕计算并创建外星人
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien_number_per_row = (self.settings.screen_width - (2 * alien_width)) // (2 * alien_width)
        alien_number_per_column = (self.settings.screen_height - self.boat.rect.height - 3 * alien_height) // (2 * alien_height)
        for counts_per_row in range(alien_number_per_row):
            for counts_per_col in range(alien_number_per_column):
            
                self._create_alien(counts_per_row,counts_per_col)

    def _create_alien(self,counts_per_row,counts_per_col):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * counts_per_row
        alien.y = alien_height + 2 * alien_height * counts_per_col
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)
        
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _ship_hit(self):
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
            self.sb.prep_boats()
            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.boat.to_center()

            sleep(0.5)
        else:
            pygame.mouse.set_visible(True)
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """检查是否有外星人到底了屏幕底部"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.boat,self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.boat.boat_moving()
                self._update_aliens()
                self._update_bullets()
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                self._write_score()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _write_score(self):
        filename = 'score.json'
        with open(filename,'w') as f:
            json.dump(self.stats.high_score,f)
        sys.exit()        

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
        #删除发生碰撞的子弹、外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,True,True)
        #如果外星人没有了，清空子弹，重新创建外星人
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.boat.boat_blit()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _check_keydown(self,event):
        if event.key == pygame.K_RIGHT:
            self.boat.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.boat.moving_left = True
        elif event.key == pygame.K_UP:
            self.boat.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.boat.moving_down = True
        elif event.key == pygame.K_q:
            self._write_score()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        
    def _check_keyup(self,event):
        if event.key == pygame.K_RIGHT:
            self.boat.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.boat.moving_left = False
        elif event.key == pygame.K_UP:
            self.boat.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.boat.moving_down = False
    
    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            #隐藏鼠标光标
            pygame.mouse.set_visible(False)
            self.boat.to_center()
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet() #不加这行也会创建外星人大军，因为在_update_bullets调用了此方法，书上是有这行
            self.stats.reset_stats()
            self.stats.game_active = True
            self.settings.initialize_dynamic_settings()
            self.sb.prep_level()
            self.sb.prep_score()
            self.sb.prep_boats()

if __name__ == '__main__':
    boes = Boat_escaping()
    boes.run_game()