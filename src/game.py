import curses

from src.map import Map
from things import *

class Game:
    def __init__(self, *kwargs):
        self.frame_width = 20
        self.frame_height = 6

        self.cursor_x = 0
        self.cursor_y = 0
        self.cursor_flash = False
        self.cursor_change = False
        
        self.cur_team = "PLAYER"

        self.things = []
        self.cur_thing = None

        self.map = Map(self.frame_width, self.frame_height)

        self.key = ""

    def is_turn_over(self):
        return sum([x.cur_actions for x in self.things if x.team == self.cur_team]) == 0

    def refresh(self):
        for thing in self.things:
            if hasattr(thing, "cur_actions"):
                thing.cur_actions = thing.max_actions

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

        if key == 32: # SPACEBAR
            if self.cur_thing and self.cur_thing.team == self.cur_team:
                self.cur_thing.cur_actions -= 1

        self.cur_thing = self.map[self.cursor_y][self.cursor_x].thing

        if self.is_turn_over():
            if self.cur_team == "PLAYER":
                self.cur_team = "ENEMY"
            elif self.cur_team == "ENEMY":
                self.cur_team = "PLAYER"
            
            self.refresh()

        self.key = key

    def draw(self, y: int, x: int, scr):
        # draw frame
        scr.addstr(y + 0, x, "╔════════════════════╗")
        scr.addstr(y + 1, x, "║                    ║") 
        scr.addstr(y + 2, x, "║                    ║") 
        scr.addstr(y + 3, x, "║                    ║") 
        scr.addstr(y + 4, x, "║                    ║") 
        scr.addstr(y + 5, x, "║                    ║") 
        scr.addstr(y + 6, x, "║                    ║") 
        scr.addstr(y + 7, x, "╚════════════════════╝")

        self.map.draw(y + 1, x + 1, scr)

        # draw current turn
        scr.addstr(y + 8, x + 2, f"<< {self.cur_team} Turn >>")

        # draw info frame
        scr.addstr(y + 0, x + 23, "╔══════════════════════╗")
        scr.addstr(y + 1, x + 23, "║                      ║") 
        scr.addstr(y + 2, x + 23, "║                      ║") 
        scr.addstr(y + 3, x + 23, "╚══════════════════════╝")

        if self.cur_thing is not None:
            self.cur_thing.draw_info(y + 1, x + 25, scr)

        # cursor
        self.cursor_flash = not self.cursor_flash
        if self.cursor_flash:
            scr.addstr(y + 1 + self.cursor_y, x + 1 + self.cursor_x, "■")   

        scr.addstr(9, 0, str(self.key))
        scr.addstr(9, 5, str(sum([x.cur_actions for x in self.things if x.team == self.cur_team])))

    def test(self):
        self.things.append(Thing())
        self.things.append(Thing())
        self.things.append(Scout(team="PLAYER"))
        self.things.append(Scout(team="ENEMY"))

        self.map.add_thing(2, 3, self.things[0])
        self.map.add_thing(2, 4, self.things[1])
        self.map.add_thing(0, 3, self.things[2])
        self.map.add_thing(3, 10, self.things[3])