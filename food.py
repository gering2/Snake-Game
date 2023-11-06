import pygame
from pygame import Vector2
class Food:
    def __init__(self,cellSize,cellWidth) -> None:
        self.x = 1
        self.y = 1
        self.cellSize = cellSize
        self.cellWidth = cellWidth
        self.pos = Vector2(self.x,self.y)

    def drawFood(self):
        pygame.Rect(self.x,self.y,self.cellSize,self.cellWidth)