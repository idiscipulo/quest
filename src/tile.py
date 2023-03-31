import curses

class Tile:
    def __init__(self):
        self.thing = None
        self.img = " "
        self.fg = 0
        self.bg = 0

    def get_color(self):
        return (self.bg * 10) + self.fg + 1