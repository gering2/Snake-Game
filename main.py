import pygame
import pygame.freetype
import snake

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Snake')

running=True
SCREEN_SIZE = (800,800)
SPEED = 10
LENGTH = 1
score = 0
initSnake = snake.Snake(SPEED,LENGTH)
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
gameFont = pygame.freetype.Font('Roboto-Regular.ttf',24)
testSurface = pygame.Surface((10,10))
testSurface.fill((255,255,255))
scoreSurface,rect = gameFont.render("score:",(250,250, 250))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.fill((25, 25, 25))
    screen.blit(scoreSurface,(680,30))
    screen.blit(testSurface,(10,10))
    clock.tick(60)

    pygame.display.update()

