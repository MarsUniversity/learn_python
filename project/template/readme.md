# Project

## 1: PyGame Basics

You are given some code that opens a window and says "Hello", modify the code to do:

- Move the score with the "Hello" string to the top center of the window
- Add the FPS to the "Hello" string
- Add key events for:
    - Pressing the `escape` key or the `q` key will quit the program
    - Pressing the `s` calls the `game_setup()` function
    - Pressing the arrow keys (left, right, up, down) print the key pressed
    - For the up/down arrows, if the key event is `KEY_UP` also have it print `up key_up` or `down key_up`

## 2: Asteroid

Now we are going to start adding game elements, let's start with making an `asteriod`.

- Use the `World` class to add `Asteroids` to the game
- Use the `Asteriod` class template to creat an asteriod in the game
    - Give it a random direction and velocity
    - Set its points based on its size
    - If `GameOject.debug` is `True`, then draw the bounding circle

## Movement in a Game

Here we are going to use a thing called Euler integration to calculate the position
of an object in our game.

```
position_new = position_old + velocity*time_step
```

## 3: Player

- Add a player variable to the `World` class
- Use the `Player` class template to creat a ship in the game
    - Enable arrow keys to move the `Player` class around
    - If `GameOject.debug` is `True`, then draw the bounding circle
- Use the `Bullet` class template to shoot in the game
    - Enable shooting with the space bar

## 4: World Collision

- Create functions to handle collisions between world objects
- Have the `Player` class keep track of its score
- Have sounds play when things blow up, bullets fired, or spaceship moves