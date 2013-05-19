import random
import time
import pygame
import sys
from pygame.locals import *

# define variables
FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#define colours
#WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
BGCOLOR = BLACK

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

def main():
    global MAINCLOCK, MAINSURF, BASICFONT
    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    MAINSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snakey')
    while True:
        gameLoop()

def gameLoop():
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    snakeCoords = [(startx, starty), (startx-1, starty)]
    direction = RIGHT
    apple = (random.randint(0, CELLWIDTH - 1), random.randint(0, CELLHEIGHT - 1))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                if (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                if (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                if (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                if event.key == K_ESCAPE:
                    terminate()
        if snakeCoords[0][0] == -1 or snakeCoords[0][0] == CELLWIDTH or snakeCoords[0][1] == -1 or snakeCoords[0][1] == CELLHEIGHT:
            return
        for snakeBody in snakeCoords[1:]:
            if (snakeCoords[0][0], snakeCoords[0][1]) == snakeBody:
                return
        if snakeCoords[0][0] == apple[0] and snakeCoords[0][1] == apple[1]:
            apple = (random.randint(0, CELLWIDTH - 1), random.randint(0, CELLHEIGHT - 1))
        else:
            snakeCoords.pop()
        
        if direction == UP:
            snakeCoords.insert(0, (snakeCoords[0][0], snakeCoords[0][1] - 1))
        elif direction == DOWN:
            snakeCoords.insert(0, (snakeCoords[0][0], snakeCoords[0][1] + 1))
        elif direction == LEFT:
            snakeCoords.insert(0, (snakeCoords[0][0] - 1, snakeCoords[0][1]))
        elif direction == RIGHT:
            snakeCoords.insert(0, (snakeCoords[0][0] + 1, snakeCoords[0][1]))
        MAINSURF.fill(BGCOLOR)
        drawSnake(snakeCoords)
        drawApple(apple)
#        drawScore(len(snakeCoords))
        pygame.display.update()
        MAINCLOCK.tick(FPS)
#def drawScore(score):
#    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
#    scoreRect = scoreSurf.get_rect()
#    scoreRect.topleft = (WINDOWWIDTH - 80, 10)
#    MAINSURF.blit(scoreSurf, scoreRect)
def drawSnake(snakeCoords):
    for coord in snakeCoords:
        x = coord[0] * CELLSIZE
        y = coord[1] * CELLSIZE
        coordRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        #pygame.draw.rect(MAINSURF, GREEN, coordRect)
	pygame.draw.circle(MAINSURF, GREEN, (x+(CELLSIZE/2),y+(CELLSIZE/2)), CELLSIZE/2, 2)
def drawApple(coord):
    x = coord[0] * CELLSIZE
    y = coord[1] * CELLSIZE
#    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
#    pygame.draw.rect(MAINSURF, RED, appleRect)
    pygame.draw.circle(MAINSURF, RED, (x+(CELLSIZE/2),y+(CELLSIZE/2)), CELLSIZE/2, 2)
if __name__ == '__main__':
    main()
