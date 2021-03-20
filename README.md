## This will be a tutorial for a simple jumping program using the pygame libary in Python.
First we are going to set up the display to render the game on.
```
import pygame

width = 600
height = 400
fps = 30

pygame.init()

surface = pygame.display.set_mode((width, height))

running = true
while running:
	pygame.display.update()
	clock.tick(fps)
```
