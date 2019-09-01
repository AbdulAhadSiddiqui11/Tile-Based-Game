import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    # Player class inherits from Sprtie class and defines player characteristics.
    def __init__(self, game, x, y):
        # Player belongs to all_sprites Group
        self.groups = game.all_sprites
        # Initilize the Sprite class with player's group.
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
<<<<<<< HEAD
        self.image.fill(BLUE)
=======
        self.image.fill(WHITE)
>>>>>>> Added wall collisions and map functionality
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

<<<<<<< HEAD
    def move(self, dx=0, dy=0):
        # Update the coordinates of player when called (KEYDOWN).
        self.x += dx
        self.y += dy
=======
    def move(self, dx = 0, dy = 0):
        # Check if there's a wall/obstacle on (dx,dy),
        # If not then update the coordinates of player when called (KEYDOWN).
        if not self.collision(dx,dy):
            self.x += dx
            self.y += dy

    def collision(self, dx = 0, dy = 0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy :
                return True
        return False
>>>>>>> Added wall collisions and map functionality

    def update(self):
        # Draw the player at new coordinates
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
    # Defines the chara of wall/ obstacle and inherits from Sprite class.
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
