import pygame
import gun
import controls


def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space invaders")
    bg_color = (0, 0, 0)
    game_weapon = gun.Gun(screen)
    bullets = list()

    while True:
        controls.event_handler(screen, game_weapon, bullets)
        controls.bullets_update(bullets)
        game_weapon.move()
        controls.screen_update(bg_color, screen, game_weapon, bullets)


if __name__ == "__main__":
    run()
