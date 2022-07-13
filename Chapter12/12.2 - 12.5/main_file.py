# Основной файл для запуска заданий 12.2 - 12.5

import pygame

from picture import Picture


class Main:
    """Класс для запуска приложения."""

    def __init__(self):
        """Инициализация основных атрибутов класса."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 900))
        pygame.display.set_caption("Misha on black screen")
        self.pic = Picture(self.screen)

    def run_app(self):
        """Запуск приложения"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.pic.moving_up = True
                    elif event.key == pygame.K_s:
                        self.pic.moving_down = True
                    elif event.key == pygame.K_a:
                        self.pic.moving_left = True
                    elif event.key == pygame.K_d:
                        self.pic.moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.pic.moving_up = False
                    elif event.key == pygame.K_s:
                        self.pic.moving_down = False
                    elif event.key == pygame.K_a:
                        self.pic.moving_left = False
                    elif event.key == pygame.K_d:
                        self.pic.moving_right = False
            # Данная строка кода нужна, чтобы не оставалось остаточного следа от рисунка при движении:
            self.screen.fill('black')

            self.pic.continuous_moving()
            self.pic.draw_picture()
            pygame.display.flip()  # отображение экрана.


if __name__ == "__main__":
    misha = Main()
    misha.run_app()
