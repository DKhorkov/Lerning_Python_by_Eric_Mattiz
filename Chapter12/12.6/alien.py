"""Класс пришельца"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс пришельца для игры"""

    def __init__(self, screen):
        """Инициализация атрибутов класса пришельцев"""
        super().__init__()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.alien = pygame.image.load(
            "/home/dkhorkov/Рабочий стол/PythonProjects/Pet_projects/alien_invasion/images/alien.bmp")
        self.rect = self.alien.get_rect()
        self.rect.center = (self.screen_rect.width - 100, self.screen_rect.height - 900)

    def update_alien(self):
        """Обновление местоположения пришельца"""
        self.rect.x -= 0.5

    def draw_alien(self):
        """Рисует пришельца на экране"""
        self.screen.blit(self.alien, self.rect)
