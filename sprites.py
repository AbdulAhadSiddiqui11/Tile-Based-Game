import pygame as pg
from settings import *
vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
    # Player class inherits from Sprtie class and defines player characteristics.
    def __init__(self, game, x, y):
        # Player belongs to all_sprites Group
        self.groups = game.all_sprites
        # Initilize the Sprite class with player's group.
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # Creating local vars for directional player sprites
        self.img_right, self.img_left, self.img_up, self.img_down = game.player_sprite_right,\
         game.player_sprite_left, game.player_sprite_up, game.player_sprite_down
        self.image = game.player_sprite_right # Loading player sprite into player object
        self.rect = self.image.get_rect()
        self.velocity = vec(0,0) # Defining velocity and position vectors
        self.position = vec(x,y) * TILESIZE

    def get_keys(self):
        # Gets the value of key pressed
        self.velocity = vec(0,0)
        # Velocities of x and y
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.velocity.x = - PLAYER_SPEED
            self.image = self.img_left
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.velocity.x =  PLAYER_SPEED
            self.image = self.img_right
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.velocity.y = - PLAYER_SPEED
            self.image = self.img_up
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.velocity.y =  PLAYER_SPEED
            self.image = self.img_down
        # To reduce the Velocities of diagonal movement!
        if self.velocity.x != 0 and self.velocity.y != 0:
            # If two keys (up,right) or (down,left) ... etc then reduce the speed
            self.velocity *= 0.7071  # Diagonal from Pythagorous' theorem

    def collision(self, direction):
        if direction == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.velocity.x > 0: # Means player was moving right and hit the left side of the wall.
                    self.position.x = hits[0].rect.left - self.rect.width
                    # hits[0] -> hit is a hit, doesn't matter with which wall we collided with.
                if self.velocity.x < 0 : # Player was moving left.
                    self.position.x = hits[0].rect.right
                self.velocity.x = 0
                self.rect.x = self.position.x
        if direction == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.velocity.y > 0: # Means player was moving down.
                    self.position.y = hits[0].rect.top - self.rect.height
                    # hits[0] -> hit is a hit, doesn't matter with which wall we collided with.
                if self.velocity.y < 0 : # Player was moving up.
                    self.position.y = hits[0].rect.bottom
                self.velocity.y = 0
                self.rect.y = self.position.y

    def update(self):
        # Draw the player at new coordinates
        self.get_keys()
        self.position += self.velocity * self.game.dt
        self.rect.x = self.position.x
        self.collision('x')
        self.rect.y = self.position.y
        self.collision('y')

class Obstacle(pg.sprite.Sprite):
    # Defines the chara of wall/ obstacle and inherits from Sprite class.
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

"""class Wall(pg.sprite.Sprite):
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
        self.rect.y = y * TILESIZE"""
