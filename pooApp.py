import pygame
import random

pygame.init()


class Game:
    def __init__(self):
        self.setup_display()
        self.alien()
        self.enemy()

    def setup_display(self):
        self.screen_size = [360, 600]
        self.screen = pygame.display.set_mode(self.screen_size)
        self.title = pygame.display.set_caption("Dodge Game")
        self.bg = pygame.image.load("bg.png")

    def alien(self):
        self.alien_1 = pygame.image.load("alien.png")
        self.alien_1 = pygame.transform.scale(self.alien_1, (105, 105))
    
    def enemy(self):
        self.enemy_1 = pygame.image.load("enemy.png")
        self.enemy_1 = pygame.transform.scale(self.enemy_1, (120, 120))


game = Game()


running = True
while running:  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("game over")
            
