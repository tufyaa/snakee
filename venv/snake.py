import pygame
from generator import gen
import obstacle


class Snake:

    x, y = gen([], obstacle.obstacle1)

    len = 1

    body = []

    def new(self, body, obstacle):
        self.x, self.y = gen(body, obstacle)
        self.body.append((self.x, self.y))

    vx = 0
    vy = 0

    color = pygame.image.load('imag/pixil-frame-21.png')
