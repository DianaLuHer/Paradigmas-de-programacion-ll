import pygame
from pygame.sprite import Sprite

class Fuego(Sprite):
    def __init__(self, jugador_config, screen, lagarto):
        super(Fuego, self).__init__()
        self.jugador_config = jugador_config
        self.screen = screen
        self.lagarto = lagarto

        # Carga la imagen del fuego
        self.fuego_image = pygame.image.load("../Media/fuego (2).png")
        self.fuego_image = pygame.transform.scale(self.fuego_image, (80, 80))

        # Rectángulo del fuego
        self.rect = self.fuego_image.get_rect()
        self.screen_rect = screen.get_rect()

        # Máscara del fuego para colisiones precisas
        self.mask = pygame.mask.from_surface(self.fuego_image)

        # Velocidad y posición inicial
        self.speed = self.jugador_config.fuego_speed
        self.rect.x = -100
        self.rect.y = -100

        # Disparo
        self.last_shot_time = pygame.time.get_ticks()
        self.shot_interval = 3000  # 3 segundos
        self.is_shooting = False

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if not self.is_shooting and current_time - self.last_shot_time >= self.shot_interval:
            self.rect.centerx = self.lagarto.lagarto_rect.right
            self.rect.centery = self.lagarto.lagarto_rect.centery
            self.is_shooting = True
            self.last_shot_time = current_time

    def update(self):
        if self.is_shooting:
            self.rect.x += self.speed
            if self.rect.left > self.screen_rect.right:
                self.is_shooting = False

    def check_collision(self, jugador):
        if self.is_shooting:  # Solo verifica colisión si el fuego está en movimiento
            offset = (jugador.rect.x - self.rect.x, jugador.rect.y - self.rect.y)
            jugador_mask = pygame.mask.from_surface(jugador.image)
            if self.mask.overlap(jugador_mask, offset):  # Verifica la superposición
                return True
        return False

    def blitme(self):
        if self.is_shooting:
            self.screen.blit(self.fuego_image, self.rect)