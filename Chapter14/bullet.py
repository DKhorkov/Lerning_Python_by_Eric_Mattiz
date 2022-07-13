"""Класс пуль для игры с квадратами"""
import pygame
from pygame.sprite import Sprite

from settings import Settings


class Bullet(Sprite):
    """Обычные пули"""

    def __init__(self, screen, main_square):
        """Атрибуты пули"""
        super().__init__()
        pygame.init()

        self.settings = Settings()
        self.color = self.settings.bullet_color
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.main_square = main_square

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.x = self.main_square.rect.right
        self.rect.y = self.main_square.rect.top + self.settings.main_square_face // 2 - self.settings.bullet_height // 2

    def update_bullet_position(self):
        """Полет пули"""
        self.rect.x += self.settings.bullet_speed

    def show_bullet(self):
        """Отображает пулю на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)
