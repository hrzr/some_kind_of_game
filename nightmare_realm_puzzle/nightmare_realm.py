# TODO: develop game logic
# TODO: develop graphics
# TODO: develop music
# TODO: develop interface
import pygame
import sys
from constants import *
from gamefield import GameField


def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Nightmare realm")
    bg_color = 0, 0, 0
    game_field = GameField(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        game_field.draw()
        pygame.display.flip()


if __name__ == "__main__":
    run()
