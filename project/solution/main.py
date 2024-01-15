#!/usr/bin/env python3
# http://www.classicgaming.cc
import os
import sys
import pygame
from asteroid import Asteroid
from world import World

class Application:
    """
    This gets inputs from a player and draws the world to the screen
    """
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        pygame.display.set_caption("Asteroids")

        self.screen = pygame.display.set_mode((600, 600))
        self.font = pygame.font.SysFont("Monaco",20)

        self.is_game_over = True

        self.player_keys = [
            pygame.K_LEFT,
            pygame.K_RIGHT,
            pygame.K_UP,
            pygame.K_DOWN,
            pygame.K_SPACE,
            pygame.K_a
        ]

        # TODO: Your program should test that pygame.mixerpygame module
        # for loading and playing sounds is available and intialized before using it.
        # pygame.mixer.music.load(os.path.join("Sounds", "background.ogg"))
        # pygame.mixer.music.set_volume(0.01)
        # pygame.mixer.music.play(-1, 31)

        self.world = World()

    def run(self):
        self.quit = False
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        while(not self.quit):
            self.clock.tick(60)

            for event in pygame.event.get():
                self.handle_event(event)

            self.update(self.clock.get_time())
            self.render()

    def game_setup(self):
        if self.world.is_player_dead == False:
            return
        self.world.append_player()
        self.is_game_over = False

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.USEREVENT:
            self.world.append(Asteroid(30))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.quit = True
            elif event.key in self.player_keys:
                self.world.player_key(event)
            elif event.key == pygame.K_s:
                self.game_setup()
        elif event.type == pygame.KEYUP:
            if event.key in self.player_keys:
                self.world.player_key(event)
            elif event.key == pygame.K_ESCAPE:
                self.quit = True

    def update(self, delta_time):
        screen_rect = self.screen.get_rect()
        self.world.update(delta_time, screen_rect)
        if self.world.is_player_dead:
            self.is_game_over = True

    def render(self):
        surface = self.screen
        rect = self.screen.get_rect()
        surface.fill((0, 0, 0))

        if self.is_game_over:
            self.game_over()
        else:
            score_surface = self.font.render(
                f"Score: {int(self.world.player.score)}",
                True,
                (255, 255, 255)
            )
            score_rect = score_surface.get_rect()
            score_rect.topright = rect.topright
            surface.blit(score_surface, score_rect)

        for go in self.world:
            go.render(surface, rect)

        pygame.display.flip()

    def on_quit(self):
        self.quit = True

    def game_over(self):
        text_surface = self.font.render(
            "[s]TART or [q]UIT",
            True,
            (255, 255, 255)
        )
        text_rect = text_surface.get_rect()
        rect = self.screen.get_rect()
        text_rect.center = rect.center
        self.screen.blit(text_surface, text_rect)


if getattr(sys, 'frozen', False):
    os.chdir(os.path.dirname(sys.executable))

print("Asteroid 1.0")
app = Application()
app.run()
