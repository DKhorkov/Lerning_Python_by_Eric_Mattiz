"""Класс для отображения статистики игрока"""
import pygame.font


class Scoreboard:
    """Игровая статистика"""

    def __init__(self, screen, score):
        """Атрибуты игровой статистики"""
        pygame.init()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.lives = 3
        self.score = score

        self.text_color = (245, 255, 250)
        self.font = pygame.font.SysFont(None, 40)

        self.draw_score()
        self.draw_lives()

    def draw_score(self):
        """Создает изображение текста очков"""
        score_str = f' ENEMY-SQUARES KILLED: {self.score}'
        self.score_image = self.font.render(score_str, True, self.text_color, 'black')  # Черный фон для надписи

        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.left = self.screen_rect.right - 500
        self.score_image_rect.top = 20

    def draw_lives(self):
        """Создает изображение текста жизней"""
        lives_str = f'LIVES: {str(self.lives)}'
        self.lives_image = self.font.render(lives_str, True, self.text_color, 'black')

        self.lives_image_rect = self.lives_image.get_rect()
        self.lives_image_rect.top = 20
        self.lives_image_rect.left = 20

    def show_score(self):
        """Вывод очков на экран"""
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.lives_image, self.lives_image_rect)