import pygame.font
from constants import *


class Scores:
    """Game info output"""

    def __init__(self, screen, stats):
        """Initiate score count"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = 0, 255, 0
        self.font = pygame.font.SysFont("Courier", 36)
        self.score_image = None
        self.score_rect = None
        self.create()
        self.show()

    def create(self):
        """Create score to show on the screen"""
        self.score_image = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - MARGIN
        self.score_rect.top = self.screen_rect.top + MARGIN

    def show(self):
        """Shows score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
