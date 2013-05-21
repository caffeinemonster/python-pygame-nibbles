#pgnibbles with classes
import random, pygame, time
from pygame.locals import *
wWIDTH = 640
wHEIGHT = 480
GSIZE = 10
GWIDTH=int(wWIDTH / GSIZE)
GHEIGHT=int(wHEIGHT / GSIZE)
class csnake():
    def __init__(self):
	direction = 0
	self.data = []
	self.alive = 1
    def add (self, x, y):
	self.data.insert(0,(x,y))
    def head(self):
	r = self.data[0]
	return r
    def body(self):
	r = self.data
	return r
    def remove(self):
	self.data.pop()
class capple():
    def __inti__(self):
	self.data = []
    def add(self,x,y):
	self.data=[]
	self.data.append((x,y))
while (1):
    pygame.init()
    GCLOCK = pygame.time.Clock()
    GSURF = pygame.display.set_mode((wWIDTH, wHEIGHT))
    apple = capple()
    snake = csnake()
    snake.direction=K_RIGHT
    sx = random.randint(5, GWIDTH - 6)
    sy = random.randint(5, GHEIGHT - 6)
    snake.add(sx,sy)
    snake.add(sx-1,sy)
    apple.add(random.randint(0, GWIDTH - 1),random.randint(0, GHEIGHT - 1))
    while(1):
	for event in pygame.event.get():
            if event.type == QUIT:
        	quit()    
            elif event.type == KEYDOWN:
                if ((event.key == K_LEFT) and snake.direction != K_RIGHT):
                    snake.direction = K_LEFT
                if (event.key == K_RIGHT) and snake.direction != K_LEFT:
                    snake.direction = K_RIGHT
                if (event.key == K_UP) and snake.direction != K_DOWN:
                    snake.direction = K_UP
                if (event.key == K_DOWN) and snake.direction != K_UP:
                    snake.direction = K_DOWN
                if event.key == K_ESCAPE:
                    quit()
        if snake.data[0][0] == -1 or snake.data[0][0] == GWIDTH or snake.data[0][1] == -1 or snake.data[0][1] == GHEIGHT:
            snake.alive = 0
	for body in snake.data[1:]:
	    if (body == snake.head()):
	        snake.alive = 0
	if snake.data[0][0] == apple.data[0][0] and snake.data[0][1] == apple.data[0][1]:
            apple.add(random.randint(0, GWIDTH - 1),random.randint(0, GHEIGHT - 1))
        else:
	    snake.remove()
	if snake.direction == K_UP:
            snake.add(snake.data[0][0], snake.data[0][1] - 1)
        elif snake.direction == K_DOWN:
            snake.add(snake.data[0][0], snake.data[0][1] + 1)
        elif snake.direction == K_LEFT:
            snake.add(snake.data[0][0] - 1, snake.data[0][1])
        elif snake.direction == K_RIGHT:
            snake.add(snake.data[0][0] + 1, snake.data[0][1])
        GSURF.fill((0,0,0))
	for co in snake.data:
            pygame.draw.circle(GSURF, (0, 255, 0), (co[0]*GSIZE+(GSIZE/2),co[1]*GSIZE+(GSIZE/2)), GSIZE/2, 2)
        pygame.draw.circle(GSURF, (255, 0, 0), (apple.data[0][0]*GSIZE+(GSIZE/2),apple.data[0][1]*GSIZE+(GSIZE/2)), GSIZE/2, 2)
        pygame.display.update()
        GCLOCK.tick(15)
	if snake.alive==0:
	    break
