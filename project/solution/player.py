import math
import numpy as np
import pygame
from game_object import GameObject
# from bullet import Bullet

class Player(GameObject):
    def __init__(self):
        self.pts = np.array([
            (0,10),
            (10,-10),
            (5,-7.5),
            (-5,-7.5),
            (-10,-10),
            (0,10)
        ])
        super().__init__(20, 300, 300, 0, 0)

        self.rotation_speed = 0
        self.angle = 0
        self.shields = True
        self.score = 0
        # self.auto_fire = False

    def rotate_left(self):
        self.rotation_speed = 5

    def rotate_right(self):
        self.rotation_speed = -5

    def rotate_none(self):
        self.rotation_speed = 0

    def forward(self):
        self.vx -= math.sin(math.radians(self.angle))
        self.vy -= math.cos(math.radians(self.angle))

    def backwards(self):
        self.vx += math.sin(math.radians(self.angle))
        self.vy += math.cos(math.radians(self.angle))

    def update(self, delta_time):
        self.angle = (self.angle + self.rotation_speed) % 360
        super().update(delta_time)

    def render(self, surface, rect):
        a = self.angle * np.pi / 180.0+np.pi
        rot = np.array([[np.cos(a), -np.sin(a)],[np.sin(a),np.cos(a)]])
        pts = self.pts @ rot
        pts += np.array([self.x, self.y])
        pygame.draw.polygon(surface,"yellow",pts.tolist())

        if self.debug:
            pygame.draw.circle(surface, "red", (self.x, self.y,), self.size, width=2)

        if self.shields:
            pygame.draw.circle(surface, "blue", (self.x, self.y,), self.size, width=2)