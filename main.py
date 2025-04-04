import pygame
from snake import Snake
from boost import Boost, Blockboost
import random
import sys

resolution = 400
bgcolor = (100, 100, 100)
bgcolor1 = (200, 200, 200)
white = (255, 255, 255)
snakecolor = (0, 255, 127)
sizecell = 20
sizefield = resolution//sizecell
bg = pygame.image.load('imag/fon.png')
wh = pygame.Surface((sizecell - 1, sizecell - 1))
wh.fill(white)
snc = pygame.image.load('imag/pixil-frame-21.png')
list_score = []

pygame.init()
field = pygame.display.set_mode((resolution, resolution))
pygame.display.set_caption("Sssnake")
clock = pygame.time.Clock()
font_score = pygame.font.SysFont("Arial", 26, bold=True)
font_gameover = pygame.font.SysFont("Arial", 50, bold=True)


def draw1(color, i, j):
    field.blit(color, (i*sizecell, j*sizecell, sizecell, sizecell))


def draw(color, i, j):
    pygame.draw.rect(
        field, color, [i*sizecell, j*sizecell, sizecell, sizecell])


def drawbg(color):
    # for cell in range(sizefield):
    #     for cell1 in range(sizefield):
    #         if ((cell + cell1) % 2 == 0):
    #             color = bgcolor
    #         else:
    #             color = bgcolor1
    #         color = (0, 0, 0)
    #         draw(color, cell, cell1)
    field.blit(color, (0, 0))


def drawobst(color, obstacle):
    for i in obstacle:
        x, y = i
        field.blit(color, (x*sizecell, y*sizecell, sizecell, sizecell))


def end_game(count):
    while True:
        draw_gameover = font_gameover.render(
            'GAME OVER', 1, pygame.Color("orange"))
        field.blit(draw_gameover, (resolution //
                                   2 - 125, resolution//2 - 50))
        pygame.display.flip()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                with open('score.txt', 'r') as f:
                    list_score.append(int(f.readline()))
                    list_score.append(int(f.readline()))
                    list_score.append(int(f.readline()))
                    list_score.append(count)
                    list_score.sort()
                with open('score.txt', 'w')as f:
                    f.write(str(list_score[3]) + '\n')
                    f.write(str(list_score[2]) + '\n')
                    f.write(str(list_score[1]))

                pygame.quit()
                sys.exit()


def object_interaction_controller(snake, apple, multiapple, fast, slow, obstacle, Block_fast, Block_slow,
                                  fps, need_fast, need_slow, need_Block_fast, need_Block_slow, need_multiapple):
    # генерация различных объектов
    # oe_i - once every i apple
    fps_and_fast_oc_i = 3
    slow_blockfast_blockslow_oc_i = 4
    multiapple_oc_i = 5
    sizeof_block = 25

    if (snake.body[-1] == apple.coords):
        apple.new(snake.body, obstacle)
        apple.count += 1
        snake.len += 1
        if (apple.count % fps_and_fast_oc_i == 0):
            fps += 1
            need_fast = True
            fast.new(snake.body, obstacle)
        if (apple.count % slow_blockfast_blockslow_oc_i == 0):
            need_slow = True
            slow.new(snake.body, obstacle)

            need_Block_fast = True
            Block_fast.new(snake.body, obstacle)
            Block_fast.body = Block_fast.body[-sizeof_block:]

            need_Block_slow = True
            Block_slow.new(snake.body, obstacle)
            Block_slow.body = Block_slow.body[-sizeof_block:]
        if (apple.count % multiapple_oc_i == 0):
            need_multiapple = True
            multiapple.new(snake.body, obstacle)

    # съедение объектов
    if (snake.body[-1] == slow.coords):
        need_slow = False
        fps = fps - 1
    if (snake.body[-1] == fast.coords):
        need_fast = False
        fps = fps + 1
    if (snake.body[-1] == multiapple.coords):
        need_multiapple = False
        multiapple.count += 1
        snake.len += 1

    return (snake, apple, multiapple, fast, slow, Block_fast, Block_slow,
            fps, need_fast, need_slow, need_Block_fast, need_Block_slow, need_multiapple)


def snake_controll(snake):
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and not (snake.vx == 0 and snake.vy == 1):
        snake.vx, snake.vy = 0, -1
    if key[pygame.K_s] and not (snake.vx == 0 and snake.vy == -1):
        snake.vx, snake.vy = 0, 1
    if key[pygame.K_a] and not (snake.vx == 1 and snake.vy == 0):
        snake.vx, snake.vy = -1, 0
    if key[pygame.K_d] and not (snake.vx == -1 and snake.vy == 0):
        snake.vx, snake.vy = 1, 0

    return snake


def if_end_game(snake, ac, mc, obstacle):
    if (len(set(snake.body)) != ac + mc + 1 or
        snake.body[-1][0] < 0 or snake.body[-1][0] > sizefield - 1 or
            snake.body[-1][1] < 0 or snake.body[-1][1] > sizefield - 1):
        end_game(ac + mc * 2)
    if (snake.body[-1] in obstacle):
        end_game(ac + mc * 2)


def draw_all(snake, fast, slow, Block_fast, Block_slow, multiapple, apple, obstacle,
             need_Block_fast, need_Block_slow, need_slow, need_fast, need_multiapple):
    drawbg(bg)
    # отрисовка блоковых бустов
    if need_Block_fast:
        Block_fast.draw(field, sizecell)
    if need_Block_slow:
        Block_slow.draw(field, sizecell)

    # отрисовка препятствий
    drawobst(wh, obstacle)

    # отрисовка змейки
    for cell in snake.body:
        x, y = cell
        draw1(snake.color, x, y)

    # отрисовка обычных бустов
    if need_slow:
        draw1(slow.color, slow.x, slow.y)
    if need_fast:
        draw1(fast.color, fast.x, fast.y)
    if need_multiapple:
        draw1(multiapple.color, multiapple.x, multiapple.y)
    draw1(apple.color, apple.x, apple.y)

    # отрисовывает score
    draw_score = font_score.render(
        f'SCORE : {apple.count + multiapple.count * 2}', 1, pygame.Color("orange"))
    field.blit(draw_score, (5, 5))


def in_block(snake, Block_fast, Block_slow, apple, flag_fast, flag_slow):
    # проверка на "нахождение в блоковом бусте"
    if (snake.body[-1] in Block_fast.body and apple.count >= 1 and flag_fast == 0):
        flag_fast = 1

    elif (not (snake.body[-1] in Block_fast.body) and apple.count >= 1 and flag_fast == 1):
        flag_fast = 0

    if (snake.body[-1] in Block_slow.body and apple.count >= 1 and flag_slow == 0):
        flag_slow = 1

    elif (not (snake.body[-1] in Block_slow.body) and apple.count >= 1 and flag_slow == 1):
        flag_slow = 0
    return (flag_fast, flag_slow)


def run(obstacle):
    # создаю нужные объекты и тд
    fps = 8
    need_slow = False
    need_fast = False
    need_multiapple = False
    need_Block_fast = False
    need_Block_slow = False

    snake = Snake()
    snake.new([], obstacle)
    snake.color = snc

    color_apple = pygame.image.load('imag/applenorm1.png')
    color_fast = pygame.image.load('imag/fast.png')
    color_slow = pygame.image.load('imag/slow.png')
    color_multiapple = pygame.image.load('imag/multiapple.png')
    apple = Boost(color_apple)
    apple.new(snake.body, obstacle)
    slow = Boost(color_slow)
    fast = Boost(color_fast)
    multiapple = Boost(color_multiapple)

    color_bfast = pygame.image.load('imag/fastblock1.png')
    color_bslow = pygame.image.load('imag/slowblock1.png')
    Block_fast = Blockboost(color_bfast)
    Block_slow = Blockboost(color_bslow)

    flag_fast = 0
    flag_slow = 0

    # основный цикл, который отрисовывает все и тут прописано управление змейки и тд
    while True:
        # заканчивает игруБ когда нажимается кнопка "крестик"(справа сверху)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

        draw_all(snake, fast, slow, Block_fast, Block_slow, multiapple, apple, obstacle,
                 need_Block_fast, need_Block_slow, need_slow, need_fast, need_multiapple)

        # передвежение змейки
        x, y = snake.body[-1]
        x += snake.vx
        y += snake.vy
        snake.body.append((x, y))
        snake.body = snake.body[-snake.len:]

        # проверка на столкновения с препятствиями и с телом змеи
        if_end_game(snake, apple.count, multiapple.count, obstacle)

        snake, apple, multiapple, fast, slow, Block_fast, Block_slow, fps, need_fast, need_slow, need_Block_fast, need_Block_slow, need_multiapple = object_interaction_controller(snake, apple, multiapple, fast, slow, obstacle, Block_fast, Block_slow,
                                                                                                                                                                                   fps, need_fast, need_slow, need_Block_fast, need_Block_slow, need_multiapple)

        pygame.display.flip()

        flag_fast, flag_slow = in_block(
            snake, Block_fast, Block_slow, apple, flag_fast, flag_slow)

        # изменение скорости на блоковом бусте
        # во сколько раз увеличьться скорость при нахождении в block
        x_in_fast = 4
        x_in_slow = 2
        if (flag_fast == 1):
            clock.tick(fps * x_in_fast)
            print("fast")
        elif (flag_slow == 1):
            clock.tick(fps//x_in_slow)
            print("slow")
        else:
            clock.tick(fps)

        # управление змейкой
        snake = snake_controll(snake)
