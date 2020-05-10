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

bullet_size = (5, 10)

fps = 60

bullet_dist = 5 #this is a distance between player and bullet when player shoots

all_sprites = pygame.sprite.Group()

objects = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_image
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.speed = 3
        self.rect.x = Width // 2 - self.rect.width // 2
        self.rect.y = Height - 2 * self.rect.height

    def shoot(self):
        all_sprites.add(Bullet(self.rect.centerx - bullet_size[0] // 2, self.rect.top - 2 * bullet_dist, 1))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >= 5:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right <= Width - 5:
            self.rect.x += self.speed


class SecondPlayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_image
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.speed = 3
        self.rect.x = Width // 2 - self.rect.width // 2
        self.rect.y = self.rect.height

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP4] and self.rect.left >= 5:
            self.rect.x -= self.speed
        if keys[pygame.K_KP6] and self.rect.right <= Width - 5:
            self.rect.x += self.speed

    def shoot(self):
        all_sprites.add(Bullet(self.rect.centerx - bullet_size[0] // 2, self.rect.bottom + bullet_dist, 2))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, num):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_image, (bullet_size[0], bullet_size[1]))
        self.rect = self.image.get_rect()
        self.speed = 15
        self.rect.x = x  # x from input as you see
        self.rect.y = y  # y from input as you see
        self.player = num  # who is shooting ( number of player )

    def update(self):
        hit = pygame.sprite.spritecollide(self, objects, False)
        if self.player == 2:
            self.rect.y += self.speed
        elif self.player == 1:
            self.rect.y -= self.speed
        if self.rect.top >= Height or self.rect.bottom <= 0 or hit:
            self.kill()


class Wall(pygame.sprite.Sprite):
    def __init__(self,x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def spawning_walls():
    for i in range(0, 800, 200):
        current_wall = Wall(50 + i, 150)
        all_sprites.add(current_wall)
        objects.add(current_wall)
    for i in range(0, 800, 200):
        current_wall = Wall(50 + i, 400)
        all_sprites.add(current_wall)
        objects.add(current_wall)
spawning_walls()

player = Player()
player2 = SecondPlayer()

all_sprites.add(player2)
all_sprites.add(player)
objects.add(player)
objects.add(player2)

while game_is_running is True:
    clock.tick(fps)
    screen.fill(white)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP8:
                player2.shoot()
            if event.key == pygame.K_UP:
                player.shoot()

    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
