import pygame
import random

pygame.init()

class Display:
    def __init__(self):
        self.screen_size = [360, 600]
        self.screen = pygame.display.set_mode(self.screen_size)
        self.title = pygame.display.set_caption("Dodge Game")
        self.bg = pygame.image.load("bg.png")

class Alien:
    def __init__(self):
        self.alien_0 = pygame.image.load("alien.png")
        self.alien_0 = pygame.transform.scale(self.alien_0, (105, 105))
        self.alien_x = 130

class Enemy:
    def __init__(self):
        self.enemy_0 = pygame.image.load("enemy.png")
        self.enemy_0 = pygame.transform.scale(self.enemy_0, (120, 120))
        
display = Display()
alien = Alien()
enemy = Enemy()

running = True
while running:

    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and alien.alien_x < 260:
        alien.alien_x += 1
    elif keys[pygame.K_LEFT] and alien.alien_x > 0:
        alien.alien_x -= 1

    display.screen.blit(display.bg, [0, 0])
    display.screen.blit(alien.alien_0, [alien.alien_x, 500])
    display.screen.blit(enemy.enemy_0, [130, 0])

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("game over")
