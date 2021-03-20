## This will be a tutorial for a simple jumping program using the pygame libary in Python.
The first step of making a game is to create a screen to display things on. To start, we will import the pygame library and initialize it. We will also set 3 constants: the width and height of the screen in pixels, and the framerate (number of times the screen updates in one second).
```
import pygame

pygame.init()

width = 600
height = 400
fps = 30
```
Next we will create a clock and surface. To display a screen in pygame, we need to create a surface, and tell it the dimenions we want (as defined earlier). The clock keeps track of the time and makes sure that the 
```
clock = pygame.time.Clock()
surface = pygame.display.set_mode((width, height))
```

```
running = true
while running:
	pygame.display.update()
	clock.tick(fps)
```
