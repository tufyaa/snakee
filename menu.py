import pygame
import main
import obstacle

import sys

# это главное меню, его описание и его старт
pygame.init()

count = 0
col = pygame.image.load('imag/pixil-frame-21.png')


def change():
    # не смог тут убрать global, не знаю как сделать
    global col, count
    if count % 2 == 0:
        col = pygame.Surface((main.sizecell - 1, main.sizecell - 1))
        col.fill((0, 255, 127))
    else:
        col = pygame.image.load('imag/pixil-frame-21.png')
    count = count + 1
    main.snc = (col)
    print('changed', count)

# класс меню, чтобы на WASD передвигаться в меню


class Menu:
    fontt = pygame.font.SysFont("Arial", 35, bold=True)

    def __init__(self) -> None:
        self.option_surf = []
        self.callback = []
        self.current_option = 0

    def append_option(self, option, callback):
        self.option_surf.append(self.fontt.render(
            option, True, (255, 255, 255)))
        self.callback.append(callback)

    def switch(self, dir):
        self.current_option = max(
            0, min(self.current_option + dir, len(self.option_surf) - 1))

    def draw(self, surf, x, y, gap):
        for i, option in enumerate(self.option_surf):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * gap)
            if i == self.current_option:
                pygame.draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)

    def select(self):
        self.callback[self.current_option]()


def run_menu():
    global col
    with open('score.txt', 'r+') as f:
        score1 = int(f.readline())
        score2 = int(f.readline())
        score3 = int(f.readline())

    # шрифты и тому подобное
    sc = pygame.display.set_mode((main.resolution, main.resolution))
    col = pygame.image.load('imag/pixil-frame-21.png')
    fo = pygame.font.SysFont("Arial", 35, bold=True)
    fon = fo.render(
        f'Records: ', True, (255, 255, 255))
    fon_rect = fon.get_rect()
    fon_rect.topleft = (200, 40)
    sc1 = fo.render(
        f'1) {score1}', True, (255, 255, 255))
    sc1_rect = sc1.get_rect()
    sc1_rect.topleft = (235, 80)
    sc2 = fo.render(
        f'2) {score2}', True, (255, 255, 255))
    sc2_rect = sc2.get_rect()
    sc2_rect.topleft = (235, 120)
    sc3 = fo.render(
        f'3) {score3}', True, (255, 255, 255))
    sc3_rect = sc3.get_rect()
    sc3_rect.topleft = (235, 160)
    # самого меню
    menu = Menu()
    menu.append_option('Level 1', lambda: main.run(obstacle.obstacle0))
    menu.append_option('Level 2', lambda: main.run(obstacle.obstacle1))
    menu.append_option('Level 3', lambda: main.run(obstacle.obstacle2))
    menu.append_option('Level 4', lambda: main.run(obstacle.obstacle3))
    menu.append_option('Level 5', lambda: main.run(obstacle.obstacle4))
    menu.append_option('Change color', change)
    menu.append_option("Quit", quit)

    running = True

    # главный цикл, который отрисовывает все и считывает нажатия
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
                quit()
                sys.exit()
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_w:
                    menu.switch(-1)
                elif ev.key == pygame.K_s:
                    menu.switch(1)
                elif ev.key == pygame.K_SPACE:
                    menu.select()

        sc.blit(main.bg, (0, 0))

        menu.draw(sc, 40, 40, 50)

        sc.blit(col, (300, 300, main.sizefield, main.sizefield))
        sc.blit(fon, fon_rect)
        sc.blit(sc1, sc1_rect)
        sc.blit(sc2, sc2_rect)
        sc.blit(sc3, sc3_rect)

        pygame.display.flip()
