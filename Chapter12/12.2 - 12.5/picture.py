"""Класс для создания картинки с целью дальнейшего вывода на экран."""
import pygame


class Picture:
    """Обычная картинка."""

    def __init__(self, screen):
        """Инициализация атрибутов картинки."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load(
            "/home/dkhorkov/Рабочий стол/PythonProjects/Pet_projects/alien_invasion/images/ship3.bmp")
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen_rect.center

        # Флаги для продолжительного движения при нажатии клавиш пользователем:
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def continuous_moving(self):
        """Если флаг включен, изображение будет продолжать двигаться."""
        if self.moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.image_rect.y += 1
        elif self.moving_up and self.image_rect.top > 0:
            self.image_rect.y -= 1
        elif self.moving_left and self.image_rect.left > 0:
            self.image_rect.x -= 1
        elif self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.image_rect.x += 1

    def draw_picture(self):
        """Рисует картинку на экране."""
        self.screen.blit(self.image, self.image_rect)
