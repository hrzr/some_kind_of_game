import pygame
import sys
import bullet


def event_handler(screen, gun, bullets):
    """Handles all events that we get from the keyboard"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # move right
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                gun.move_right = True
            # move left
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                gun.move_left = True
            elif event.key == pygame.K_SPACE:
                new_bullet = bullet.Bullet(screen, gun)
                bullets.append(new_bullet)
            # exit on esc
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.KEYUP:
            # stop moving right
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                gun.move_right = False
            # stop moving left
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                gun.move_left = False


def screen_update(bg_color, screen, gun, bullets):
    """Updates game screen"""
    screen.fill(bg_color)
    for bullet in bullets:
        bullet.output()
    gun.output()
    pygame.display.flip()


def bullets_update(bullets):
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        else:
            bullet.move()

