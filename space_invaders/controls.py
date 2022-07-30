import pygame
import sys
import time
from bullet import Bullet
from invader import Invader
from constants import *


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


def update(bg_color, screen, stats, score, gun, invaders, bullets):
    screen.fill(bg_color)
    score.show()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    invaders.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, score, invaders, bullets):
    """Update bullets positions"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, invaders, True, True)
    if collisions:
        stats.score += 10 * len(*collisions.values())
        score.create()
    if len(invaders) == 0:
        bullets.empty()
        time.sleep(0.5)
        create_army(screen, invaders)


def update_invaders(stats, screen, invaders, gun, bullets):
    invaders.update()
    invaders_check_bottom(stats, screen, invaders, gun, bullets)


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


def gun_kill(stats, screen, invaders, gun, bullets):
    """Detect collision between invaders army and gun"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        invaders.empty()
        bullets.empty()
        create_army(screen, invaders)
        gun.create_gun()
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()


def invaders_check_bottom(stats, screen, invaders, gun, bullets):
    """Check if any of invaders are at the bottom of the screen"""
    screen_rect = screen.get_rect()
    for invader in invaders.sprites():
        if invader.rect.bottom > screen_rect.bottom - gun.rect.height - MARGIN:
            gun_kill(stats, screen, invaders, gun, bullets)
            break

