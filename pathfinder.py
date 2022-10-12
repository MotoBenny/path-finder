from curses import wrapper
import curses
import queue

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
            stdscr.addstr(i, j * 2, value, BLUE)


def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None


def find_path(maze, stdscr):
    start = "O"  # noqa: F841
    end = "X"  # noqa: F841
    start_pos = find_start(maze, start)  # noqa: F841

    q = queue.Queue  # noqa: F841


def main(stdscr):  # standard output screen.
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.clear()
    print_maze(maze, stdscr)
    stdscr.refresh()
    stdscr.getch()  # waits for input before closing the terminal.


wrapper(main)
