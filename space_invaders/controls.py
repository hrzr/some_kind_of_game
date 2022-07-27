import pygame
import sys
from bullet import Bullet
from invader import Invader
from space_invaders import SCREEN_WIDTH, SCREEN_HEIGHT


def events(screen, gun, bullets):
    """Event handler"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                gun.move_right = True
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                gun.move_left = True
            elif event.key == pygame.K_SPACE:
                bullets.add(Bullet(screen, gun))
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                gun.move_right = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                gun.move_left = False


def update(bg_color, screen, gun, invaders, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    invaders.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    """Update bullets positions"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)


def update_invaders(invaders):
    invaders.update()


def create_army(screen, invaders):
    invader = Invader(screen)
    invader_width = invader.rect.width
    invader_height = invader.rect.height
    number_of_invaders_x = (SCREEN_WIDTH - 2 * invader_width) // invader_width
    number_of_invaders_y = (SCREEN_HEIGHT - 100 - 2 * invader_height) // invader_height
    for invaders_row in range(number_of_invaders_y - 1):
        for invaders_column in range(number_of_invaders_x):
            invader = Invader(screen)
            invader.x = invader_width + invader_width * invaders_column
            invader.y = invader_height + invader_height * invaders_row
            invader.rect.x = invader.x
            invader.rect.y = invader.rect.height + invader.rect.height * invaders_row
            invaders.add(invader)
