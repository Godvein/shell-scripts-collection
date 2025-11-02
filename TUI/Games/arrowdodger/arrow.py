import os

class Arrow:

    def __init__(self, x, y, state):
        # arrow stats
        self.velocity = 15
        
        # arrow location
        self.x = x
        self.y = y 
        
        # arrow sprite and state
        self.state = state
        self.sprite = self.get_arrow_sprite()
        self.tick = 0

        self.out_of_bounds = False
 
        # default collision variable
        self.width = 6
        self.height = 1

        self.set_collision_box()

    def set_collision_box(self):
       if self.state == "right":
            self.width = 6
            self.height = 1
 
    def get_arrow_sprite(self):
        folder = os.path.join(os.path.dirname(__file__), "sprites/arrows")

        for file in sorted(os.listdir(folder)):

            # sprite for right spawn arrow
            if self.state == "right":
                with open(os.path.join(folder, file)) as f:
                    return f.read().splitlines()
                        

    def update(self, stdscr):  
        max_y, max_x = stdscr.getmaxyx()
        # logic to check arrow in or out of bounds
        if self.y < 0 or self.y > max_y or self.x < 6 or self.x > max_x:
            self.out_of_bounds = True

        # logic to move right spawn arrows if not out of bounds and every 5 function call
        if self.state == "right" and not self.out_of_bounds and self.tick % 5 == 0:
            self.x = self.x - self.velocity
        self.tick += 1

    def draw(self, stdscr):
        for i, line in enumerate(self.sprite):
            # check out of bounds before drawing
            if not self.out_of_bounds:
                stdscr.addstr(self.y + i, self.x, line)
        
