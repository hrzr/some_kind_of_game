import pygame
import sys


def event_handler(gun):
    """Handles all events that we get from the keyboard"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.move_right = True
            elif event.key == pygame.K_a:
                gun.move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.move_right = False
            elif event.key == pygame.K_a:
                gun.move_left = False



