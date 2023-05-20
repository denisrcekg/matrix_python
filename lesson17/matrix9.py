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
    symbols = []
    user_input = ''

    stdscr.addstr(0, 0, "Enter the symbols to display in the matrix (without spaces): ")
    stdscr.refresh()

    while True:
        try:
            key = stdscr.getkey()
            if key == '\n':
                break
            user_input += key
            stdscr.addstr(0, len("Enter the symbols to display in the matrix (without spaces): "), key)
            stdscr.refresh()
        except curses.error:
            pass

    symbols = list(user_input)
    matrix = [[' '] * cols for _ in range(rows)]
    positions = [0] * cols
    velocities = [random.randint(1, 3) for _ in range(cols)]

    def update_matrix():
        for i in range(cols):
            if positions[i] < rows - 1:
                stdscr.addstr(positions[i], i, ' ')
                matrix[positions[i]][i] = ' '

            if random.random() < 0.1 or positions[i] == 0:
                matrix[positions[i]][i] = random.choice(symbols)
                stdscr.addstr(positions[i], i, matrix[positions[i]][i], curses.color_pair(1))

            positions[i] += velocities[i]

            if positions[i] >= rows - 1:
                positions[i] = 0
                velocities[i] = random.randint(1, 3)

    stdscr.erase()
    stdscr.refresh()
    time.sleep(2)

    while True:
        update_matrix()
        stdscr.refresh()
        time.sleep(0.1)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
