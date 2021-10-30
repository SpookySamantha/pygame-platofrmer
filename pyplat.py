# Music I think is neat is listed at the bottom :)
# I'm following a tutorial but will be adding my own comments to show understanding

# Foundation

# Initialization and constants

# Importing pygame

import pygame
from pygame.locals import *

pygame.init()

# Setting the dimensions as 2D (Vector2)

vec = pygame.math.Vector2 

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

# vec, ACC, and FRIC will be used for physiscs stuff

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')

# Player and Platform Classes

# Player class

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
# Create a surface object with a fixed size
        self.surf = pygame.Surface((30,30))
# Give it a colour (RGB format)
        self.surf.fill((128,255,40))
# Create a rect object from the surface, centre is used to define a starting position
        self.rect = self.surf.get_rect(center = (10,420))

        self.pos = vec((10, 385))
        self.vel = vec((0,0))
        self.acc = vec((0,0))

# Platform class
# Won't comment on this as it'd be redundant

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))

PT1 = Platform()
P1 = Player()

# Creating a general sprite group and adding the player and the platform

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

# While loop to see the quit event and shutdown

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

# Refreshing the screen with each itteration
    displaysurface.fill((0,0,0))

# Drawing all sprites to the screen

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

# Pushing all changes to the screen, tick rate has been set to 60 a second matching the framerate
# We set earlier.

    pygame.display.update()
    FramePerSec.tick(FPS)

# Music listened to while working on this project:

# Singles:
# Glass Animals : Heat Waves (with iann dior)

# Albums:
# Glass Animals : How To Be A Human Being
# Glass Animals : Dreamland (+ Bonus Levels)
# Vantage : Metro City
