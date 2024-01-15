import os
import pygame
from bbox import BBox

class GameObject:
    """
    This contains all of the varibles that are common to
    EVERY game object in the asteroids game
    """
    def __init__(self, size, x, y, vx, vy):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.is_dead = False
        self.points = 0

    def events(self, event):
        pass

    def update(self, delta_time):
        self.x += self.vx
        self.y += self.vy