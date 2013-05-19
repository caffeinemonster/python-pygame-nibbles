import random
import time
import pygame
from pygame.locals import *
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 10
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)
def main():
    global MAINCLOCK, MAINSURF, BASICFONT
    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    MAINSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    while True:
        gameLoop()
def stop():
    pygame.quit()
    quit()
def gameLoop():
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    snakeCoords = [(startx, starty), (startx-1, starty)]
    direction = K_RIGHT
    apple = (random.randint(0, CELLWIDTH - 1), random.randint(0, CELLHEIGHT - 1))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                stop()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != K_RIGHT:
                    direction = K_LEFT
                if (event.key == K_RIGHT or event.key == K_d) and direction != K_LEFT:
                    direction = K_RIGHT
                if (event.key == K_UP or event.key == K_w) and direction != K_DOWN:
                    direction = K_UP
                if (event.key == K_DOWN or event.key == K_s) and direction != K_UP:
                    direction = K_DOWN
                if event.key == K_ESCAPE:
                    stop()
        if snakeCoords[0][0] == -1 or snakeCoords[0][0] == CELLWIDTH or snakeCoords[0][1] == -1 or snakeCoords[0][1] == CELLHEIGHT:
            return
        for snakeBody in snakeCoords[1:]:
            if (snakeCoords[0][0], snakeCoords[0][1]) == snakeBody:
                return
        if snakeCoords[0][0] == apple[0] and snakeCoords[0][1] == apple[1]:
            apple = (random.randint(0, CELLWIDTH - 1), random.randint(0, CELLHEIGHT - 1))
        else:
            snakeCoords.pop()
        if direction == K_UP:
            snakeCoords.insert(0, (snakeCoords[0][0], snakeCoords[0][1] - 1))
        elif direction == K_DOWN:
            snakeCoords.insert(0, (snakeCoords[0][0], snakeCoords[0][1] + 1))
        elif direction == K_LEFT:
            snakeCoords.insert(0, (snakeCoords[0][0] - 1, snakeCoords[0][1]))
        elif direction == K_RIGHT:
            snakeCoords.insert(0, (snakeCoords[0][0] + 1, snakeCoords[0][1]))
        MAINSURF.fill((0,0,0))
        drawSnake(snakeCoords)
        drawApple(apple)
        pygame.display.update()
        MAINCLOCK.tick(15)
def drawSnake(snakeCoords):
    for coord in snakeCoords:
        x = coord[0] * CELLSIZE
        y = coord[1] * CELLSIZE
	pygame.draw.circle(MAINSURF, (0, 255, 0), (x+(CELLSIZE/2),y+(CELLSIZE/2)), CELLSIZE/2, 2)
def drawApple(coord):
    x = coord[0] * CELLSIZE
    y = coord[1] * CELLSIZE
    pygame.draw.circle(MAINSURF, (255, 0, 0), (x+(CELLSIZE/2),y+(CELLSIZE/2)), CELLSIZE/2, 2)
if __name__ == '__main__':
    main()
