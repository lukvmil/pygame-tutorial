import pygame
import random

pygame.init()

width = 600
height = 400
fps = 30

clock = pygame.time.Clock()
surface = pygame.display.set_mode((width, height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                
    surface.fill((255, 255, 255))

    pygame.display.update()
    clock.tick(fps)