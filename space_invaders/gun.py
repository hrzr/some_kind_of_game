import pygame


class Gun:

    def __init__(self, screen):
        """Gun initialization"""
        self.screen = screen
        self.image = pygame.image.load("art/01_gun.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False

    def output(self):
        """Draw the gun"""
        self.screen.blit(self.image, self.rect)

    def move(self):
        """Updates the gun's position on the screen"""
        if self.move_right:
            self.rect.centerx += 1
        elif self.move_left:
            self.rect.centerx -= 1
