from generator import gen
import pygame
import obstacle


class Boost:
    color = 0

    def __init__(self, col):
        self.color = col
    x, y = gen([], obstacle.obstacle1)

    count = 0

    coords = (x, y)

    def new(self, body, obstacle):
        self.x, self.y = gen(body, obstacle)
        self.coords = (self.x, self.y)


class Blockboost:
    def __init__(self, col):
        self.color = col
    x = 0
    y = 0

    body = []

    def new(self, body, obstacle):
        self.x, self.y = gen(body, obstacle)
        for i in range(5):
            for j in range(5):
                self.body.append((self.x + i, self.y + j))

    def draw(self, field, sizecell):
        field.blit(self.color, (self.x*sizecell, self.y *
                   sizecell, 5*sizecell, 5*sizecell))
