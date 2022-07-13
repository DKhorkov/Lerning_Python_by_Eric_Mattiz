"""Настройки для игры из упр. 14.2"""


class Settings:
    """Обычные настройки"""

    def __init__(self):
        """Инициализация статичных настроек"""

        self.screen_width = 1200
        self.screen_height = 900
        self.screen_bg_color = 'black'

        self.main_square_face = 50
        self.main_square_color = 'blue'
        self.main_square_indent = 150

        self.enemy_square_face = 50
        self.enemy_square_indent = 150
        self.enemy_square_color = 'red'

        self.bullet_width = 50
        self.bullet_height = 10
        self.bullet_color = 'white'

        self.initialize_dynamic_settings()
        self.lives_at_start = 3

    def initialize_dynamic_settings(self):
        """Инициализация динамических настроек, которые могут меняться в ходе игры"""
        self.main_square_speed = 1
        self.enemy_square_speed = 0.4
        self.direction = 1
        self.bullet_speed = 2
