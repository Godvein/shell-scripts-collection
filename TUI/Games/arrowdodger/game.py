import curses, time
from curses import wrapper
from hero import Hero
from arrowspawner import ArrowSpawner

def main(stdscr, difficulty):
    # remove cursor
    curses.curs_set(0)

    # initialize hero class
    hero = Hero(10, 10)

    # initialize arrowspawner class
    arrowspawner = ArrowSpawner(stdscr, state="right", difficulty=difficulty)
    
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
    statsscr = curses.newwin(2, 80, 0, 0)

    #health color
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    high_health = curses.color_pair(2)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    half_health = curses.color_pair(3)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    low_health = curses.color_pair(4)

    # start time to get time survived
    start_time = time.time()
    time_survived = 0
    
    current_key = None
    while running:
        while not game_over:

            key = stdscr.getch()

            if key == -1:
                key = current_key
            else:
                current_key = key

            if key not in [ord('w'), ord('a'), ord('s'), ord('d')]:
                current_key = None            

            # if key not pressed set hero state to idle
            if key == -1:
                hero.set_state("idle")

            game_over = hero.move(key, stdscr) # move hero and check of out of bounds ( returns true if out of screen )
            hero.update()

            arrowspawner.spawn()
            arrowspawner.update(stdscr)

            # change hero color if collision with arrow
            if arrowspawner.detectcollision(hero):
                hero.health -= 1
                hero_color = curses.color_pair(4)
            else:
                hero_color = curses.color_pair(1)

            # draw on screen
            stdscr.clear()
            hero.draw(stdscr, hero_color)
            arrowspawner.draw(stdscr)
            stdscr.refresh()

            #stats screen logic
            statsscr.clear()
            statsscr.addstr(0, 0, "Double press q to quit")
            stdscr.addstr(0, 55, "W A S D to sprint, Press any key to stop")
            stdscr.addstr(0, 30, "current difficulty:")
            stdscr.addstr(1, 30, difficulty)
            if hero.health > 70:
                statsscr.addstr(1, 0, f"hero health: {hero.health}", high_health)
            elif hero.health > 40:
                statsscr.addstr(1, 0, f"hero health: {hero.health}", half_health)
            else:
                statsscr.addstr(1, 0, f"hero health: {hero.health}", low_health)

            # calculate survival time
            time_survived = int(time.time() - start_time)
            statsscr.addstr(1, 55, f"time survived: {time_survived} s")

            statsscr.refresh()
            
            #logic to quit game and game over
            if key == ord('q') or hero.health <= 0:
                game_over = True

        # game over screen
        if game_over == True:
            running = gameOver(stdscr, time_survived, difficulty)

        


def gameOver(stdscr, time_survived, difficulty):
    # game over color  
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    game_over_screen = True 
    while game_over_screen:
        stdscr.clear()
        stdscr.addstr(20, 20, "GAME OVER", curses.color_pair(1)) 
        stdscr.addstr(22, 20, f"you survived {time_survived} seconds", curses.color_pair(1))
        stdscr.addstr(24, 20, "press r to retry and q to quit")
        stdscr.addstr(26, 20, f"Current difficulty: {difficulty}")
        stdscr.addstr(28, 20, f"use up and down arrow keys to adjust difficulty")
        stdscr.refresh()
        key = stdscr.getch()

        # adjust difficulty
        if key == curses.KEY_UP and difficulty == "easy":
            difficulty = "normal"
        elif key == curses.KEY_UP and difficulty == "normal":
            difficulty = "hard"
        elif key == curses.KEY_DOWN and difficulty == "normal":
            difficulty = "easy"
        elif key == curses.KEY_DOWN and difficulty == "hard":
            difficulty = "normal"
        
        # restart game 
        if key == ord('r'):    
            main(stdscr, difficulty)
            return True

        # quit game
        if key == ord('q'):
            game_over_screen = False
            return False

    
if __name__ == "__main__":
    wrapper(main, "easy")
