import curses

from src.map import Map
from things import *

class Game:
    def __init__(self):
        self.frame_width = 16
        self.frame_height = 5

        self.cursor_x = 0
        self.cursor_y = 0
        self.cursor_flash = False
        self.cursor_change = False

        self.things = []
        self.cur_thing = None

        self.map = Map(self.frame_width, self.frame_height)

        self.key = ""

    def update(self, key):
        self.cursor_change = True

        if key in [258, 456]: # DOWN
            self.cursor_y = min(self.cursor_y + 1, self.frame_height - 1)
        elif key in [259, 450]: # UP
            self.cursor_y = max(self.cursor_y - 1, 0)
        elif key in [260, 452]: # LEFT
            self.cursor_x = max(self.cursor_x - 1, 0)
        elif key in [261, 454]: # RIGHT
            self.cursor_x = min(self.cursor_x + 1, self.frame_width - 1)
        else:
            self.cursor_change = False

        self.cur_thing = self.map[self.cursor_y][self.cursor_x].thing

        self.key = key

    def draw(self, y: int, x: int, scr):
        # draw frame
        scr.addstr(y + 0, x, "╔════════════════╗")
        scr.addstr(y + 1, x, "║                ║") 
        scr.addstr(y + 2, x, "║                ║") 
        scr.addstr(y + 3, x, "║                ║") 
        scr.addstr(y + 4, x, "║                ║") 
        scr.addstr(y + 5, x, "║                ║") 
        scr.addstr(y + 6, x, "╚════════════════╝")

        self.map.draw(y + 1, x + 1, scr)

        # draw info frame
        scr.addstr(y + 0, x + 19, "╔══════════════════════╗")
        scr.addstr(y + 1, x + 19, "║                      ║") 
        scr.addstr(y + 2, x + 19, "║                      ║") 
        scr.addstr(y + 3, x + 19, "╚══════════════════════╝")

        if self.cur_thing is not None:
            self.cur_thing.draw_info(y + 1, x + 21, scr)


        # cursor
        self.cursor_flash = not self.cursor_flash
        if self.cursor_flash:
            scr.addstr(y + 1 + self.cursor_y, x + 1 + self.cursor_x, "■")   

        scr.addstr(8, 0, str(self.key))

    ##########

    def test(self):
        self.map.add_thing(2, 3, Thing())
        self.map.add_thing(2, 4, Thing())
        self.map.add_thing(0, 3, Scout(team="PLAYER"))
        self.map.add_thing(3, 10, Scout(team="ENEMY"))