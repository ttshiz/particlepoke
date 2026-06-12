import curses
import gameoflife
import numpy as np
from curses import wrapper
from curses.textpad import rectangle

def main(stdscr):
    stdscr.clear()
    stdscr.nodelay(True)
    game = gameoflife.GameOfLife()
    game.randomize()
    #initialize display
    for j in range(game.bsize):
        stdscr.addstr(j, 2, np.array_str(game.board[j])[1:-1])
    stdscr.refresh()
    #loop for game
    for i in range(0, 1000):
        game.life_step()
        for j in range(game.bsize):
            stdscr.addstr(j, 2, np.array_str(game.board[j])[1:-1])
        stdscr.refresh()
        
        # TODO: check for user input
        try:
            keypress = stdscr.getkey()
        except:
            keypress = None
        # handle input
        #if position poke position elif start/stop do that else if quit quit

wrapper(main)