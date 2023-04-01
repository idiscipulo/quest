import curses
from src.my_random import get_id

class Thing:
    def __init__(self, team: str=None):
        self.id = get_id()
        self.team = team
        self.img = "■"
        self.name = None

    def get_color(self):
        if self.team == "PLAYER":
            return curses.COLOR_CYAN
        elif self.team == "ENEMY":
            return curses.COLOR_YELLOW
        else:
            return curses.COLOR_WHITE

    def draw_info(self, y: int, x: int, scr):
        act_color = (curses.COLOR_BLACK * 10) + self.get_color() + 1
        scr.addstr(y, x, self.img, curses.color_pair(act_color))

        name_str = self.__class__.__name__
        if self.name is not None:
            name_str = f"{name_str} | {self.name}"

        scr.addstr(y, x + 2, name_str)