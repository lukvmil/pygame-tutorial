import pygame
import random

pygame.init()

clock = pygame.time.Clock()
fps = 30
screen_width = 600
screen_height = 400
surface = pygame.display.set_mode((screen_width, screen_height))

floor_level = 350
jump_strength = 30
gravity = 2


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
        self.rect = pygame.Rect(screen_width, 300, 50, 50)
        self.vel_x = -10

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def update(self):
        self.rect.x += self.vel_x

        return self.rect.right < 0


p1 = Player()
enemies = []

counter = 0
score = 0
wait_time = 0

pressed = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if p1.on_ground():
                    p1.vel_y = -jump_strength

    if (counter > wait_time):
        counter = 0
        wait_time = random.randint(60, 120)
        enemies.append(Enemy())

    p1.update()

    for enemy in enemies:
        if enemy.update():
            enemies.remove(enemy)
            score += 1
            print(score)
        if p1.rect.colliderect(enemy.rect):
            p1.rect.center = 100, -20
            enemies = []
            score = 0
            print("You died! Restarting...")

    counter += 1

    surface.fill((255, 255, 255))  # white

    pygame.draw.rect(surface, (0, 153, 0), pygame.Rect(
        0, floor_level, screen_width, screen_height-floor_level))

    for enemy in enemies:
        enemy.draw(surface)

    p1.draw(surface)

    pygame.display.update()
    clock.tick(fps)