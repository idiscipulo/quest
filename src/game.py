import curses

from src.color_helper import color_code
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
        self.team_things = {
            "PLAYER": []
            , "ENEMY": []
        }
        self.cur_thing_ind = 0
        self.cur_thing = None

        self.map = Map(self.frame_width, self.frame_height)

        self.key = ""

    def is_turn_over(self):
        return sum([x.cur_actions for x in self.things if x.team == self.cur_team]) == 0

    def refresh_actions(self):
        for thing in self.things:
            if hasattr(thing, "cur_actions"):
                thing.cur_actions = thing.max_actions
                thing.refresh_action_blocks()

    def add_thing(self, thing: Thing):
        self.things.append(thing)

        if thing.team:
            self.team_things[thing.team].append(thing)

    def update(self, key):
        if self.cur_team == "PLAYER":
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

            if key == 9: # TAB
                self.cur_thing_ind += 1
                self.cur_thing_ind = self.cur_thing_ind % len(self.team_things[self.cur_team])
                
                self.cur_thing = self.team_things[self.cur_team][self.cur_thing_ind] # have to do this early to get y,x
                self.cur_thing.refresh_action_blocks()
                self.cursor_y = self.cur_thing.y
                self.cursor_x = self.cur_thing.x

        
            self.cur_thing = self.team_things[self.cur_team][self.cur_thing_ind]
            
            if key in range(49, 58): # 1, 2, 3, 4, 5, 6, 7, 8, 9
                num_key = key - 48
        
                if self.cur_thing and self.cur_thing.team == "PLAYER" and len(self.cur_thing.action_blocks) >= num_key:
                    self.cur_thing.action_blocks[num_key - 1]["func"]()

            if self.is_turn_over():
                self.cur_team = "ENEMY"
                self.refresh_actions()

            self.key = key
        elif self.cur_team == "ENEMY":
            # >>>
            thing_options = [x for x in self.things if x.team == "ENEMY" and x.cur_actions > 0]
            thing_options[0].cur_actions -= 1

            if self.is_turn_over():
                self.cur_team = "PLAYER"
                self.refresh_actions()

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

        for thing in self.things:
            this_bg = self.map[thing.y][thing.x].bg
            scr.addstr(y + thing.y + 1, x + thing.x + 1, thing.img, curses.color_pair(color_code(thing.get_color(), this_bg)))

        # draw current turn
        scr.addstr(y + 8, x + 2, f"<< {self.cur_team} Turn >>")

        # draw info frame
        scr.addstr(y + 0, x + 23, "╔══════════════════════╗")
        scr.addstr(y + 1, x + 23, "║                      ║") 
        scr.addstr(y + 2, x + 23, "║                      ║") 
        scr.addstr(y + 3, x + 23, "╚══════════════════════╝")

        if self.cur_thing is not None:
            self.cur_thing.draw_info(y + 1, x + 25, scr)
            self.cur_thing.draw_actions(y + 4, x + 23, scr)

        if self.cur_team == "PLAYER":
            # cursor
            self.cursor_flash = not self.cursor_flash
            if self.cursor_flash:
                scr.addstr(y + 1 + self.cursor_y, x + 1 + self.cursor_x, "■")   

        scr.addstr(9, 0, str(self.key))
        scr.addstr(9, 5, str(sum([x.cur_actions for x in self.things if x.team == self.cur_team])))

    def test(self):
        self.add_thing(Thing(0, 3, team="PLAYER"))
        self.add_thing(Thing(3, 10, team="PLAYER"))

        self.refresh_actions()