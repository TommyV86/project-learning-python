import pygame
import random

pygame.init()

score = 0
running = True

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

def random_y():
    return -1 * random.randint(100, 1000)

enemy_y = [random_y(), random_y(), random_y()]

def crash(idx):
    global score
    global running
    score -= 500
    enemy_y[idx] = random_y()
    print("crash with alien", idx)
    if score < -1000:
        running = False
        print("Sorry, you lose")

def update_enemies_pos(idx):
    enemy_y[idx] += 0.9
    if enemy_y[0] > 500 and alien.alien_x < 70:
        crash(0)
    if enemy_y[1] > 500 and alien.alien_x > 80 and alien.alien_x < 200:
        crash(1)
    if enemy_y[2] > 500 and alien.alien_x > 220:
        crash(2)

def final_pos(idx):
    global score
    global running
    if enemy_y[idx] > 600:
        score += 250
        enemy_y[idx] = random_y()
        print("good !")
        if score > 3000:
            running = False
            print("Congratulations ! You finished the game !")
        
def display_score(score):
    font = pygame.font.SysFont("Comic Sans MS", 20)
    score_text = "Score : " + str(score)
    text_img = font.render(score_text, True, (0, 255, 0))
    display.screen.blit(text_img, [20, 10])

display = Display()
alien = Alien()
enemy = Enemy()

while running:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and alien.alien_x < 260:
        alien.alien_x += 1
    elif keys[pygame.K_LEFT] and alien.alien_x > 0:
        alien.alien_x -= 1

    display.screen.blit(display.bg, [0, 0])
    display.screen.blit(alien.alien_0, [alien.alien_x, 500])
    display.screen.blit(enemy.enemy_0, [0, enemy_y[0]])
    display.screen.blit(enemy.enemy_0, [130, enemy_y[1]])
    display.screen.blit(enemy.enemy_0, [260, enemy_y[2]])
    display_score(score)
    
    update_enemies_pos(0)
    update_enemies_pos(1)
    update_enemies_pos(2)

    final_pos(0)
    final_pos(1)
    final_pos(2)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("game over")