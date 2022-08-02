import pygame
from player import Player
from controls import handle_events

pygame.init()
main_window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("platformer of eternal fun")

player = Player(main_window)

run = True
while run:
    pygame.time.delay(50)
    run = handle_events(player)
    player.move()
    pygame.display.update()

pygame.quit()