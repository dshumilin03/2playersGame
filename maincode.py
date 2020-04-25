# <editor-fold desc="imports">
import pygame
import sys
import math
from os import path
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

image_dir = path.join(path.dirname(__file__), 'images')

pygame.image.load(image_dir)

game_is_running = True

while game_is_running is True:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

# It's better to extract this class into separate file
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = 10
        self.height = 10
