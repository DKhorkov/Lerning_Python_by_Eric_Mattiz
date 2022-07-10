# Основной файл для упражнения 12.6
import pygame

from ship import Ship
from bullet import Bullet


class Game:
    """Класс для запуска игры."""

    def __init__(self):
        """Инициализация атрибутов класса игры."""
        self.screen = pygame.display.set_mode((1200, 900))
        pygame.display.set_caption('12.6')
        self.ship = Ship(self.screen)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Запуск игры"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.ship.moving_up = True
                    elif event.key == pygame.K_s:
                        self.ship.moving_down = True
                    elif event.key == pygame.K_SPACE:
                        new_bullet = Bullet(self.screen, self.ship)
                        self.bullets.add(new_bullet)
                    elif event.key == pygame.K_q:
                        exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.ship.moving_up = False
                    elif event.key == pygame.K_s:
                        self.ship.moving_down = False
            self.ship.ship_moving()
            self.bullets.update()

            # Заливка экрана должна быть до прорисовки объектов, иначе они будут закрашены (пользователь не увидит их).
            self.screen.fill('black')
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.draw_ship()

            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run_game()
