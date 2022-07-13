# Основной файл для упражнения 12.6, 13.5 - 13.6
import pygame

from ship import Ship
from bullet import Bullet
from alien import Alien


class Game:
    """Класс для запуска игры."""

    def __init__(self):
        """Инициализация атрибутов класса игры."""
        pygame.init()
        self.screen = pygame.display.set_mode((1800, 1000))
        pygame.display.set_caption('12.6')
        self.ship = Ship(self.screen)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.game_active = True

        self.create_fleet()  # Флот создается тут, а не в цикле игры, иначе дичь.

    def create_fleet(self):
        """Создает флот из 12 пришельцев (2 ряда по 6 штук)"""
        for row in range(2):
            for i in range(6):
                alien = Alien(self.screen)
                alien.y = alien.rect.y + alien.rect.y * 3 * i
                alien.x = alien.rect.x - alien.rect.y * 3 * row
                alien.rect.y = alien.y
                alien.rect.x = alien.x
                self.aliens.add(alien)

    def check_bullets(self):
        """Удаляет пулю, если она уходит за экран, удаляет пулю и пришельца в случае их столкновения."""
        for bullet in self.bullets:
            if bullet.rect.right >= 1800:
                self.bullets.remove(bullet)
            for alien in self.aliens:
                if bullet.rect.right >= alien.rect.left:
                    if bullet.rect.y >= alien.rect.top and bullet.rect.y <= alien.rect.bottom:
                        self.bullets.remove(bullet)
                        self.aliens.remove(alien)

    def ship_collide(self):
        """Столкновение корабля с пришельцами останавливает игру"""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.game_active = False

    def check_events(self):
        """Проверяет события"""
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

    def check_alien_edges(self):
        """Если пришельцы достигают левого крана экрана, то флот удаляется и создается заново"""
        for alien in self.aliens:
            if alien.rect.x < 10:
                for alien in self.aliens:
                    self.aliens.remove(alien)
                self.create_fleet()
                break

    def update_display(self):
        """Обновляет экран и объекты на нем."""
        self.ship.ship_moving()

        if self.game_active:
            self.ship_collide()
            # Заливка экрана должна быть до прорисовки объектов, иначе они будут закрашены (пользователь не увидит их).
            self.screen.fill('black')
            self.bullets.update()
            self.check_alien_edges()
            for alien in self.aliens.sprites():
                alien.update_alien()
                alien.draw_alien()
            self.check_bullets()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.draw_ship()
        pygame.display.flip()

    def run_game(self):
        """Запуск игры"""
        while True:
            self.check_events()
            self.update_display()


if __name__ == "__main__":
    game = Game()
    game.run_game()
