### This will be a tutorial for a simple jumping program using the pygame libary!

## Step 1: Setup

To start, we will import the pygame library and initialize it. We will also set 3 constants: the width and height of the screen in pixels, and the framerate (number of times the screen updates in one second).
```python
import pygame

pygame.init()

width = 600
height = 400
fps = 30
```
Next we will create a clock and surface. To create a surface we need to input the dimensions we want (as defined earlier). The surface will appear as a window on your computer, and it is how the game is displayed. The clock keeps track of the time and makes sure that the surface updates according to the framerate we set.
```python
clock = pygame.time.Clock()
surface = pygame.display.set_mode((width, height))
```
Finally we will create the game loop, where all of the actual code for the game will run. The game loop will run as long as the variable `running` stays set to true. 
Each time the loop runs, it first checks all of the events. In pygame, events are how the game registers input like key presses, mouse movement, or mouse clicks. In order to check all of the events, we will iterate through a list of them given by `pygame.event.get()`. For now we are just going to check if the "X" button on the window has been pressed. When this happens, pygame will detect an event of the type `pygame.QUIT`. So in the if statement below, when we detect this event, running will be set to false causing the game loop to exit and the window to close.
After checking for events, we update the display to show the next frame that was rendered, and then "tick" the clock to wait until it is time to generate the next frame.
```python
running = true
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = false
		
	pygame.display.update()
	clock.tick(fps)
```
Try running this code now! A black window should pop up that is the size we specified, and if you click the "X", it should close. On Windows, it will look like this:

![step1.png](https://raw.githubusercontent.com/lukvmil/pygame-tutorial/master/images/step1.png)


## Step 2
Now it's time to add the player!