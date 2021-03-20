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
        self.rect.center = 100, -20
        self.vel_y = 0

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), self.rect)
    
    def update(self):
        self.vel_y += gravity
        self.rect.y += self.vel_y

        if self.rect.bottom > floor_level:
            self.rect.bottom = floor_level
            self.vel_y = 0
    
    def on_ground(self):
        return self.rect.bottom == floor_level

p = Player()

gravity = 2
floor_level = 350
jump_strength = 30

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if p.on_ground():
                    p.vel_y = -jump_strength
                
    p.update()

    surface.fill((255, 255, 255))

    p.draw(surface)

    pygame.display.update()
    clock.tick(fps)