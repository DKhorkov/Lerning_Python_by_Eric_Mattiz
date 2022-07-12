"""Класс для создания корабля."""
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Корабль для игры."""

    def __init__(self, screen):
        """Инициализация атрибутов корабля."""
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.ship = pygame.image.load(
            "/home/dkhorkov/Рабочий стол/PythonProjects/Pet_projects/alien_invasion/images/ship3.bmp")
        self.rect = self.ship.get_rect()
        self.rect.center = (self.rect.width / 2, self.screen_rect.height / 2)

        # Флаги для движения корабля:
        self.moving_up = False
        self.moving_down = False

    def ship_moving(self):
        """Движение корабля"""
        if self.moving_up and self.rect.y > 0:
            self.rect.y -= 2
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 2

    def draw_ship(self):
        """Рисует корабль."""
        self.screen.blit(self.ship, self.rect)
