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
    def __init__(self, sxy):
        #self.direction = 0  # set initial direction
        self.data = []  # init snake data array
        self.alive = 1  # let it live
        self.direction = K_RIGHT  # set initial player direction
        self.add(sxy[0] - 2, sxy[1])  # add snake body
        self.add(sxy[0] - 1, sxy[1])  # add snake body
        self.add(sxy[0], sxy[1])  # add snake body

    def add(self, x, y):  # add snake part
        self.data.insert(0, (x, y))  # add snake part @xy loc

    def head(self):
        r = self.data[0]  # return head loc
        return r  # return r

    def body(self):
        r = self.data[1:]  # return all parts but 1st (head)
        return r  # return r

    def remove(self):
        self.data.pop()  # remove trailing end of snake


class capple():  # apple class
    def __init__(self):
        self.data = []  # define empty array

    def add(self, x, y):  # add apple at xy loc
        self.data = []  # clear array
        self.data.append((x, y))  # add new apple loc


class cscore():  # score class
    def __init__(self):
        self.score = 0  # var to hold score

    def add(self, s):  # add score
        self.score = self.score + s


class cparticle():  # particle class
    def __init__(self):
        # set init vars
        self.size = 0
        self.x = 0
        self.y = 0
        self.speedx = 10
        self.speedy = 10
        self.life = 0
        self.totallife = 0
        self.alive = 0
        self.colour = (255, 255, 255)
        self.gravity = (0, 1)

    def seedrandom(self, xy): # seed random particle
        self.x = xy[0]  # set xloc
        self.y = xy[1]  # set yloc
        #self.colour = (random.randint(1, 200), random.randint(1, 200), random.randint(1, 200))
        self.seed(xy, (3, 20), random.randint(1, 5), (255, 255, 255), 20)  # seed
        self.colour = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))  # set random colour

    def seed(self, xy, speed, isize, rgbcolour, ilife):  # seed particle
        self.life = random.randint(1, ilife)  # set life
        self.totallife = self.life  # set totlife
        self.colour = rgbcolour  # set rgb colour
        self.size = random.randint(1, isize)  # random particle size
        self.x = xy[0]  # set xloc
        self.y = xy[1]  # set yloc
        if random.randint(0, 1) == 1:  # random left/right
            self.speedx = random.randint(speed[0], speed[1])
        else:
            self.speedx = -random.randint(speed[0], speed[1])
        if random.randint(0, 1) == 1:  # random up/down
            self.speedy = random.randint(speed[0], speed[1])
        else:
            self.speedy = -random.randint(speed[0], speed[1])
        self.alive = 1  # make it live

    def move(self):  # move the particle
        if self.life > 0:
            self.x = self.x + self.speedx + (self.gravity[0] * (self.totallife - self.life))
            self.y = self.y + self.speedy + (self.gravity[1] * (self.totallife - self.life))
            self.life -= 1
        else:
            self.alive = 0

class cparticles():  # particle group class
    def __init__(self):
        self.particles = []

    def seed(self, x, y, speed, life, amount, rgbcolour, size):
        self.killold()  # remove old particles
        for i in range(1, amount):  # loop for amont
            part = cparticle()  # create new particle
            # seed(self, xy, speed, isize, rgbcolour, ilife) # reference
            # part.seedrandom((x, y))  # seed particle at xy
            part.seed((x, y), (3, speed), size, rgbcolour, life)
            self.particles.insert(0, part)

    def seedrandom(self, xy, amount):  # seed random amount of particles at xy
        self.killold()  # remove old particles
        for i in range(1, amount):  # loop for amount
            part = cparticle()  # create a particle
            part.seedrandom(xy)  # seed particle at xy location
            self.particles.insert(0, part)  # add particle to array

    def move(self):  # moves the particles
        for p in self.particles:  # for all particles
            p.move()  # move the particle

    def killold(self):  # removes old particles
        for p in self.particles:  # for all particles
            if p.alive <= 0:  # if they are dead or less than dead
                del(p)  # remove them from the array


class csounds():  # sound effects class
    def __init__(self):  # init sound class
        self.enabled = 1  # sfx enabled
        self.sndeat = pygame.mixer.Sound('sndfx/beep.wav')  # load sound
        self.snddead = pygame.mixer.Sound('sndfx/dead.wav')  # load sound
        self.sndbonus = pygame.mixer.Sound('sndfx/bonus.wav')  # load sound

    def toggle_enable(self):
        if self.enabled:
            self.enabled = 0  # disable sfx
        else:
            self.enabled = 1  # enable sfx

    def fxdead(self):  # dead
        if self.enabled:
            self.snddead.play()

    def fxeat(self):  # eat
        if self.enabled:
            self.sndeat.play()

    def fxbonus(self):  # bonus
        if self.enabled:
            self.sndbonus.play()


def terminate():  # quit function - tidy up
    pygame.mixer.quit()  # quit the game mixer
    pygame.quit()  # quit pygame
    quit()  # quit python  #


def main():  # main game loop
    r = 1  # set return value = 1  # everthing is ok continue to run
    sfx = csounds()  # init my sounds module
    apple = capple()  # init apple
    sxy = ['0', '0']  # define var for snake init to hold xy vars
    sxy[0] = random.randint(5, GWIDTH - 6)  # generate random snake coords
    sxy[1] = random.randint(5, GHEIGHT - 6)  # generate random snake coords
    snake = csnake(sxy)  # initialise snake with grid coords
    score = cscore()  # init score class
    #apple.add(random.randint(0, GWIDTH - 1), random.randint(0, GHEIGHT - 1))  # add an apple
    apple.add(0, 0)
    while(1):  # do for a while (game loop)
        for event in pygame.event.get():  # handle events
            if event.type == QUIT:  # ctrl+c
                r = 0  # return 0 = (game is over)
            elif event.type == KEYDOWN:  # down arrow
                if event.key == K_LEFT and snake.direction != K_RIGHT:
                    snake.direction = K_LEFT  # left arrow
                if event.key == K_RIGHT and snake.direction != K_LEFT:
                    snake.direction = K_RIGHT  # right arrow
                if event.key == K_UP and snake.direction != K_DOWN:
                    snake.direction = K_UP  # up arrow
                if event.key == K_DOWN and snake.direction != K_UP:
                    snake.direction = K_DOWN  # down arrow
                if event.key == K_ESCAPE:
                    r = 0  # return 0 = (game is over)
                if event.key == K_s:
                    sfx.toggle_enable()
        if snake.data[0][0] == -1 or snake.data[0][0] == GWIDTH or snake.data[0][1] == -1 or snake.data[0][1] == GHEIGHT:  # # is the snake within the game area
            snake.alive = 0  # snake is dead, they're all dead dave everybody's dead.'
        #else:
        #    particles.seed((snake.data[0][0] * GSIZE), (snake.data[0][1] * GSIZE), 5, 5, 2, (0,255,0), 2)
        #for body in snake.data[1:]:  # for each part in the body of the snake
        sbody = snake.body()
        for body in sbody:  # for each part in the body of the snake
            if (body == snake.head()):  # if the snakes head is eating the body
                snake.alive = 0  # snake is dead, they're all dead dave everybody's dead.'
        if snake.data[0][0] == apple.data[0][0] and snake.data[0][1] == apple.data[0][1]:  # is the snake eating ?
            # seed(self, x, y, speed, life, amount, rgbcolour, size)  # for refernce
            particles.seed((apple.data[0][0] * GSIZE), (apple.data[0][1] * GSIZE), 10, 25, 50, (0, 127, 0), random.randint(1, 3))  # seed particles
            particles.seed((apple.data[0][0] * GSIZE), (apple.data[0][1] * GSIZE), 15, 25, 50, (127, 0, 0), random.randint(1, 3))  # seed particles
            particles.seed((apple.data[0][0] * GSIZE), (apple.data[0][1] * GSIZE), 25, 15, 40, (0, 255, 0), random.randint(1, 2))  # seed particles
            particles.seed((apple.data[0][0] * GSIZE), (apple.data[0][1] * GSIZE), 25, 15, 40, (255, 255, 0), random.randint(1, 2))  # seed particles
            particles.seedrandom((GSURF.get_width() / 2, 10), 100)  # seed particles
            particles.seedrandom((GSURF.get_width() - 20, 475), 100)  # seed particles
            sadd = 0
            if snake.alive == 1:  # if the snake is alive add score
                if apple.data[0][0] == 0 and apple.data[0][1] == 0:  # apple is in top left corner
                    if sadd == 0:
                        sadd = 5
                        sfx.fxbonus()
                if apple.data[0][0] == (GWIDTH - 1) and apple.data[0][1] == 0:  # apple is in top right corner
                    if sadd == 0:
                        sadd = 5
                        sfx.fxbonus()
                if apple.data[0][0] == 0 and apple.data[0][1] == (GHEIGHT - 1):  # apple is in bottom left corner
                    if sadd == 0:
                        sadd = 5
                        sfx.fxbonus()
                if apple.data[0][0] == (GWIDTH - 1) and apple.data[0][1] == (GHEIGHT - 1):  # apple is in bottom right corner
                    if sadd == 0:
                        sadd = 5
                        sfx.fxbonus()
                if apple.data[0][0] == 0 or apple.data[0][0] == (GWIDTH - 1):  # apple is on edge
                    if sadd == 0:
                        sadd = 2
                        sfx.fxbonus()
                if apple.data[0][1] == 0 or apple.data[0][1] == (GHEIGHT - 1):  # apple is on edge
                    if sadd == 0:
                        sadd = 2
                        sfx.fxbonus()
                else:  # somewhere on screen
                    if sadd == 0:
                        sadd = 1
                score.add(sadd)  # add sadd to the score
            apple.add(random.randint(0, GWIDTH - 1), random.randint(0, GHEIGHT - 1))  # add a new apple
            particles.seed((apple.data[0][0] * GSIZE), (apple.data[0][1] * GSIZE), 20, 5, 50, (255, 0, 0), random.randint(1, 3))  # seed particles
            pygame.mixer.music.queue('sndmusic/TRACK' + str(random.randint(1, 16)) + '.mp3')  # choose another track to play next
            sfx.fxeat()  # play the eat sound effect
        else:
            snake.remove()  # remove the last body part
        if snake.direction == K_UP:  # detect relevant keypress
            snake.add(snake.data[0][0], snake.data[0][1] - 1)  # move the snake
        elif snake.direction == K_DOWN:  # detect relevant keypress
            snake.add(snake.data[0][0], snake.data[0][1] + 1)  # move the snake
        elif snake.direction == K_LEFT:  # detect relevant keypress
            snake.add(snake.data[0][0] - 1, snake.data[0][1])  # move the snake
        elif snake.direction == K_RIGHT:  # detect relevant keypress
            snake.add(snake.data[0][0] + 1, snake.data[0][1])  # move the snake
        GSURF.fill((0, 0, 0))  # fill game surface with black

        #b = pygame.sprite.Sprite() # create sprite
        #b.image = pygame.image.load("imgs/fireball.png").convert_alpha() # load ball image
        #b.image.set_colorkey(-1)
        #b.rect = pygame.Rect(0,0,10,10)
        #b.image.get_rect() # use image extent value

        for p in particles.particles:  # draw particles
            if p.alive == 1:  # if the particle is alive
                #if p.image == '':
                pygame.draw.circle(GSURF, p.colour, (p.x + (GSIZE / 2), p.y + (GSIZE / 2)), p.size)  # render particle
                #else:
                    #b.rect.topleft = [p.x, p.y] # put the ball in the top left corner
                    #b.rect.inflate(-20,-20)
                    #GSURF.blit(b.image, b.rect)

        particles.move()  # move the particles to their next location
        if snake.alive:  # if the snake is alive
            for co in snake.data:  # draw the snake
                pygame.draw.circle(GSURF, (0, 255, 0), (co[0] * GSIZE + (GSIZE / 2), co[1] * GSIZE + (GSIZE / 2)), GSIZE / 2, 2)  # draw circle to surface
            pygame.draw.circle(GSURF, (255, 0, 0), (apple.data[0][0] * GSIZE + (GSIZE / 2), apple.data[0][1] * GSIZE + (GSIZE / 2)), GSIZE / 2, 2)  # draw circle to surface
        if pygame.font:  # if fonts are available
            font = pygame.font.Font(None, 24)  # set font and size
            text = font.render("Score : " + str(score.score), 1, (255, 255, 255))  # set text and colour
            textpos = text.get_rect(centerx=GSURF.get_width() / 2)  # set text pos
            GSURF.blit(text, textpos)  # render text
            text = font.render("pgnibbles", 1, (255, 255, 255))  # set text and colour
            textpos = text.get_rect(center=(600, 465))  # set text pos
            GSURF.blit(text, textpos)  # render text
        pygame.display.flip()  # render game objects
        GCLOCK.tick(30)  #  advance at 30 fps
        if snake.alive == 0:  # if the snake is alive
            if score.score > 0:  # if the score is greater than 0
                print(("You died your score was " + str(score.score)))  # print score to terminal
            sfx.fxdead()  # play dead sound effect
            particles.seedrandom((snake.data[0][0] * GSIZE, snake.data[0][1] * GSIZE), 200)  # seed particles
            particles.seedrandom((apple.data[0][0] * GSIZE, apple.data[0][1] * GSIZE), 200)  # seed particles
            return r  #  return value'
            break  # break game loop
        if r != 1:  #  if player is not alive
            return r  # return value

if __name__ == "__main__":  # main function call
    global particles  # declare partical class globally
    particles = cparticles()  # initialise partice array
    r = 1  # set variable for return value
    pygame.init()  # initialise python pygame
    GCLOCK = pygame.time.Clock()  # set game clock
    GSURF = pygame.display.set_mode((wWIDTH, wHEIGHT), pygame.SRCALPHA)  # main game surface
    GSURF.convert_alpha()  # used for transparent sprites
    pygame.display.set_caption("pgnibbles")  # set window name
    pygame.mixer.init()  # initialise mixer
    pygame.mixer.music.load('sndmusic/TRACK' + str(random.randint(1, 16)) + '.mp3')  # queue random track
    #pygame.mixer.music.play()  # play music
    pygame.mouse.set_visible(0)  # hide mouse
    while r != 0:  # quit if return not equal to 0 (esc key hit)
        r = main()  # get return value from main loop (1 == OK ... 0 == exit)
    pygame.mouse.set_visible(1)  # show mouse