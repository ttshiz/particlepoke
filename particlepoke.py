import curses
import gameoflife
from curses import wrapper
from curses.textpad import rectangle

def main(stdscr):
    stdscr.clear()
    #stdscr.nodelay(True)
    # make window with boarder for game, window size then coordinates
    #win = curses.newwin(77, 77, 2, 2)
    # boarder of window coordinates then window size
    rectangle(stdscr, 1, 1, 23, 23)
    #loop for game
    for i in range(2, 10):
        v = i-10
        # change to add line of array
        stdscr.addstr(i, 2, '10 divided by {} is {}'.format(v, 10/v))
        #move refresh till after all array added
        stdscr.refresh()
        # check for user input
        try:
            keypress = stdscr.getkey()
        except:
            keypress = None
        # handle input
        #if position poke position elif start/stop do that else if quit quit

wrapper(main)