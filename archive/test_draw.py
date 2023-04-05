import curses

def draw_map(scr, y: int, x: int, clock:bool):
    # actual dimensions:
    # width -- 9
    # height - 7
    #
    # draw dimensions:
    # width -- 7
    # height - 5

    scr.addstr(y + 0, x, "╔═══════╗")
    scr.addstr(y + 1, x, "║███████║") 
    scr.addstr(y + 2, x, "║   █   ║") 
    scr.addstr(y + 3, x, "║ █████ ║")
    scr.addstr(y + 4, x, "║ █   █ ║")
    scr.addstr(y + 5, x, "╚═══════╝")

    # if clock:
    scr.addstr(y + 3, x + 4, "^", curses.color_pair(1))
        # scr.addstr(y + 3, x + 5, "v", curses.color_pair(1))
        # scr.addstr(y + 3, x + 5, "<", curses.color_pair(1))
        # scr.addstr(y + 3, x + 5, ">", curses.color_pair(1))

def draw_viewport(scr, y, x):
    # actual dimensions:
    # width -- 27
    # height - 11
    #
    # draw dimensions:
    # width -- 25
    # height - 10

    scr.addstr(y + 0, x,  "╔═════════════════════════╗")
    scr.addstr(y + 1, x,  "║████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████║") 
    scr.addstr(y + 2, x,  "║█████▓░░░░░░░░░░░░░▓█████║") 
    scr.addstr(y + 3, x,  "║█████▓▓░░░░░░░░░░░▓▓█████║") 
    scr.addstr(y + 4, x,  "║█████▓▓▓         ▓▓▓█████║") 
    scr.addstr(y + 5, x,  "║█████▓▓▓         ▓▓▓█████║") 
    scr.addstr(y + 6, x,  "║█████▓▓░░░░░░░░░░░▓▓█████║") 
    scr.addstr(y + 7, x,  "║█████▓░░░░░░░░░░░░░▓█████║") 
    scr.addstr(y + 8, x,  "║████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████║") 
    scr.addstr(y + 9, x,  "║███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███║")  
    scr.addstr(y + 10, x, "║██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██║")  
    scr.addstr(y + 11, x, "╚═════════════════════════╝")

def draw_controls(scr, y, x):
    scr.addstr(y + 0, x, "╔═══╗ ╔═══╗ ╔═══╗")
    scr.addstr(y + 1, x, "║ ┐ ║ ║ ^ ║ ║ ┌ ║")
    scr.addstr(y + 2, x, "╚[Q]╝ ╚[W]╝ ╚[E]╝")
    scr.addstr(y + 3, x, "╔═══╗ ╔═══╗ ╔═══╗")
    scr.addstr(y + 4, x, "║ < ║ ║ v ║ ║ > ║")
    scr.addstr(y + 5, x, "╚[A]╝ ╚[S]╝ ╚[D]╝")