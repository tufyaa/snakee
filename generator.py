import random

# эта функция генерирует объекты так, чтобы они не попадали на стены и на змейку

sizefield = 20

field1 = []
for i in range(sizefield):
    for j in range(sizefield):
        field1.append((i, j))


def gen(body, obstacle):
    for i in body:
        if i in field1:
            field1.remove(i)
    for i in obstacle:
        if i in field1:
            field1.remove(i)

    return random.choice(field1)
