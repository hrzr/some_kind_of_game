import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """Create a bullet at the gun center position"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("art/02_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = gun.rect.centerx
        self.speed = 1.5
        self.rect.top = gun.rect.top + 50
        self.y = float(self.rect.y)

    def move(self):
        """Movement logic of the bullet"""
        self.y -= self.speed
        self.rect.centery = self.y

    def output(self):
        """Draw the bullet on the screen"""
        self.screen.blit(self.image, self.rect)




