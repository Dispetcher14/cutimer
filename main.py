# -*- coding: utf-8 -*-
import curses, time, random
current_time = time.time()
scurrent_time = time.time()

def timerstart():
    c = stdscr.getch()
    current_time = time.time()
def clrscr():
	stdscr.clear()
	xi = 1
	yi = 1
def timerstop():
    c = stdscr.getch()
    scurrent_time = current_time - time.time()

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
clrscr()
timerstart()
timerstop()
curses.endwin()

