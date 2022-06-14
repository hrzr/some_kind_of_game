import pygame


class Invader(pygame.sprite.Sprite):
    """Describes single invader"""

    def __init__(self, screen):
        """Initiate and set starting position"""
        super(Invader, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("art/03_invader.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.rect.width * 3, self.rect.height * 3))
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def output(self):
        """Draw the invader"""
        self.screen.blit(self.image, self.rect)

