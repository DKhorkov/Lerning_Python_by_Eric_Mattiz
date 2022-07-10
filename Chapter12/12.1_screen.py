# Упражнение 12.1 - Создание простого экрана любого цвета.

import pygame

screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('Some name of the screen')
screen.fill((0, 0, 255))
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            elif event.type == pygame.QUIT:
                exit()
    pygame.display.flip()

