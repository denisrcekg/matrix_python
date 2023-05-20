import curses
import random
import time

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    rows, cols = stdscr.getmaxyx()
    pad = curses.newpad(rows * 3, cols * 3)  # Создание newpad с увеличенными размерами

    def generate_symbol():
        return chr(random.randint(33, 126))

    def update_matrix():
        for i in range(cols):
            for j in range(rows):
                if random.random() < 0.1:
                    symbol = generate_symbol()
                    pad.addch(j * 3, i * 3, symbol)  # Установка символа в newpad с учетом увеличенных размеров
                else:
                    pad.addch(j * 3, i * 3, ' ')

    while True:
        update_matrix()

        pad.refresh(0, 0, 0, 0, rows - 1, cols - 1)  # Обновление видимой области на экране

        time.sleep(0.1)

if __name__ == '__main__':
    curses.wrapper(main)
