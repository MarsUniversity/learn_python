import pygame

class Asteroid(GameObject):
    def __init__(self, size):
        """
        Create a random asteriod at some position and velocity
        """
        # create random x,y,vx,vy
        # set points based on size
        super().__init__(size, x, y, vx, vy)

    def render(self, suface):
        pass

