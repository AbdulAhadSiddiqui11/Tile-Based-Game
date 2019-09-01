import pygame as pg
import sys
<<<<<<< HEAD
=======
from os import path
>>>>>>> Added wall collisions and map functionality
from settings import *
from sprites import *

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
<<<<<<< HEAD
        pass
=======
        # Path for the game folder
        game_dir = path.dirname(__file__)
        # Empty list to store map map_data, availale throught the game class (self)
        self.map_data = []
        # Open the map file
        with open (path.join(game_dir, 'map.txt'), 'r') as map:
            for line in map:
                # Each line is a string
                self.map_data.append(str(line).strip('\n'))
>>>>>>> Added wall collisions and map functionality

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player = Player(self, 10, 10)
<<<<<<< HEAD
        for x in range(20, 40):
            # Draw a wall from
            Wall(self, x, 10)
=======
        for row, tiles in enumerate(self.map_data):
            # for each row (line) get all the tiles(string of tiles)
            for col, tile in enumerate(tiles):
                # for each tile in that row check if its a wall at (col,row)
                if tile == 'w':
                    Wall(self,col,row)
>>>>>>> Added wall collisions and map functionality

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
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # Deals with all the outside inputs/ events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                # If key is pressed check for which key.
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx = -1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx = 1)
                if event.key == pg.K_UP:
                    self.player.move(dy = -1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy = 1)

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
