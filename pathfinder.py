# import curses
from curses import wrapper
import curses

# import queue
# import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"],
]


def main(stdscr):  # standard output screen.
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    blue_white = curses.color_pair(1)

    stdscr.clear()
    stdscr.addstr(0, 0, "Hello!", blue_white)  # row, column, message
    stdscr.refresh()
    stdscr.getch()  # waits for input before closing the terminal.


wrapper(main)
