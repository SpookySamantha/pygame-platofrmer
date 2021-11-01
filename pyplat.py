
# Music I think is neat is listed at the bottom :)
# I'm following a tutorial but will be adding my own comments to show understanding

# Foundation

# Initialization and constants

# Importing pygame

import pygame
from pygame.locals import *
import sys
 
pygame.init()

# Setting the dimensions as 2D along with setting screen size, accerlation, friction, and frames per second
 
vec = pygame.math.Vector2 
# ACC, and FRIC will be used for physiscs stuff
HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60
FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
 
# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
# Create a surface object with a fixed size 
        self.surf = pygame.Surface((30, 30))
# Give it a colour RGB
        self.surf.fill((128,255,40))
# Create a rect object from the surface, center is used to define a starting position
        self.rect = self.surf.get_rect(center = (10,100))
   
        self.pos = vec((10, 430))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
# Defining the move function
    def move(self):
# Resets the accerlation rate to 0
        self.acc = vec(0,0)
# Checks for key presses and changes acceraltion accordingly
        pressed_keys = pygame.key.get_pressed()            
        if pressed_keys[K_a]:
            self.acc.x = -ACC
        if pressed_keys[K_d]:
            self.acc.x = ACC
# Code that I don't fully understand however it's about friction so messing around with FRIC
# should make the friction more or less. I'm very good at explaining stuff
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

#Screen wrapping code!
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
            
        self.rect.midbottom = self.pos    

# Platform class
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
 
PT1 = platform()
P1 = Player()
 
# Creating a general sprite group and adding the player and the platform classes
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

# Main while loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
# Refreshes the display     
    displaysurface.fill((0,0,0))
 # Lets the player move and then draws all the sprites to the screen
    P1.move()
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
    
    pygame.display.update()
    FramePerSec.tick(FPS)



# Music listened to while working on this project:

# Singles:
# Glass Animals : Heat Waves (with iann dior)
# Vantage : 50//50

# Albums:
# Glass Animals : How To Be A Human Being
# Glass Animals : Dreamland (+ Bonus Levels)
# Vantage : Metro City
# Vantage : Aloha Island
