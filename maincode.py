# <editor-fold desc="imports">
import pygame
import sys
import math
# </editor-fold>

pygame.display.init()

# <editor-fold desc="Colors">
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
# </editor-fold>

# <editor-fold desc="Screen settings">
Width = 800
Height = 600
screen = pygame.display.set_mode((Width, Height))
# </editor-fold>

game_is_running = True

while game_is_running is True:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 10
        self.height = 10

