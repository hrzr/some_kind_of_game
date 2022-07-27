import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """Create bullet at gun"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 0, 255, 0
        self.speed = 1.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top + 60
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw a bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
