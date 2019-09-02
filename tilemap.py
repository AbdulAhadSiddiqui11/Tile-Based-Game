import pygame as pg
import pytmx
from settings import *


# Defining a general class for accessing multiple map files
class Map:
    def __init__(self, mapfile):
        # Empty list to store map map_data
        self.map_data = []
        # Open the map file
        with open(mapfile, 'r') as map:
            for line in map:
                # Each line is a string
                self.map_data.append(str(line).strip('\n'))

        # Height and width of the map based on the number of tiles
        self.tilewidth = len(self.map_data[0])
        self.tileheight = len(self.map_data)
        # Height and Width of the Map in pixels
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class TiledMap:
    ''' Class TiledMap used to read an entire map from tmx file '''
    def __init__ (self,filename):
        # Loading the tiledmap file
        tiledmap = pytmx.load_pygame(filename, pixelalpha = True) # pixelalpha = True for transparent background
        self.width = tiledmap.width * tiledmap.tilewidth # width is how many tiles and tilewidth is how many pixels wide is each tile
        self.height = tiledmap.height * tiledmap.tileheight
        self.tmx_data = tiledmap # Storing the map in a local var.

    def render(self, surface):
        get_ti = self.tmx_data.get_tile_image_by_gid # get_ti -> alias for this line
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer): # Check if it's a tile layer.
                for x,y,gid in layer:
                    tile = get_ti(gid) # for each tile; if its a tile, draw the tile
                    if tile :
                        surface.blit(tile,(x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight))

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        # Creater a temporary surface for render method to draw the tiles on.
        self.render(temp_surface)
        return temp_surface


class Camera:
    def __init__(self, width, height):
        # Using Rectangle to keep track of the camera
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        # Movement of the camera, Gives new rectangle/camera which is shifted due to movement of the player
        # Can only be used on a sprite
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        # Instead of a player (sprite)r this method can be used on anybody's rect.
        return rect.move(self.camera.topleft)

    def update(self, target):
        # X and Y are co ordinates, where camera is to be shifted due to movement of the Player
        # target = player / any sprite
        # If player moves to the right then offset/map moves in opposite direction
        # Wdith / 2, Height / 2 is to keep the player in the middle of the camera
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        # Limit scrolling to map size
        x = min(0, x) # limit left scrolling
        y = min(0, y) # limit top scrolling
        x = max(-(self.width - WIDTH), x) # limit right scrolling
        y = max(-(self.height - HEIGHT), y) # limit bottom scrolling
        # Updating the camera after the movemnet of the player
        self.camera = pg.Rect(x, y, self.width, self.height)
