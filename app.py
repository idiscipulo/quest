# ■□▬■←→↑↓—|ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-=_+[]\';,./<>?:"{}¤

import curses
import os

from time import sleep, time

from src.game import Game
from src.color_helper import color_code

FPS_RATIO = 1 / 12
WIDTH = 12
HEIGHT = 12

def app(scr):
    # 0:black
    # 1:red
    # 2:green
    # 3:yellow
    # 4:blue
    # 5:magenta
    # 6:cyan
    # 7:white

    for bg in range(7 + 1):
        for fg in range(7 + 1):
            curses.init_pair(color_code(fg, bg), fg, bg)

    curses.curs_set(False)
    scr.nodelay(True)

    clock = True

    game = Game()
    game.test()

    while True:
        clock = not clock

        # get time at loop start
        s_time = time()

        key = scr.getch()
        
        if key == 27: # escape
            break
        else:
            game.update(key)

        curses.flushinp()

        scr.clear()

        game.draw(0, 0, scr)

        scr.refresh()

        dt = time() - s_time
        delay = max(0, FPS_RATIO - dt)
        sleep(delay)

if __name__ == "__main__":
    terminal_size = os.get_terminal_size()
    cols = terminal_size.columns
    lines = terminal_size.lines

    os.system(f"mode con: cols=80 lines=40")

    curses.wrapper(app)

    os.system(f"mode con: cols={cols} lines={lines}")
