import pygame

class Enemy:

    def __init__(self, speed, x,y, width, height) -> None:
        self.square = pygame.Rect(x,y,width,height)
        self.speed = speed
        self.x = x
        self.y = y

    def displaySquare(surface, square):
        pygame.draw.rect(surface, "red", square)