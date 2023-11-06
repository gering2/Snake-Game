import pygame
import pygame.freetype
import snake
import random
import sys
from pygame import Vector2
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Snake')

#import pygame
#from pygame import Vector2
class Main:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = Score()
    def update(self):
        self.snake.updateSnake()
        self.checkCollision()
        self.checkFail()
    def drawElements(self):
        self.food.drawFood()
        self.snake.drawSnake()
        self.score.drawScore()
    def checkCollision(self):
        #head of snake colliding with fruit
        if self.food.pos == self.snake.body[0]:
            #remove fruit and place a new fruit
            self.food.randomize()
            self.score.incrementScore()
            self.snake.addSegment()
            #add tail to snake
    def checkFail(self):
        #check if snake is outside screen (outside number of cells)
        if self.snake.body[0].x > CELL_NUMBER-1 or self.snake.body[0].x < 0 or self.snake.body[0].y < 0 or self.snake.body[0].y>CELL_NUMBER-1:
            self.gameOver()
        #check if snake hits itself (if head touches any part of the body)
        if self.snake.body[0] in self.snake.body[1:]:
            self.gameOver()
    def gameOver(self):
        pygame.quit()
        sys.exit()

class Food:
    def __init__(self) -> None:
        self.randomize()

    def drawFood(self):
        
        food = pygame.Rect(self.x*CELL_SIZE,self.y*CELL_SIZE,CELL_SIZE,CELL_SIZE)
        pygame.draw.rect(screen,(255,255,255),food)

    def randomize(self):
        self.x = random.randint(0,CELL_NUMBER-1)
        self.y = random.randint(0,CELL_NUMBER-1)
        self.pos = Vector2(self.x,self.y)
class Snake:
    def __init__(self):
        self.body = [Vector2(1,1),Vector2(1,2)]
        self.direction = Vector2(1,0)
        self.ateFood = False
    def drawSnake(self):
        #create a segment (rect) for each piece of the snake
        for segment in self.body:
            segmentRect = pygame.Rect(segment.x*CELL_SIZE,segment.y*CELL_SIZE,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen,(255,0,0),segmentRect)

    def updateSnake(self):
        #make a copy of the snake, removing the end and placing the new head according to user movement
        if not self.ateFood:
            snakeCutCopy =  self.body[:-1]
            newSnake = [self.body[0]+self.direction] + snakeCutCopy
            self.body = newSnake[:]
        else:
            self.body = [self.body[0]+self.direction] + self.body
            self.ateFood = False

    def addSegment(self):
        #keep the tail of the snake instead of removing it (when colliding with food)
        self.ateFood = True
class Score:
    def __init__(self):
            self.score = 0
            self.color = (250,250, 250)
            self.font =  pygame.freetype.Font('Roboto-Regular.ttf',24)
    def drawScore(self):
        scoreSurface,rect = gameFont.render(f"score:{self.score}",self.color)
        screen.blit(scoreSurface,(680,30))
    def incrementScore(self):
        self.score +=1

running=True
SPEED = 10
CELL_SIZE = 40
CELL_NUMBER = 20
LENGTH = 1
score = 0
screen = pygame.display.set_mode((CELL_SIZE*CELL_NUMBER,CELL_SIZE*CELL_NUMBER))
gameFont = pygame.freetype.Font('Roboto-Regular.ttf',24)

scoreSurface,rect = gameFont.render("score:",)
#testRect = testSurface.get_rect(center = (400,400))

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

mainGame = Main()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.USEREVENT:
            mainGame.update()
           
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP:
                    #dont let snake go opposite direction
                    if mainGame.snake.direction != Vector2(0,1):
                        mainGame.snake.direction = Vector2(0,-1)
                case pygame.K_DOWN:
                    if mainGame.snake.direction != Vector2(0,-1):
                        mainGame.snake.direction = Vector2(0,1)
                case pygame.K_RIGHT:
                    if mainGame.snake.direction != Vector2(-1,0):
                        mainGame.snake.direction = Vector2(1,0)
                case pygame.K_LEFT:
                    if mainGame.snake.direction != Vector2(1,0):
                        mainGame.snake.direction = Vector2(-1,0)
    screen.fill((20, 20, 20))
    mainGame.drawElements()

   

    pygame.display.update()

