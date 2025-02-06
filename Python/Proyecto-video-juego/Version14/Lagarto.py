import pygame
from pygame.sprite import Sprite

# Clase Lagarto
class Lagarto(Sprite):
    def __init__(self, jugador_config, screen, jugador):
        super(Lagarto, self).__init__()
        self.jugador_config = jugador_config
        self.screen = screen
        self.jugador = jugador

        # Carga la imagen del lagarto
        self.lagarto_image = pygame.image.load("../Media/lagarto.png")
        self.lagarto_image = pygame.transform.scale(self.lagarto_image, (300, 300))

        # Rectángulo del lagarto
        self.lagarto_rect = self.lagarto_image.get_rect()
        self.screen_rect = screen.get_rect()
        self.lagarto_speed = self.jugador_config.lagarto_speed

        # Posición inicial
        self.lagarto_rect.left = 0
        self.lagarto_rect.bottom = self.screen.get_height()

    def update_pos(self):
        # Mantén al lagarto en la esquina inferior izquierda
        self.lagarto_rect.left = max(0, self.lagarto_rect.left)

    def blitme(self):
        self.screen.blit(self.lagarto_image, self.lagarto_rect)