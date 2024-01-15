from game_object import GameObject
import math
import pygame

class Bullet(GameObject):
    def __init__(self, player):
        self.size = 3
        x = player.x + math.sin(math.radians(player.angle+180)) * 10
        y = player.y + math.cos(math.radians(player.angle+180)) * 10
        vx = math.sin(math.radians(player.angle+180)) * 5
        vy = math.cos(math.radians(player.angle+180)) * 5
        super().__init__(self.size, x, y, vx, vy)

    def render(self, surface, rect):
        pygame.draw.circle(surface, "orange", (self.x, self.y,), self.size)