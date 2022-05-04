import pygame

import sys

from boat import Boat

class Boat_escaping:
    """boat escaping主类"""

    def __init__(self):
        self.screen = pygame.display.set_mode((1200,800))
        self.bg_color = (255,128,255)

        pygame.display.set_caption("Boat escaping")

        self.boat = Boat(self)

    def run_game(self):
        while True:
            self._check_events()
            self.boat.boat_moving()
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
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.boat.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.boat.moving_left = False
                elif event.key == pygame.K_UP:
                    self.boat.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.boat.moving_down = False
                    
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.boat.boat_blit()
        pygame.display.flip()

if __name__ == '__main__':
    boes = Boat_escaping()
    boes.run_game()