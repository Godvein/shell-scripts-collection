from arrow import Arrow
from collisiondetector import HACollisionDetector
import random

class ArrowSpawner:

    def __init__(self, stdscr, state, difficulty):
        # get screen max x and y
        self.max_y, self.max_x = stdscr.getmaxyx()

        # tick time to spawn
        self.tick = 0

        # arrows array
        self.arrows = []

        #arrow state
        self.state = state

        #initialize collisiondetector
        self.collisiondetector = HACollisionDetector(None, None)
       
        # difficulty settings
        self.difficulty = difficulty

    def detectcollision(self, hero):
        # collision detection check every arrow in arrows
        for arrow in self.arrows:
            self.collisiondetector = HACollisionDetector(hero, arrow)
            if self.collisiondetector.detect():
                return True

        return False
                
    def spawn(self):
        # spawn arrow every 10 ticks fucntion call
        if self.tick % 10 == 0:
            random_y = random.randint(1, self.max_y - 2)
            arrow = Arrow(self.max_x - 7, random_y, self.state)
            # random arrow spawn
            self.arrows.append(arrow)
            if self.difficulty == "hard":
                arrow.velocity = 15
            if self.difficulty == "easy":
                arrow.velocity = 5

        self.tick += 1

    def update(self, stdscr):
        for arrow in list(self.arrows):
            arrow.update(stdscr)
 
    def draw(self, stdscr):
        for arrow in list(self.arrows):
            arrow.draw(stdscr)
        
        # destroy arrow from array if out of bounds
        self.arrows = [a for a in self.arrows if not a.out_of_bounds]

            
           

