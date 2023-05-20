import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    stdscr.keypad(1)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    rows, cols = stdscr.getmaxyx()
    matrix = [''] * cols
    positions = [0] * cols

    def generate_symbol():
        return chr(random.randint(33, 126))

    def update_matrix():
        for i in range(cols):
            if matrix[i] == '' or positions[i] >= rows - 1 or random.random() < 0.1:
                matrix[i] = generate_symbol()
                positions[i] = 0

            if positions[i] > 0:
                stdscr.addstr(positions[i] - 1, i, ' ')

            stdscr.addstr(positions[i], i, matrix[i], curses.color_pair(1))
            positions[i] += 1

            if positions[i] >= rows - 1:
                matrix[i] = ''

    while True:
        update_matrix()
        stdscr.refresh()
        time.sleep(0.1)
        stdscr.erase()

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
