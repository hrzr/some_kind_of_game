import pygame.font
from gun import Gun
from pygame.sprite import Group
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
        self.high_score_image = None
        self.high_score_rect = None
        self.lives_image = None
        self.lives_rect = None
        self.guns = None
        self.create()
        self.create_high_score()
        self.create_lives()
        self.show_score()

    def create(self):
        """Create score to show on the screen"""
        self.score_image = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - MARGIN
        self.score_rect.top = self.screen_rect.top + MARGIN

    def show_score(self):
        """Shows score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.guns.draw(self.screen)

    def create_high_score(self):
        """Show high score on the screen"""
        self.high_score_image = self.font.render(f"HIGH SCORE: {str(self.stats.high_score)}", True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + MARGIN

    def create_lives(self):
        """Show lives"""
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            # the gun is 100x40
            gun.image = pygame.transform.scale(gun.image, (50, 20))
            gun.rect = gun.image.get_rect()
            gun.rect.x = MARGIN + gun_number * (gun.rect.width + 6)
            gun.rect.centery = self.high_score_rect.centery
            self.guns.add(gun)
