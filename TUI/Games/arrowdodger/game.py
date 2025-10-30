import curses
from curses import wrapper
from hero import Hero

def main(stdscr):
    # remove cursor
    curses.curs_set(0)

    # initialize hero class
    hero = Hero(10, 10)

    # hero color
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    hero_color = curses.color_pair(1)

    # game running
    running = True

    # game over 
    game_over = False

    stdscr.timeout(30) # run loop every 30ms
   
    while running:
        while not game_over:
            key = stdscr.getch()

            game_over = hero.move(key, stdscr) # move hero and check of out of bounds ( returns true if out of screen )
            hero.update()

            # draw on screen
            stdscr.clear()
            hero.draw(stdscr, hero_color)
            stdscr.refresh()

            #logic to quit game
            if key == ord('q'):
                game_over = True


        key = stdscr.getch()
        # game quit logic
        if key == ord('q'):
            running = False

    
if __name__ == "__main__":
    wrapper(main)
