#pygame most minimal nibbles - still removing code - any suggestions welcome.
import random, time, pygame
from pygame.locals import *
wWIDTH = 640
wHEIGHT = 480
GSIZE = 10
GRIDWIDTH = int(wWIDTH / GSIZE)
GRIDHEIGHT = int(wHEIGHT / GSIZE)

def main():
    global GCLOCK, GSURF, BASICFONT
    pygame.init()
    GCLOCK = pygame.time.Clock()
    GSURF = pygame.display.set_mode((wWIDTH, wHEIGHT))
    while True:
        gameLoop()
def stop():
    pygame.quit()
    quit()
def gameLoop():
    startx = random.randint(5, GRIDWIDTH - 6)
    starty = random.randint(5, GRIDHEIGHT - 6)
    snakeCoords = [(startx, starty), (startx-1, starty)]
    direction = K_RIGHT
    apple = (random.randint(0, GRIDWIDTH - 1), random.randint(0, GRIDHEIGHT - 1))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                stop()
            elif event.type == KEYDOWN:
                if ((event.key == K_LEFT or event.key == K_a) and direction != K_RIGHT):
                    direction = K_LEFT
                if (event.key == K_RIGHT or event.key == K_d) and direction != K_LEFT:
                    direction = K_RIGHT
                if (event.key == K_UP or event.key == K_w) and direction != K_DOWN:
                    direction = K_UP
                if (event.key == K_DOWN or event.key == K_s) and direction != K_UP:
                    direction = K_DOWN
                if event.key == K_ESCAPE:
                    stop()
        if snakeCoords[0][0] == -1 or snakeCoords[0][0] == GRIDWIDTH or snakeCoords[0][1] == -1 or snakeCoords[0][1] == GRIDHEIGHT:
            return
        for snakeBody in snakeCoords[1:]:
            if (snakeCoords[0][0], snakeCoords[0][1]) == snakeBody:
                return
        if snakeCoords[0][0] == apple[0] and snakeCoords[0][1] == apple[1]:
            apple = (random.randint(0, GRIDWIDTH - 1), random.randint(0, GRIDHEIGHT - 1))
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
        GSURF.fill((0,0,0))
	for co in snakeCoords:
            pygame.draw.circle(GSURF, (0, 255, 0), (co[0]*GSIZE+(GSIZE/2),co[1]*GSIZE+(GSIZE/2)), GSIZE/2, 2)
        pygame.draw.circle(GSURF, (255, 0, 0), (apple[0]*GSIZE+(GSIZE/2),apple[1]*GSIZE+(GSIZE/2)), GSIZE/2, 2)
        pygame.display.update()
        GCLOCK.tick(15)
if __name__ == '__main__':
    main()
