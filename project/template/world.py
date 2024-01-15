import os
import pygame
from player import Player
from bullet import Bullet
from asteroid import Asteroid

class World:
    """
    This holds all of the game objects (player, bullets, asteroids, sounds).
    This class does not draw anything to the screen.
    """
    def __init__(self):
        self.player = None
        self.is_player_dead = True
        self.game_objects = []

        self.death_sounds = [
            pygame.mixer.Sound(os.path.join("Sounds", "bangLarge.wav")),
            pygame.mixer.Sound(os.path.join("Sounds", "bangMedium.wav")),
            pygame.mixer.Sound(os.path.join("Sounds", "bangSmall.wav"))
        ]
        self.fire_sound = pygame.mixer.Sound(os.path.join("Sounds", "fire.wav"))
        self.thrust_sound = pygame.mixer.Sound(os.path.join("Sounds", "thrust.wav"))

    def __iter__(self):
        return iter(self.game_objects)

    def append(self, obj):
        self.game_objects.append(obj)

    def append_player(self):
        # already have a player, so return
        if self.player:
            return

        self.player = Player()
        self.game_objects.append(self.player)
        self.is_player_dead = False

    def player_key(self, event):
        pass

    def update(self, delta_time, rect):
        pass

    def remove_if_out_of_frame(self, gobj, rect):
        pass

    def wrap(self, obj, rect):
        pass

    def collision(self, go, ogo):
        pass