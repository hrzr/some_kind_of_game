import pygame
import controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from constants import *


def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Space invaders")
    bg_color = 0, 0, 0
    gun = Gun(screen)
    bullets = Group()
    invaders = Group()
    controls.create_army(screen, invaders)
    stats = Stats()
    score = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.move()
            controls.update(bg_color, screen, stats, score, gun, invaders, bullets)
            controls.update_bullets(screen, stats, score, invaders, bullets)
            controls.update_invaders(stats, screen, score, invaders, gun, bullets)


if __name__ == "__main__":
    run()
