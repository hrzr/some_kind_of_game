import pygame
import controls
from gun import Gun
from pygame.sprite import Group

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 700


def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Space invaders")
    bg_color = 0, 0, 0
    gun = Gun(screen)
    bullets = Group()
    invaders = Group()
    controls.create_army(screen, invaders)

    while True:
        controls.events(screen, gun, bullets)
        gun.move()
        bullets.update()
        controls.update(bg_color, screen, gun, invaders, bullets)
        controls.update_bullets(bullets)
        controls.update_invaders(invaders)




if __name__ == "__main__":
    run()