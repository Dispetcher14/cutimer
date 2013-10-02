# -*- coding: utf-8 -*-
import curses, datetime, random

def timerstart():
    return datetime.datetime.now()

def clrscr():
	stdscr.clear()
	xi = 1
	yi = 1
	
def timerstop(d):
    return datetime.datetime.now() - d

def scramble():
    sc = ''
    r = ['U', 'D', 'L', 'R', 'F', 'B', 'U2', 'D2', 'L2', 'R2', 'F2', 'B2', 'U"', 'D"', 'L"', 'R"', 'F"', 'B"']
    t = range(20)
    i = 0
    for i in t:
        sc = sc + random.choice(r) + ' '
    stdscr.addstr(11, 15, 'Your scrumble')
    stdscr.addstr(12, 12, sc)

stdscr = curses.initscr()
stdscr.border(0)
scramble()
stdscr.addstr(13, 15, 'Press any key for start and then - for stop')
stdscr.getch()
w = timerstart()
stdscr.getch()
stdscr.addstr(14, 15, str(timerstop(w)))
stdscr.getch()
curses.endwin()
