import curses
import time
#import keyboard

#keyboard.wait('q') 
def main(stdscr):
    key = ""
    while True:
        current_key = key
        key = stdscr.getkey()
        if key != current_key:
            print(key)
            time.sleep(1)
        stdscr.clear()
        
curses.wrapper(main)
getch()
print("This is a pretty cool test right")