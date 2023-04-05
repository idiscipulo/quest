import curses

from src.my_random import get_id

class Thing:
    def __init__(self, y: int, x: int, team: str=None):
        self.id = get_id()
        self.team = team
        self.y = y
        self.x = x
        
        self.img = "■"
        self.name = None
        
        self.speed = 0

        self.actions = []
        self.action_blocks = []

        self.max_health = 6
        self.cur_health = self.max_health
        self.speed = 3
        self.max_actions = 2
        self.cur_actions = self.max_actions

        self.actions = ["MOVE"]

    def get_color(self):
        if self.team == "PLAYER":
            return curses.COLOR_CYAN
        elif self.team == "ENEMY":
            return curses.COLOR_YELLOW
        else:
            return curses.COLOR_WHITE

    def move(self):
        self.cur_actions -= 1
    
    def draw_actions(self, y: int, x: int, scr):
        for ind, action in enumerate(self.action_blocks):
            scr.addstr(y + 0, x, "╔══════════════════════════════════╗")
            scr.addstr(y + 1, x, "║                                  ║") 
            scr.addstr(y + 2, x, "╚═══════════[Press < >]════════════╝")

            scr.addstr(y + 1, x + 2, action["desc"])
            scr.addstr(y + 2, x + 20, str(ind + 1))


    def refresh_action_blocks(self):
        self.action_blocks = []

        if "MOVE" in self.actions:
            if self.cur_actions >= 1:
                self.action_blocks.append({
                    "name": "Move"
                    , "desc": f"Move up to {self.speed} tiles."
                    , "func": self.move
                })

    def draw_info(self, y: int, x: int, scr):
        act_color = (curses.COLOR_BLACK * 10) + self.get_color() + 1
        scr.addstr(y, x, self.img, curses.color_pair(act_color))

        name_str = self.__class__.__name__
        if self.name is not None:
            name_str = f"{name_str} | {self.name}"

        scr.addstr(y, x + 2, name_str)

        scr.addstr(y + 1, x, "HP: ")
        for i in range(self.max_health):
            scr.addstr(y + 1, x + 4 + i, "□")  
        for i in range(self.cur_health):
            scr.addstr(y + 1, x + 4 + i, "■")