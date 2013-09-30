# -*- coding: utf-8 -*-
import curses, time, random
current_time = time.time()
scurrent_time = time.time()

def timerstart():
    stdscr = curses.initscr()
    c = stdscr.getch()
    curses.endwin()
    current_time = time.time()

def timerstop():
    stdscr = curses.initscr()
    c = stdscr.getch()
    curses.endwin()
    scurrent_time = current_time - time.time()

def scramble():
    sc = ''
    r = ['U', 'D', 'L', 'R', 'F', 'B', 'U2', 'D2', 'L2', 'R2', 'F2', 'B2', 'U"', 'D"', 'L"', 'R"', 'F"', 'B"']
    t = range(20)
    i = 0
    for i in t:
		sc = sc + random.choice(r) + ' '
    print sc

scramble()
timerstart()
timerstop()
print scurrent_time
raw_input()
