from generator import gen
import pygame
import obstacle
import main


class Boost:
    x, y = gen([], obstacle.obstacle1)

    count = 0

    coords = (x, y)

    def new(self, body, obstacle):
        self.x, self.y = gen(body, obstacle)
        self.coords = (self.x, self.y)


class Apple(Boost):
    color = pygame.image.load('imag/applenorm1.png')


class Fast(Boost):
    color = pygame.image.load('imag/fast.png')


class Slow(Boost):
    color = pygame.image.load('imag/slow.png')


class MultiApple(Boost):
    color = pygame.image.load('imag/multiapple.png')


class BlockboostFast:
    color = pygame.image.load('imag/fastblock1.png')
    x = 0
    y = 0

    body = []

    def new(self, body, obstacle):
        self.x, self.y = gen(body, obstacle)
        for i in range(5):
            for j in range(5):
                self.body.append((self.x + i, self.y + j))

    def draw(self, field):
        field.blit(self.color, (self.x*main.sizecell, self.y *
                   main.sizecell, 5*main.sizecell, 5*main.sizecell))


class BlockboostSlow:
    color = pygame.image.load('imag/slowblock1.png')
    x = 0
    y = 0

    body = []

    def new(self, body, obstacle):
        self.x, self.y = gen(body, obstacle)
        for i in range(5):
            for j in range(5):
                self.body.append((self.x + i, self.y + j))

    def draw(self, field):
        field.blit(self.color, (self.x*main.sizecell, self.y *
                   main.sizecell, 5*main.sizecell, 5*main.sizecell))
