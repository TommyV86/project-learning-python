import pygame
import random


pygame.font.init()
screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)
bg_game = pygame.image.load("bg.png")
alien = pygame.image.load("alien.png")
alien = pygame.transform.scale(alien, (105, 105))
alien_x = 130
enemy = pygame.image.load("enemy.png")
enemy = pygame.transform.scale(enemy, (120, 120))
score = 0

def display_score(score):
    font = pygame.font.SysFont("Comic Sans MS", 20)
    score_text = "Score : " + str(score)
    text_img = font.render(score_text, True, (0, 255, 0))
    screen.blit(text_img, [20, 10])


def random_y():
    return -1 * random.randint(100, 1000)


enemy_y = [random_y(), random_y(), random_y()]


def crash(idx):
    global score
    global running
    score -= 100
    enemy_y[idx] = random_y()
    print("crash with alien", idx, score)
    if score == -300:
        print("perdu ..")
        running = False


def update_enemies_pos(idx):
    global score
    global running
    if enemy_y[idx] > 600:
        score += 100
        print(f"t'as gagné {score} points !")
        enemy_y[idx] = random_y()
        if score == 5000:
            running = False
            print("Bien joué !")
    else:
        enemy_y[idx] += 0.9
    

running = True
while running:

    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and alien_x < 260:
        alien_x += 1
    elif keys[pygame.K_LEFT] and alien_x > 0:
        alien_x -= 1

    

    screen.blit(bg_game, [0, 0])
    screen.blit(alien, [alien_x, 500])
    screen.blit(enemy, [30, enemy_y[0]])
    screen.blit(enemy, [130, enemy_y[1]])
    screen.blit(enemy, [240, enemy_y[2]])
    
    update_enemies_pos(0)
    update_enemies_pos(1)
    update_enemies_pos(2)
    
    
    if enemy_y[0] > 500 and alien_x < 70:
        crash(0)
    
    if enemy_y[1] > 500 and alien_x > 80 and alien_x < 200:
        crash(1)
    
    if enemy_y[2] > 500 and alien_x > 220:
        crash(2)


    display_score(score)
    pygame.display.update()

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("game over")