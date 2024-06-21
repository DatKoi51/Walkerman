import pygame

class walkerman:

    def __init__(self,speed, x, y, width, height) -> None:
        self.square = pygame.Rect(x,y,width,height)
        self.speed = speed
        self.x = x
        self.y = y

    def displaySquare(surface, square):
        return pygame.draw.rect(surface, "white", square)