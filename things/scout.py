import curses
from things.thing import Thing

class Scout(Thing):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.img = "$"

        # >>>
        self.max_health = 6
        self.cur_health = self.max_health
        self.speed = 3
        self.max_actions = 2
        self.cur_actions = self.max_actions

    def draw_info(self, y: int, x: int, scr):
        super().draw_info(y, x, scr)

        scr.addstr(y + 1, x, "HP: ")
        for i in range(self.max_health):
            scr.addstr(y + 1, x + 4 + i, "□")  
        for i in range(self.cur_health):
            scr.addstr(y + 1, x + 4 + i, "■")