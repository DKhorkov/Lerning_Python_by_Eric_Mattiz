# Упражнения 13.1 и 13.4

import pygame
from star_class import Star

pygame.init()
screen = pygame.display.set_mode((1200, 900))
screen_rect = screen.get_rect()
pygame.display.set_caption('13.1-13.4 endless starfall')
stars = pygame.sprite.Group()
for i in range(50):
    star = Star(screen)
    stars.add(star)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(pygame.image.load('space.bmp'), pygame.image.load('space.bmp').get_rect())
    for star in stars.sprites():
        if star.star_rect.top > 0 and star.star_rect.bottom < screen_rect.bottom:
            star.star_rect.y += 1
        elif star.star_rect.bottom >= screen_rect.bottom and star.star_rect.top > 0:
            stars.remove(star)
        star.draw_star()
    if len(stars) < 50:
        star = Star(screen)
        stars.add(star)
    pygame.display.flip()
