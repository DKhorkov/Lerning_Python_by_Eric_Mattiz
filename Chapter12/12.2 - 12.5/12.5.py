
import pygame

screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('Some name of the screen')
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_ESCAPE:
                exit()
        elif event.type == pygame.QUIT:
            exit()
    pygame.display.flip()
