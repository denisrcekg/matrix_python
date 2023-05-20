import curses
import time
import random

stdscr = curses.initscr()
curses.start_color()  # Добавляем вызов функции start_color()

curses.curs_set(0)
stdscr.nodelay(1)
stdscr.timeout(100)

rows, cols = stdscr.getmaxyx()

# Определение цветовых пар
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

symbols = ['@', '#', '%', '*', '+', '=', '-', '_', ' ', '0', '1', 'Б', 'А', 'Ш', 'Т', 'О', 'В', 'Е', 'Н', 'К', 'О']

while True:
    x = random.randint(0, cols-1)
    y = 0

    while y < rows:
        symbol = random.choice(symbols)
        stdscr.addstr(y, x, symbol, curses.color_pair(1))  # Используем цветовую пару 1
        stdscr.refresh()
        time.sleep(0.1)
        stdscr.addstr(y, x, ' ')  # Стираем символ
        y += 1

curses.endwin()