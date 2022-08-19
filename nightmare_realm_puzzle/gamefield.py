import pygame
from constants import *


class Tile:

    __sprite = "art/04_box.png"
    __aspect = 4

    def __init__(self, screen, left, top):
        self.screen = screen
        self.img = pygame.image.load(self.__sprite)
        self.rect = self.img.get_rect()
        self.img = pygame.transform.scale(
            self.img,
            (self.rect.width * self.__aspect, self.rect.height * self.__aspect)
        )
        self.rect = self.img.get_rect()
        self.rect.top = top + MARGIN
        self.rect.left = left + MARGIN

    def draw(self):
        self.screen.blit(self.img, self.rect)


class GameField:

    def __init__(self, screen):
        self.screen = screen
        self.game_field = list()
        tile_width = Tile(self.screen, 0, 0).rect.width
        tile_height = Tile(self.screen, 0, 0).rect.height
        for y in range(5):
            self.game_field.append(list())
            for x in range(5):
                self.game_field[y].append(Tile(self.screen, x * tile_width, y * tile_height))

    def draw(self):
        for line in self.game_field:
            for tile in line:
                tile.draw()

