"""Класс для создания корабля."""
import pygame


class Ship:
    """Корабль для игры."""

    def __init__(self, screen):
        """Инициализация атрибутов корабля."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.ship = pygame.image.load(
            "/home/dkhorkov/Рабочий стол/PythonProjects/Pet_projects/alien_invasion/images/ship3.bmp")
        self.ship_rect = self.ship.get_rect()
        self.ship_rect.center = (self.ship_rect.width / 2, self.screen_rect.height / 2)

        # Флаги для движения корабля:
        self.moving_up = False
        self.moving_down = False

    def ship_moving(self):
        """Движение корабля"""
        if self.moving_up and self.ship_rect.y > 0:
            self.ship_rect.y -= 1
        elif self.moving_down and self.ship_rect.bottom < self.screen_rect.bottom:
            self.ship_rect.y += 1

    def draw_ship(self):
        """Рисует корабль."""
        self.screen.blit(self.ship, self.ship_rect)
