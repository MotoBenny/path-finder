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


def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)  # noqa: F841
    RED = curses.color_pair(2)  # noqa: F841

    for i, row in enumerate(maze):  # gives me index and value
        for j, value in enumerate(row):
            stdscr.addstr()


def main(stdscr):  # standard output screen.
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)

    # stdscr.clear()
    # stdscr.addstr(0, 0, "Hello!", blue_white)  # row, column, message
    # stdscr.refresh()
    # stdscr.getch()  # waits for input before closing the terminal.


wrapper(main)
