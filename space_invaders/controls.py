import pygame
import sys


def event_handler(gun):
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



