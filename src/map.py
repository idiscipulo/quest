import curses

from src.tile import Tile
from things.thing import Thing

class Map(list):
    def __init__(self, width:int, height:int):
        for y in range(height):
            self.append([])
            for x in range(width):
                self[y].append(Tile())

    def add_thing(self, y:int, x:int, thing:Thing):
        thing.y = y
        thing.x = x

        self[y][x].thing = thing
        self[y][x].img = thing.img
        self[y][x].fg = thing.get_color()

    def draw(self, y:int, x:int, scr):
        for yy, row in enumerate(self):
            for xx, tile in enumerate(row):
                scr.addstr(yy + y, xx + x, tile.img, curses.color_pair(tile.get_color()))