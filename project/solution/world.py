
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
        if self.player is None:
            return

        # if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or self.player.auto_fire:
        #     bullet = Bullet(self.player)
        #     self.game_objects.append(bullet)
        #     self.fire_sound.play()
        # else:
        #     print("auto off")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player.rotate_left()
            elif event.key == pygame.K_RIGHT:
                self.player.rotate_right()
            elif event.key == pygame.K_UP:
                self.player.forward()
                self.thrust_sound.play()
            elif event.key == pygame.K_DOWN:
                self.player.backwards()
                self.thrust_sound.play()
            elif event.key == pygame.K_SPACE or event.key:
                bullet = Bullet(self.player)
                self.game_objects.append(bullet)
                self.fire_sound.play()
            elif event.key == pygame.K_a:
                self.player.auto_fire = not self.player.auto_fire
                print(f"Auto: {self.player.auto_fire}")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.player.rotate_none()
            elif event.key == pygame.K_RIGHT:
                self.player.rotate_none()

    def update(self, delta_time, rect):
        for go in self.game_objects:
            go.update(delta_time)
            self.remove_if_out_of_frame(go, rect)

        for go in self.game_objects:
            for ogo in self.game_objects:
                if ogo == go: continue
                distance = (ogo.x - go.x) ** 2 + (ogo.y - go.y) ** 2
                if distance <= (go.size + ogo.size) ** 2:
                    self.collision(go, ogo)

        self.game_objects = [go for go in self.game_objects if not go.is_dead]

        if self.player and self.player.is_dead == True:
            self.is_player_dead = True
            self.player = None

    def remove_if_out_of_frame(self, gobj, rect):
        minx = 0 - gobj.size
        maxx = rect.width + gobj.size
        miny = 0 - gobj.size
        maxy = rect.height + gobj.size

        if gobj.x < minx or gobj.x > maxx or gobj.y < miny or gobj.y > maxy:
            # wrap the player to the other side of the screen
            if isinstance(gobj, Player):
                self.wrap(gobj, rect)
                return
            gobj.is_dead = True

    def wrap(self, obj, rect):
        if obj.y < 0: obj.y = rect.height
        elif obj.y > rect.height: obj.y = 0
        if obj.x < 0: obj.x = rect.width
        elif obj.x > rect.height: obj.x = 0
        return obj

    def collision(self, go, ogo):
        """
        go (game obj): asteroid only
        ogo (other game obj): either player or bullet
        """
        if self.player is None:
            return

        if not isinstance(go, Asteroid):
            return

        if isinstance(ogo, Asteroid):
            return

        if isinstance(ogo, Player):
            if ogo.shields is True:
                ogo.shields = False
                go.is_dead = True
            else:
                ogo.is_dead = True
                self.is_player_dead = True
                self.death_sounds[0].play()
            return

        go.is_dead = True
        ogo.is_dead = True
        self.player.score += go.points

        sound_index = go.size // 10 - 1
        self.death_sounds[sound_index].play()

        if go.size > 10:
            a = Asteroid(go.size - 10)
            a.x = go.x
            a.y = go.y
            self.game_objects.append(a)

            a = Asteroid(go.size - 10)
            a.x = go.x
            a.y = go.y
            self.game_objects.append(a)

        return