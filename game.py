import pygame
import random
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
    screen = pygame.display.set_mode((x,y))
    pygame.display.set_caption('Walkerman')
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill("black")

        #pygame.QUIT events means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        enemy_npc = Enemy(5,random_x, random_y, width, height)
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
        
        if keys[pygame.K_RIGHT] and x_coord < x - width:
            x_coord += speed

        if keys[pygame.K_UP] and y_coord > 0:
            y_coord -= speed

        if keys[pygame.K_DOWN] and y_coord < y - height:
            y_coord += speed

        player = walkerman(speed, x_coord, y_coord, width, height)

        playerSquare = walkerman.displaySquare(screen, player.square)

        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] and keys[pygame.K_SPACE]:
            width -= 2
            height -= 2

        elif keys[pygame.K_SPACE]:
            width += 2
            height += 2

        

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()