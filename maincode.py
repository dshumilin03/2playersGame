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
clock = pygame.time.Clock()
# </editor-fold>

image_dir = path.join(path.dirname(__file__), 'images')

player_image = pygame.image.load(path.join(image_dir, "player.png"))

game_is_running = True

all_sprites = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_image
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.speed = 2
        self.rect.x = 400
        self.rect.y = 400

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed


player = Player()

all_sprites.add(player)

while game_is_running is True:
    clock.tick(60)
    screen.fill(white)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
