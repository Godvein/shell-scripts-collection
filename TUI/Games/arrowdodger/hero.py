import curses

class Hero:
    velocity = 1;
    asciisprite = "@@"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, key):
        # move down
        if key == ord('w'):
            self.y = self.y - self.velocity
        # move up
        if key == ord('s'):
            self.y = self.y + self.velocity
        # move left
        if key == ord('a'):
            self.x = self.x - self.velocity
        # move right 
        if key == ord('d'):
            self.x = self.x + self.velocity

    def draw(self, stdscr, hero_color):
        stdscr.addstr(self.y, self.x, self.asciisprite, hero_color)

