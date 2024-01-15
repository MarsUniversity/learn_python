

class GameObject:
    """
    This contains the physics of an object in the world
    """
    def __init__(self, size, x, y, vx, vy):
        self.size = size # radius of bounding circle
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.is_dead = False
        self.points = 0 # how many points is this worth?
        self.debug = True

    def update(self, delta_time):
        self.x += self.vx
        self.y += self.vy

