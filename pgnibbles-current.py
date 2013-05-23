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

    def seedrandom(self, xy):
        self.x = xy[0]
        self.y = xy[1]
        self.colour = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
        self.seed(xy, (3, 20), 2, (255, 255, 255), 20)
        self.colour = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

    def seed(self, xy, speed, isize, rgbcolour, ilife):
        self.life = random.randint(1, ilife)
        self.colour = rgbcolour
        self.size = random.randint(1, isize)
        self.x = xy[0]
        self.y = xy[1]
        if random.randint(0, 1) == 1:
            self.speedx = random.randint(speed[0], speed[1])
        else:
            self.speedx = -random.randint(speed[0], speed[1])
        if random.randint(0, 1) == 1:
            self.speedy = random.randint(speed[0], speed[1])
        else:
            self.speedy = -random.randint(speed[0], speed[1])
        self.alive = 1

    def move(self):  # move the particle
        if self.life > 0:
            self.x = self.x + self.speedx
            self.y = self.y + self.speedy
            self.life -= 1
        else:
            self.alive = 0


class cparticles():  # particle group class
    def __init__(self):
        self.particles = []

    def seed(self, x, y, speed, life, amount, rgbcolour, size):
        self.killold()
        for i in range(1, amount):
            part = cparticle()
            # seed(self, xy, speed, isize, rgbcolour, ilife) # reference
            part.seedrandom((x, y))
            part.seed((x, y), (3, speed), size, rgbcolour, life)
            self.particles.insert(0, part)

    def seedrandom(self, xy, amount):
        self.killold()
        for i in range(1, amount):
            part = cparticle()
            part.seedrandom(xy)
            self.particles.insert(0, part)

    def move(self):
        for p in self.particles:
            p.move()

    def killold(self):
        for p in self.particles:
            if p.alive <= 0:
                del(p)


class csounds():  # sound effects class
    def __init__(self):
        self.enabled = 1  # sfx enabled
        self.sndeat = pygame.mixer.Sound('sndfx/beep.wav')
        self.snddead = pygame.mixer.Sound('sndfx/dead.wav')

    def fxdead(self):
        if self.enabled:
            self.snddead.play()

    def fxeat(self):
        if self.enabled:
            self.sndeat.play()


def terminate():  # quit function
    pygame.mixer.quit()
    pygame.quit()
    quit()


def main():  # main game loop
    r = 1
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
    #particles = cparticles() now declared as global
    apple.add(random.randint(0, GWIDTH - 1), random.randint(0, GHEIGHT - 1))
    while(1):
        for event in pygame.event.get():
            # detact and process keyboard events
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

        # is the snake within the game area
        if snake.data[0][0] == -1 or snake.data[0][0] == GWIDTH or snake.data[0][1] == -1 or snake.data[0][1] == GHEIGHT:
            snake.alive = 0
        #else:
        #    particles.seed((snake.data[0][0] * GSIZE), (snake.data[0][1] * GSIZE), 5, 5, 2, (0,255,0), 2)

        for body in snake.data[1:]:
            if (body == snake.head()):
                snake.alive = 0

        # is snake location == apple
        if snake.data[0][0] == apple.data[0][0] and snake.data[0][1] == apple.data[0][1]:
            # seed(self, x, y, speed, life, amount, rgbcolour, size)
            particles.seed((apple.data[0][0] * GSIZE), (apple.data[0][1] * GSIZE), 10, 25, 50, (0,255,0), random.randint(1,5))
            particles.seed((apple.data[0][0] * GSIZE), (apple.data[0][1] * GSIZE), 15, 25, 50, (255,0,0), random.randint(1,4))
            particles.seedrandom((GSURF.get_width() / 2, 10), 100)
            particles.seedrandom((GSURF.get_width() - 20, 475), 100)
            apple.add(random.randint(0, GWIDTH - 1), random.randint(0, GHEIGHT - 1))
            particles.seed((apple.data[0][0] * GSIZE), (apple.data[0][1] * GSIZE), 20, 5, 50, (255,0,0), random.randint(1,3))
            #for i in range(2, 16):
            pygame.mixer.music.queue('sndmusic/TRACK' + str(random.randint(1,16)) + '.mp3')
            score.add(1)
            sfx.fxeat()
        else:
            snake.remove()

        if snake.direction == K_UP:  # move snake
            snake.add(snake.data[0][0], snake.data[0][1] - 1)
        elif snake.direction == K_DOWN:
            snake.add(snake.data[0][0], snake.data[0][1] + 1)
        elif snake.direction == K_LEFT:
            snake.add(snake.data[0][0] - 1, snake.data[0][1])
        elif snake.direction == K_RIGHT:
            snake.add(snake.data[0][0] + 1, snake.data[0][1])

        # draw game elements
        GSURF.fill((0, 0, 0))
        for p in particles.particles:
            if p.alive == 1:
                pygame.draw.circle(GSURF, p.colour, (p.x + (GSIZE / 2), p.y + (GSIZE / 2)), p.size)
        particles.move()
        if snake.alive:
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
        # check to see if snake is alive
        if snake.alive == 0:
            if score.score > 0:
                print(("You died your score was " + str(score.score)))
            sfx.fxdead()
            particles.seedrandom((snake.data[0][0] * GSIZE, snake.data[0][1] * GSIZE), 200)
            particles.seedrandom((apple.data[0][0] * GSIZE, apple.data[0][1] * GSIZE), 200)
            return r
            break

        if r != 1:
            return r

if __name__ == "__main__":
    global particles
    particles = cparticles()
    r = 1
    pygame.init()
    GCLOCK = pygame.time.Clock()
    GSURF = pygame.display.set_mode((wWIDTH, wHEIGHT))  # main game surface
    pygame.display.set_caption("pgnibbles")
    #pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    pygame.mixer.init()
    pygame.mixer.music.load('sndmusic/TRACK1.mp3')
    #for i in range(2, 16):
    #    pygame.mixer.music.queue('sndmusic/TRACK' + str(i) + '.mp3')
    pygame.mixer.music.play(0)
    pygame.mouse.set_visible(0)
    #pygame.display.toggle_fullscreen()
    while r != 0:  # quit if return not equal to 0
        r = main()
    pygame.mouse.set_visible(1)