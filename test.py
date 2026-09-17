import curses
import textwrap
import keyboard
"""
def main(stdscr):
    stdscr.keypad(True)
    while True:
        print(stdscr.getkey())
    stdscr.clear()
curses.wrapper(main)
"""

from terminedia import getch
import time

getch()
valid = False
while valid is False:
    if keyboard.is_pressed('q'):
        valid = True
