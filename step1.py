import pygame
import random

pygame.init()

width = 600
height = 400
fps = 30

clock = pygame.time.Clock()
surface = pygame.display.set_mode((width, height))

class Player:
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 60, 60)
        self.vel_y = 0

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), self.rect)

p = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                
    surface.fill((255, 255, 255))
    p.draw(surface)
    pygame.display.update()
    clock.tick(fps)