#!/usr/bin/env python3

import os
import sys
import pygame
import random


class Game:

    def __init__(self):
        # sets up sounds
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        # title bar says name of game
        pygame.display.set_caption("Asteroids")
        # window is 600x600 pixels in size
        self.screen = pygame.display.set_mode((600, 600))
        # save screen size
        self.rect = self.screen.get_rect()
        # select a font for writing messages to screen
        self.font = pygame.font.SysFont("Monaco",20)
        self.state = START_SCREEN

    def run(self):
        """
        This is the main loop
        """
        self.quit = False
        self.clock = pygame.time.Clock()

        # this is the main loop and will never exit until the player is
        # done with the game
        while(not self.quit):
            self.clock.tick(60) # limit to 60 fps

            # this will loop through all events that occurred since last
            # update
            for event in pygame.event.get():
                self.handle_event(event)

            self.update(self.clock.get_time())

            self.render()

    def game_setup(self):
        pass

    def handle_event(self, event):
        """ This is where you put all of the events like key presses """
        if event.type == pygame.QUIT:
            self.quit = True

    def update(self, delta_time):
        """ Update dynamics ... don't have them yet. """
        pass

    def render(self):
        """ Draw game objects to the screen """
        self.screen.fill("black")

        fps = self.clock.get_fps()
        score_surface = self.font.render(f"Hello {fps:.1f}", True, "white")

        w,h = score_surface.get_size()
        win_w, win_h = self.screen.get_size()

        # message, antialias, color
        self.screen.blit(
            score_surface,
            (win_w//2-w//2,win_h//2-h//2)
        )

        pygame.display.flip()

app = Game()
app.run()
