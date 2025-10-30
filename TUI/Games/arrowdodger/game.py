import curses
from curses import wrapper
from hero import Hero

def main(stdscr):
    # initialize hero class
    hero = Hero(10, 10)

    # hero color
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN)
    hero_color = curses.color_pair(1)

    # game running
    running = True

    stdscr.timeout(30) # run loop every 30ms
   
    while running:

        key = stdscr.getch()
        hero.move(key)

        stdscr.clear()
        hero.draw(stdscr, hero_color)
        stdscr.refresh()

        #logic to quit game
        if key == ord('q'):
            running = False
    
if __name__ == "__main__":
    wrapper(main)
