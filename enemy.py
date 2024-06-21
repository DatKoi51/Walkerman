import pygame

class Enemy:

    def __init__(self, speed, x,y, width, height) -> None:
        self.square = pygame.Rect(x,y,width,height)
        self.speed = speed
        self.x = x
        self.y = y

    def displaySquare(surface, square):
        return pygame.draw.rect(surface, "red", square)

    def attack(square1: pygame.Rect, square2: pygame.Rect):
        return square1.colliderect(square2)