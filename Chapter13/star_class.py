"""Класс для создания звезды."""
import pygame
from pygame.sprite import Sprite
from random import randint


class Star(Sprite):
    """Звезда на экране"""

    def __init__(self, screen):
        """Инициализация атрибутов звезды."""
        super().__init__()
        self.screen = screen
        self.star = pygame.image.load('star.bmp')
        self.star.set_colorkey('white')
        self.star_rect = self.star.get_rect()
        self.star_rect.x = randint(10, 1000)
        self.star_rect.y = randint(10, 500)

    def draw_star(self):
        """Рисует звезду"""
        self.screen.blit(self.star, self.star_rect)
