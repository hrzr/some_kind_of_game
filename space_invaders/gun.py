import pygame


class Gun:

    def __init__(self, screen):
        """Gun initialization"""
        self.screen = screen
        self.image = pygame.image.load("art/01_gun.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.margin = 10
        self.rect.bottom = self.screen_rect.bottom - self.margin
        self.move_right = False
        self.move_left = False

    def move(self):
        """Updates the gun's position on the screen"""
        if self.move_right and self.rect.right <= self.screen_rect.right - self.margin:
            self.center += 1.5
        elif self.move_left and self.rect.left >= self.screen_rect.left + self.margin:
            self.center -= 1.5
        self.rect.centerx = self.center

    def output(self):
        """Draw the gun"""
        self.screen.blit(self.image, self.rect)

    def create_gun(self):
        """Places a gun in the center of the screen"""
        self.center = self.screen_rect.centerx

