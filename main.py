import curses
from curses import wrapper

def start_screen(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    
    title = "WELCOME TO THE TERMINAL APP"
    subtitle = "Press any key to continue..."
    
    stdscr.attron(curses.color_pair(1))
    stdscr.attron(curses.A_BOLD)
    stdscr.addstr(height//2 - 2, (width - len(title)) // 2, title)
    stdscr.attroff(curses.A_BOLD)
    stdscr.attroff(curses.color_pair(1))
    
    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(height//2, (width - len(subtitle)) // 2, subtitle)
    stdscr.attroff(curses.color_pair(3))
    
    stdscr.refresh()
    stdscr.getkey()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.clear()
    stdscr.addstr("Hello, World!")
    stdscr.refresh()
    stdscr.getkey()
    
wrapper(main)