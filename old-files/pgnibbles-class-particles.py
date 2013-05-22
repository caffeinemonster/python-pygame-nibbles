#pgnibbles with classes
import random
import pygame
from pygame.locals import *
wWIDTH = 640
wHEIGHT = 480
GSIZE = 10
GWIDTH = int(wWIDTH / GSIZE)
GHEIGHT = int(wHEIGHT / GSIZE)


class csnake():  # snake class
    def __init__(self):
        self.direction = 0
        self.data = []
        self.alive = 1

    def add(self, x, y):
        self.data.insert(0, (x, y))

    def head(self):
        r = self.data[0]
        return r

    def body(self):
        r = self.data
        return r

    def remove(self):
        self.data.pop()


class capple():  # apple class
    def __init__(self):
        self.data = []

    def add(self, x, y):
        self.data = []
        self.data.append((x, y))


class cscore():  # score class
    def __init__(self):
        self.score = 0

    def add(self, s):
        self.score = self.score + s


class cparticle():  # particle class
    def __init__(self):
        self.size = 0
        self.x = 0
        self.y = 0
        self.speedx = 10
        self.speedy = 10
        self.life = 0
        self.alive = 0
        self.colour = (255, 255, 255)

    def seed(self, xloc, yloc, ispeed, ilife):
        self.colour = (255, 255, 255)
        self.speed = ispeed
        self.life = random.randint(1, ilife)
        r = random.randint(0, 1)
        if (r == 1):
            self.speedx = random.randint(0, ispeed)
        else:
            self.speedx = -(random.randint(0, ispeed))
        r = random.randint(0, 1)
        if (r == 1):
            self.speedy = random.randint(0, ispeed)
        else:
            self.speedy = -(random.randint(0, ispeed))
        self.x = xloc
        self.y = yloc
        self.colour = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        self.alive = 1
        self.size = random.randint(1, 3)

    def move(self):
        if self.life > 0:
            self.x = self.x + self.speedx
            self.y = self.y + self.speedy
            self.life -= 1
        else:
            self.alive = 0


class cparticles():  # particle group class
    def __init__(self):
        self.particles = []

    def seed(self, x, y, speed, life, amount):
        self.killold()
        for i in range(1, amount):
            part = cparticle()
            part.seed(x, y, speed, life)
            self.particles.insert(0, part)

    def move(self):
        for p in self.particles:
            p.move()

    def killold(self):
        for p in self.particles:
            if p.alive != 1:
                del(p)


class csounds():  # sound effects class
    def __init__(self):
        #super(csounds, self).__init__()
        self.sndeat = pygame.mixer.Sound('beep.wav')
        self.snddead = pygame.mixer.Sound('dead.wav')

    def fxdead(self):
        self.snddead.play()

    def fxeat(self):
        self.sndeat.play()


def terminate():  # quit function
    pygame.mixer.quit()
    pygame.quit()
    quit()


def main():  # main game loop
    r = 1
    pygame.init()
    GCLOCK = pygame.time.Clock()
    GSURF = pygame.display.set_mode((wWIDTH, wHEIGHT))
    pygame.display.set_caption("pgnibbles")
    sfx = csounds()
    apple = capple()
    snake = csnake()
    snake.direction = K_RIGHT
    sx = random.randint(5, GWIDTH - 6)
    sy = random.randint(5, GHEIGHT - 6)
    snake.add(sx - 2, sy)
    snake.add(sx - 1, sy)
    snake.add(sx, sy)
    score = cscore()
    particles = cparticles()
    apple.add(random.randint(0, GWIDTH - 1), random.randint(0, GHEIGHT - 1))
    while(1):
        for event in pygame.event.get():
            if event.type == QUIT:
                r = 0
            elif event.type == KEYDOWN:
                if event.key == K_LEFT and snake.direction != K_RIGHT:
                    snake.direction = K_LEFT
                if event.key == K_RIGHT and snake.direction != K_LEFT:
                    snake.direction = K_RIGHT
                if event.key == K_UP and snake.direction != K_DOWN:
                    snake.direction = K_UP
                if event.key == K_DOWN and snake.direction != K_UP:
                    snake.direction = K_DOWN
                if event.key == K_ESCAPE:
                    r = 0
        if snake.data[0][0] == -1 or snake.data[0][0] == GWIDTH or snake.data[0][1] == -1 or snake.data[0][1] == GHEIGHT:
            snake.alive = 0
        for body in snake.data[1:]:
            if (body == snake.head()):
                snake.alive = 0
        if snake.data[0][0] == apple.data[0][0] and snake.data[0][1] == apple.data[0][1]:
            particles.seed((apple.data[0][0] * GSIZE), (apple.data[0][1] * GSIZE), 20, 10, 50)
            particles.seed(GSURF.get_width() / 2, 10, 30, 15, 100)
            particles.seed(GSURF.get_width() - 20, 475, 30, 15, 100)
            apple.add(random.randint(0, GWIDTH - 1), random.randint(0, GHEIGHT - 1))
            score.add(1)
            sfx.fxeat()
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
        GSURF.fill((0, 0, 0))
        for p in particles.particles:
            if p.alive == 1:
                pygame.draw.circle(GSURF, p.colour, (p.x + (GSIZE / 2), p.y + (GSIZE / 2)), p.size)
        particles.move()
        for co in snake.data:
            pygame.draw.circle(GSURF, (0, 255, 0), (co[0]*GSIZE+(GSIZE/2),co[1]*GSIZE+(GSIZE/2)), GSIZE/2, 2)
        pygame.draw.circle(GSURF, (255, 0, 0), (apple.data[0][0]*GSIZE+(GSIZE/2),apple.data[0][1]*GSIZE+(GSIZE/2)), GSIZE/2, 2)
        if pygame.font:
            font = pygame.font.Font(None, 24)
            text = font.render("Score : " + str(score.score), 1, (255, 255, 255))
            textpos = text.get_rect(centerx=GSURF.get_width() / 2)
            GSURF.blit(text, textpos)
            text = font.render("pgnibbles", 1, (255, 255, 255))
            textpos = text.get_rect(center=(600, 465))
            GSURF.blit(text, textpos)
        pygame.display.flip()
        GCLOCK.tick(30)
        if snake.alive == 0:
            if (score.score != 0):
                print(("You died your score was " + str(score.score)))
            sfx.fxdead()
            return r
            break

        if r != 1:
            return r

if __name__ == "__main__":
    r = 1
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    ##pygame.mixer.music.set_endevent(SONG_END)
    pygame.mixer.music.load('music/TRACK01.mp3')
    #pygame.mixer.music.load('music/TRACK02.mp3')
    #pygame.mixer.music.queue('music/TRACK03.mp3')
    #pygame.mixer.music.queue('music/TRACK04.mp3')
    #pygame.mixer.music.queue('music/TRACK05.mp3')
    pygame.mixer.music.play(-1)
    #pygame.display.toggle_fullscreen()
    while r != 0:  # quit if return not equal to 0
        r = main()