import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *

class Game:
    def __init__(self):
        pg.init()
        # Setting the screen size (Resolution)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(300, 100)
        self.load_data()

    def load_data(self):
        # Path for the game folder
        game_dir = path.dirname(__file__)
        # object consisting of map properties
        self.map = Map(path.join(game_dir, 'map2.txt'))


    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()


        for x in range(20, 40):
            # Draw a wall from
            Wall(self, x, 10)

        for row, tiles in enumerate(self.map.map_data):
            # for each row (line) get all the tiles(string of tiles)
            for col, tile in enumerate(tiles):
                # for each tile in that row check if its a wall at (col,row)
                if tile == 'w':
                    Wall(self,col,row)
                if tile == 'p':
                    self.player = Player(self, 10, 10)
        self.camera = Camera(self.map.width, self.map.height)


    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        # Exit the game and game window.
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        # Drawing a grid with width x height
        for x in range(0, WIDTH, TILESIZE):
            # line(surface, color, start_pos, end_pos, width = 1)
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        # Draw sprits, objects/obstacles and Background.
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        # Deals with all the outside inputs/ events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
