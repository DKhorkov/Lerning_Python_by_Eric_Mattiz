"""Класс для создания квадрата, которым будет управлять пользователь"""

import pygame

from settings import Settings


class MainSquare:
    """Квадрат для управления пользователем"""

    def __init__(self, screen):
        """Атрибуты квадрата"""
        pygame.init()
        self.settings = Settings()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.color = self.settings.main_square_color

        self.rect = pygame.Rect(0, 0, self.settings.main_square_face, self.settings.main_square_face)
        self.rect.x = self.screen_rect.x + self.settings.main_square_indent
        self.rect.y = self.screen_rect.y + self.settings.main_square_indent

    def update_main_square_position(self, moving_up, moving_down):
        """Изменение позиции основного корабля"""
        if moving_up and self.rect.y > 150:
            self.rect.y -= self.settings.main_square_speed
        elif moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.main_square_speed

    def show_main_square(self):
        """Отображает основной квадрат на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)
