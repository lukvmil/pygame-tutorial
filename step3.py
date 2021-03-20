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

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(width, floor_level - 50, 50, 50)
        self.vel_x = -10

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
    
    def update(self):
        self.rect.x += self.vel_x

        return self.rect.right < 0

p = Player()

gravity = 2
floor_level = 350
jump_strength = 30

enemies = []
counter = 0
wait_time = 0
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if p.on_ground():
                    p.vel_y = -jump_strength
    
    if (counter > wait_time):
        counter = 0
        wait_time = random.randint(60, 120)
        enemies.append(Enemy())
    
    counter += 1

    p.update()

    for enemy in enemies:
        if enemy.update() == True:
            enemies.remove(enemy)
            score += 1
            print(score)
        
        if p.rect.colliderect(enemy.rect):
            p.rect.center = 100, -20
            enemies = []
            score = 0
            print("You died! Restarting...")

    surface.fill((255, 255, 255))
    pygame.draw.rect(surface, (0, 153, 0), pygame.Rect(0, floor_level, width, height - floor_level))
    
    p.draw(surface)
    for enemy in enemies:
        enemy.draw(surface)

    pygame.display.update()
    clock.tick(fps)