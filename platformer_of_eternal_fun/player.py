import pygame
from config import *


class Player:
    """The class for describing main hero"""

    def __init__(self, screen, color=(255, 0, 0), bg_color=(0, 0, 0)):
        self.x = self.y = 50
        self.width = 40
        self.height = 60
        self.speed = 5
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color = color
        self.bg_color = bg_color
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def erase(self):
        pygame.draw.rect(self.screen, self.bg_color, (self.x, self.y, self.width, self.height))

    def events_handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == UP:
                self.move_up = True
            elif event.key == DOWN:
                self.move_down = True
            elif event.key == LEFT:
                self.move_left = True
            elif event.key == RIGHT:
                self.move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == UP:
                self.move_up = False
            elif event.key == DOWN:
                self.move_down = False
            elif event.key == LEFT:
                self.move_left = False
            elif event.key == RIGHT:
                self.move_right = False

    def move(self):
        if self.move_left or self.move_right or self.move_down or self.move_up:
            self.erase()
        if self.move_up and self.y >= self.screen_rect.top:
            self.y -= self.speed
        elif self.move_down and self.y <= self.screen_rect.bottom:
            self.y += self.speed
        if self.move_left and self.x >= self.screen_rect.left:
            self.x -= self.speed
        elif self.move_right and self.x <= self.screen_rect.right:
            self.x += self.speed
        self.draw()


