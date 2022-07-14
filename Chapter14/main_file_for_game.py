"""Основной файл для игры из упражнения 14.2, 14.3"""

# Упражнение 14.1, 14.4, 14.5 выполнено в рамках игры Alien Invasion

import pygame
from time import sleep

from settings import Settings
from main_square import MainSquare
from enemy_square import EnemySquare
from bullet import Bullet
from scoreboard import Scoreboard
from button import Button


class Game:
    """Игра с попаданием в движущийся квадрат"""

    def __init__(self):
        """Инициализация атрибутов класса"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Shooting in square')

        self.main_square = MainSquare(self.screen, self.settings)
        self.enemy_square = EnemySquare(self.screen, self.settings)
        self.bullets = pygame.sprite.Group()

        self.scoreboard = Scoreboard(self.screen, 0)

        self.play_button = Button(self.screen, 'play')

        self.moving_up = False
        self.moving_down = False
        self.game_active = False

    def check_play_button(self, mouse_position):
        """Проверяет, нужно ли вывести кнопку"""
        button_clicked = self.play_button.rect.collidepoint(mouse_position)  # коллизия курсора мыши с кнопкой

        if button_clicked and not self.game_active:
            self.game_active = True

    def check_events(self):
        """Проверяет события, зависящие от действия пользователя"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.moving_up = True
                elif event.key == pygame.K_q:
                    exit()
                elif event.key == pygame.K_s:
                    self.moving_down = True
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(self.screen, self.main_square, self.settings)
                    self.bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.moving_up = False
                elif event.key == pygame.K_s:
                    self.moving_down = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    def check_bullet(self):
        """Проверяет, не улетели ли пули за вражеский квадрат или не попали ли в него"""
        for bullet in self.bullets.sprites():
            bullet.update_bullet_position()
            if bullet.rect.right >= self.enemy_square.rect.right:
                self.bullets.empty()
                self.scoreboard.lives -= 1
                if self.scoreboard.lives == 0:
                    self.game_active = False
                    self.scoreboard.lives = self.settings.lives_at_start
                    self.scoreboard.score = 0
                    self.settings.initialize_dynamic_settings()
                sleep(1)
                break
            bullet.show_bullet()

        collision = pygame.sprite.spritecollideany(self.enemy_square, self.bullets)
        if collision:
            self.bullets.empty()
            self.settings.scaling()
            self.scoreboard.score += 1
            self.scoreboard.draw_score()
            sleep(0.5)
            self.enemy_square = EnemySquare(self.screen, self.settings)

    def update_screen(self):
        """Обновление картинки на экране"""
        self.screen.fill(self.settings.screen_bg_color)

        self.scoreboard.draw_lives()
        self.scoreboard.draw_score()
        self.scoreboard.show_score()  # Отображение убитых вражеских квадратов

        self.main_square.update_main_square_position(self.moving_up, self.moving_down)
        self.main_square.show_main_square()

        self.enemy_square.update_enemy_square_position()
        self.enemy_square.show_enemy_square()

        self.check_bullet()

    def run_game(self):
        """Запуск игры"""
        while True:
            if not self.game_active:
                self.play_button.draw_button()
                self.check_events()
            self.check_events()
            if self.game_active:
                self.update_screen()
            pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run_game()
