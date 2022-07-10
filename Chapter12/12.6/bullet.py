"""Класс пули для задания 12.6"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Обычная пуля"""

    def __init__(self, screen, ship):
        """Инициализация атрибутов пули."""
        super().__init__()
        self.screen = screen
        self.bullet = pygame.Rect(0, 0, 50, 15)
        self.ship_rect = ship.ship_rect
        self.bullet.topleft = self.ship_rect.topright
        self.bullet.top += 25
        self.color = 'red'

    def update(self):
        """Полет пули."""
        self.bullet.x += 1

    def draw_bullet(self):
        """Рисует пулю на экране."""
        pygame.draw.rect(self.screen, self.color, self.bullet)
