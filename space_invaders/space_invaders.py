import pygame
import gun
import controls


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space invaders")
    bg_color = (0, 0, 0)
    game_weapon = gun.Gun(screen)

    while True:
        controls.event_handler(game_weapon)
        game_weapon.move()
        screen.fill(bg_color)
        game_weapon.output()
        pygame.display.flip()


run()
