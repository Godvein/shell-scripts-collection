
class HACollisionDetector:
    def __init__(self, hero, arrow):
        self.hero = hero
        self.arrow = arrow

    def detect(self):
        return (self.hero.x < self.arrow.x + self.arrow.width and 
            self.hero.x + self.hero.width > self.arrow.x and
            self.hero.y < self.arrow.y + self.arrow.height and
            self.hero.y + self.hero.height > self.arrow.y)

    def draw(self, stdscr):
    # Draw hero hitbox
        for i in range(self.hero.height):
            for j in range(self.hero.width):
                stdscr.addstr(self.hero.y + i, self.hero.x + j, "#")


