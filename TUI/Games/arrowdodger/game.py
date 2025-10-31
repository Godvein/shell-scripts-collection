import curses
from curses import wrapper
from hero import Hero
from arrowspawner import ArrowSpawner
def main(stdscr):
    # remove cursor
    curses.curs_set(0)

    # initialize hero class
    hero = Hero(10, 10)

    # initialize arrowspawner class
    arrowspawner = ArrowSpawner(stdscr, state="right")
    
    # hero color
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    hero_color = curses.color_pair(1)

    # game running
    running = True

    # game over 
    game_over = False

    stdscr.timeout(30) # run loop every 30ms

    # stats screen
    statsscr = curses.newwin(2, 20, 0, 0)

    #health color
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    high_health = curses.color_pair(2)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    half_health = curses.color_pair(3)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    low_health = curses.color_pair(4)

    while running:
        while not game_over:
            key = stdscr.getch()

            game_over = hero.move(key, stdscr) # move hero and check of out of bounds ( returns true if out of screen )
            hero.update()
            arrowspawner.spawn()
            arrowspawner.update(stdscr)
            if arrowspawner.detectcollision(hero):
                hero.health -= 10

            # draw on screen
            stdscr.clear()
            hero.draw(stdscr, hero_color)
            arrowspawner.draw(stdscr)
            stdscr.refresh()

            #stats screen logic
            statsscr.clear()
            statsscr.addstr(0, 0, "Double press q to quit")
            if hero.health > 70:
                statsscr.addstr(1, 0, f"hero health: {hero.health}", high_health)
            elif hero.health > 40:
                statsscr.addstr(1, 0, f"hero health: {hero.health}", half_health)
            else:
                statsscr.addstr(1, 0, f"hero health: {hero.health}", low_health)
            statsscr.refresh()

            #logic to quit game
            if key == ord('q'):
                game_over = True

        
        key = stdscr.getch()
        # game quit logic
        if key == ord('q'):
            running = False

    
if __name__ == "__main__":
    wrapper(main)
