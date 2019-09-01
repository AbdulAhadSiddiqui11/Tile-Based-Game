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
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.x = x * TILESIZE
        self.y = y * TILESIZE

    def get_keys(self):
        # Gets the value of key pressed
        self.vel_x, self.vel_y = 0,0
        # Velocities of x and y
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vel_x = - PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel_x =  PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vel_y = - PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel_y =  PLAYER_SPEED
        # To reduce the Velocities of diagonal movement!
        if self.vel_x != 0 and self.vel_y != 0:
            # If two keys (up,right) or (down,left) ... etc then reduce the speed
            self.vel_x *= 0.7071  # Diagonal from Pythagorous' theorem
            self.vel_y *= 0.7071

    def collision(self, direction):
        if direction == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel_x > 0: # Means player was moving right and hit the left side of the wall.
                    self.x = hits[0].rect.left - self.rect.width
                    # hits[0] -> hit is a hit, doesn't matter with which wall we collided with.
                if self.vel_x < 0 : # Player was moving left.
                    self.x = hits[0].rect.right
                self.vel_x = 0
                self.rect.x = self.x
        if direction == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel_y > 0: # Means player was moving down.
                    self.y = hits[0].rect.top - self.rect.height
                    # hits[0] -> hit is a hit, doesn't matter with which wall we collided with.
                if self.vel_y < 0 : # Player was moving up.
                    self.y = hits[0].rect.bottom
                self.vel_y = 0
                self.rect.y = self.y

    def update(self):
        # Draw the player at new coordinates
        self.get_keys()
        self.x += self.vel_x * self.game.dt
        self.y += self.vel_y * self.game.dt
        self.rect.x = self.x
        self.collision('x')
        self.rect.y = self.y
        self.collision('y')

class Wall(pg.sprite.Sprite):
    # Defines the chara of wall/ obstacle and inherits from Sprite class.
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill((117,164,225))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
