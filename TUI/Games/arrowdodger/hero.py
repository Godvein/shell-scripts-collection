import os

class Hero:

    def __init__(self, x, y):
        #hero stats 
        self.health = 100
        self.velocity = 1

        # 2d vector location
        self.x = x
        self.y = y

        # state for animation
        self.state = "idle"

        #animation frames
        self.frames = self.load_frames()
        self.frame_index = 0
        self.tick = 0

        # collision variable
        self.width = max(len(line) for line in self.frames[0])
        self.height = len(self.frames[0])

    def load_frames(self):
        folder = os.path.join(os.path.dirname(__file__), "sprites/hero") # gives absolute path to idle animation folder
        frames = [] # initialize empty frames array

        # loop the listed and sorted files in animation folder path
        for file in sorted(os.listdir(folder)):

            if self.state == "idle":
                if file.startswith("idle"):
                # open with absolute path to the animatio .txt file as f
                    with open(os.path.join(folder, file)) as f: 
                        frames.append(f.read().splitlines()) # add the txt animation to frames array

            if self.state == "runningleft":
                with open(os.path.join(folder, "running_left.txt")) as f:
                    frames.append(f.read().splitlines())

            if self.state == "runningright":
                with open(os.path.join(folder, "running_right.txt")) as f:
                    frames.append(f.read().splitlines())


        # now frames is 2d array
        return frames 

    def move(self, key, stdscr):
        screen_height, screen_width = stdscr.getmaxyx()
        # move down
        if key == ord('w'):
            self.y = self.y - self.velocity
            if self.y < 1:
                return True
        # move up
        if key == ord('s'):
            self.y = self.y + self.velocity
            if self.y > screen_height-7:
                return True
        # move left
        if key == ord('a'):
            self.x = self.x - self.velocity
            self.set_state("runningleft")
            if self.x < 1:
                return True
        # move right 
        if key == ord('d'):
            self.x = self.x + self.velocity
            self.set_state("runningright")
            if self.x > screen_width-5:
                return True

        return False

    def update(self):

        self.tick += 1
        # increase frame index every 10 times the function is called
        if self.tick % 10 == 0:
            if self.frame_index > len(self.frames)-1:
                self.frame_index = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)

    def set_state(self, new_state):
        # efficient way to set state if new state isnt set
        if self.state != new_state:
            self.state = new_state
            self.frames = self.load_frames()
            self.frame_index = 0
            self.tick = 0

    def draw(self, stdscr, hero_color):
        frame = self.frames[self.frame_index] #get a array from 2d array frames according to index
        for i, line in enumerate(frame): # draw each array of frame y + i
            stdscr.addstr(self.y + i, self.x, line, hero_color)

