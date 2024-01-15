import pygame
import random
from game_object import GameObject
import numpy as np
# import os

class Asteroid(GameObject):
    def __init__(self, size):
        """
        size: radius
        """
        pts = []
        num = 8
        for i in range(num):
            r = abs(random.gauss(.8,.1)) # add randomness
            a = 360/num*np.pi/180*i
            p = (r*np.cos(a), r*np.sin(a),)
            pts.append(p)
        pts.append(pts[0])
        self.pts = np.array(pts)

        side = random.randrange(4)
        if side == 0:
            y = 0
            x =random.randrange(600)
            vx = random.uniform(-1.0, 1.0)
            vy = random.uniform(0.1, 1.0)
        elif side == 1:
            x = 600
            y = random.randrange(600)
            vx = random.uniform(-1.0, -0.1)
            vy = random.uniform(-1.0, 1.0)

        elif side == 2:
            x = random.randrange(600)
            y = 600
            vx = random.uniform(-1.0, 1.0)
            vy = random.uniform(-1.0, -0.1)
        else:
            x = 0
            y = random.randrange(600)
            vx = random.uniform(0.1, 1.0)
            vy = random.uniform(-1.0, 1.0)

        super().__init__(size, x, y, vx, vy)

        if size == 30:
            self.points = 20
        elif size == 20:
            self.points = 50
        elif size == 10:
            self.points = 100


    def render(self, surface, rect):
        pts = self.pts*self.size + np.array([self.x, self.y])
        pygame.draw.polygon(surface,"white",pts.tolist(), width=2)
        if self.debug:
            pygame.draw.circle(surface, "red", (self.x, self.y,), self.size, width=2)
