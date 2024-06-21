import pygame
import random
import math
from walkerman import *
from enemy import *

class game:
    #pygame setup
    pygame.init()
    x = 1280
    y= 720
    x_coord = x/2
    y_coord = y/2
    random_x = random.randrange(1280)
    random_y = random.randrange(720)
    speed = 5
    width = 30
    height = 30
    player_size = 30
    enemy_size = random.randrange(player_size / 2, player_size * 2)
    amplitude = 50
    frequency = 0.1
    screen = pygame.display.set_mode((x,y))
    pygame.display.set_caption('Walkerman')
    clock = pygame.time.Clock()
    running = True
    game_over = False
    score = 0

    def displayScore(surface, score):
        font = pygame.font.Font(None,36)
        score_text = font.render(f"Score: {score}", True, (255,255,255))
        surface.blit(score_text,(10,10))


    while running:
        screen.fill("black")

        displayScore(screen,score)

        #pygame.QUIT events means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        enemy_npc = Enemy(5,random_x, random_y, enemy_size, enemy_size)
        enemySquare = Enemy.displaySquare(screen, enemy_npc.square)

        if(enemy_npc.x < x_coord):
            random_x += 5
        elif(enemy_npc.x > x_coord):
            random_x -= 5
        if(enemy_npc.y < y_coord):
            random_y += 5
        elif(enemy_npc.y > y_coord):
            random_y -= 5

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x_coord > 0:
            x_coord -= speed
        
        if keys[pygame.K_RIGHT] and x_coord < x - player_size:
            x_coord += speed

        if keys[pygame.K_UP] and y_coord > 0:
            y_coord -= speed

        if keys[pygame.K_DOWN] and y_coord < y - player_size:
            y_coord += speed

        player = walkerman(speed, x_coord, y_coord, player_size, player_size)

        playerSquare = walkerman.displaySquare(screen, player.square)

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] and keys[pygame.K_SPACE] and player_size >= 15:
            if player_size < 15:
                player_size = 15
            else:
                player_size -= 2

        elif keys[pygame.K_SPACE] and player_size < enemy_size * 2:
            player_size += 2

        if(Enemy.attack(enemySquare,playerSquare) and enemy_size >= player_size):
            game_over = True
        elif(Enemy.attack(enemySquare,playerSquare) and enemy_size < player_size):
            random_x = random.randrange(x)
            random_y = random.randrange(y)
            enemy_size = random.randrange(player_size * 1 // 4, player_size * 2)
            score += 1

        while game_over:
            # Reset the screen
            screen = pygame.display.set_mode((x, y),0,0,0,1)
            # Initialize game over font
            gover_font = pygame.font.Font(None, 75)
            text = gover_font.render("Game Over", 1, (255, 0, 0))
            screen.blit(text, (x // 2 - text.get_width() // 2, y // 2 - text.get_height() // 2))
            # Initialize score font
            score_font = pygame.font.Font(None,36)
            score_text = score_font.render(f"Score: {score}", True, (255,255,255))
            screen.blit(score_text,(x // 2 - score_text.get_width() // 2, (y * 57 // 100 - score_text.get_height() // 2) ))
            # Run the frames
            pygame.display.flip()
            clock.tick(15)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    running = False

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()