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
After checking for events, we will fill the surface with the color white. The `surface.fill()` function takes a list of 3 numbers ranging from 0 to 255, corresponding to the red, green, and blue components of the color. For white it will be `(255, 255, 255)`. (Try changing the color too!) Then we update the display to show the next frame that was rendered, and "tick" the clock to wait until it is time to generate the next frame.
```python
running = true
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = false
	
	surface.fill(())
	
	pygame.display.update()
	clock.tick(fps)
```
Try running this code now! A black window should pop up that is the size we specified, and if you click the "X", it should close. On Windows, it will look like this:

![step1.png](https://raw.githubusercontent.com/lukvmil/pygame-tutorial/master/images/step1.png)


## Step 2
Now it's time to add the player! We're going to make a simple player class that has functions to render (display) it to the surface, update it's position, and check its state. But before we get into that let's quickly talk about rendering graphics. Unlike the convention you might learn in math class, the origin `(0, 0)` is in the _top_ left corner. Keep this in mind as we continue because the y axis will the reverse of what you are used to. Moving down the screen _increases_ the y coordinate.