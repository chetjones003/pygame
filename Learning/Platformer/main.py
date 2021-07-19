import sys
import pygame
from pygame.locals import *

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption("Platformer")

WINDOW_SIZE = (400, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

player_image = pygame.image.load("player.png")

# Game Loop
while True:
    screen.blit(player_image, (50, 50))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
