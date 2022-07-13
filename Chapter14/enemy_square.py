"""Класс вражеского квадрата"""

import pygame
from pygame.sprite import Sprite

from settings import Settings


class EnemySquare(Sprite):
    """Квадрат, который нужно сбить"""

    def __init__(self, screen, settings):
        """Атрибуты вражеского квадрата"""
        super().__init__()
        pygame.init()
        self.settings = settings
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(0, 0, self.settings.enemy_square_face, self.settings.enemy_square_face)
        self.rect.x = self.screen_rect.right - 2 * self.settings.enemy_square_indent
        self.rect.y = self.screen_rect.top + self.settings.enemy_square_indent
        self.color = self.settings.enemy_square_color

        self.y = float(self.rect.y)

    def update_enemy_square_position(self):
        """Перемещение вражеского квадрата по экрану"""
        if self.rect.bottom > self.screen_rect.bottom:
            self.settings.direction *= -1
        elif self.rect.top < 150:
            self.settings.direction *= -1

        self.y += self.settings.direction * self.settings.enemy_square_speed
        self.rect.y = self.y

    def show_enemy_square(self):
        """Показывает на экране вражеский квадрат"""
        pygame.draw.rect(self.screen, self.color, self.rect)
