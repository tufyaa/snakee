import pygame

obstacle0 = []

obstacle1 = []

obstacle1.append((2, 2))
obstacle1.append((3, 2))
obstacle1.append((2, 3))
obstacle1.append((3, 3))
obstacle1.append((16, 2))
obstacle1.append((16, 3))
obstacle1.append((17, 2))
obstacle1.append((17, 3))
obstacle1.append((2, 16))
obstacle1.append((3, 16))
obstacle1.append((2, 17))
obstacle1.append((3, 17))
obstacle1.append((16, 16))
obstacle1.append((17, 16))
obstacle1.append((16, 17))
obstacle1.append((17, 17))

obstacle2 = []

for i in range(3, 17):
    obstacle2.append((4, i))
    obstacle2.append((15, i))

obstacle3 = []

for i in range(4):
    obstacle3.append((2, 2 + i))
    obstacle3.append((2 + i, 2))
    obstacle3.append((17, 2 + i))
    obstacle3.append((17 - i, 2))
    obstacle3.append((2, 17 - i))
    obstacle3.append((2 + i, 17))
    obstacle3.append((17, 17 - i))
    obstacle3.append((17 - i, 17))

obstacle4 = []

for i in range(3, 17):
    obstacle4.append((4, i))
    obstacle4.append((15, i))

for i in range(7, 13):
    obstacle4.append((i, 6))
    obstacle4.append((i, 12))
