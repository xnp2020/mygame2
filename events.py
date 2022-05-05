import pygame

import sys

class Py_events:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200,800))
        self.bg_color = (255,255,255)


    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    else:
                        print(event.key)

            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    ins1 = Py_events()
    ins1.run_game()