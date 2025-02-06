import pygame
import sys
from Jugador import Player

# Manejar los eventos del juego
def game_events(jugador):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            game_events_keydown(event, jugador)
        elif event.type == pygame.KEYUP:
            game_events_keyup(event, jugador)

def create_jugador(config, screen):
    return Player(config.screen_width // 2, config.screen_height - 100, 1.0, (128, 128))


# Manejar teclas presionadas
def game_events_keydown(event, jugador):
    if event.key == pygame.K_RIGHT:
        jugador.is_moving_right = True
    elif event.key == pygame.K_LEFT:
        jugador.is_moving_left = True
    elif event.key == pygame.K_UP and not jugador.is_jumping:
        jugador.is_jumping = True
        jugador.y_velocity = jugador.jump_speed

# Manejar teclas soltadas
def game_events_keyup(event, jugador):
    if event.key == pygame.K_RIGHT:
        jugador.is_moving_right = False
    elif event.key == pygame.K_LEFT:
        jugador.is_moving_left = False


def show_game_over(screen, jugador_config):
    # Cargar la imagen del Game Over
    game_over_image = pygame.image.load("../Media/Game_over2.jpg").convert_alpha()
    game_over_rect = game_over_image.get_rect(
        center=(jugador_config.screen_width // 2, jugador_config.screen_height // 2))

    # Mostrar la imagen en pantalla
    screen.blit(game_over_image, game_over_rect)

    pygame.display.flip()
    pygame.time.wait(3000)  # Espera 3 segundos antes de cerrar el juego

def screen_refresh(jugador_config, screen, jugador, lagarto, fuego):
    jugador.update_jump()
    lagarto.update_pos()
    fuego.update()

    lagarto.blitme()
    fuego.blitme()
    fuego.shoot()

    if fuego.check_collision(jugador):  # Verificar si realmente hay colisión
        jugador_config.lives -= 1  # Reduce vidas solo si hay colisión
        if jugador_config.lives <= 0:
            show_game_over(screen, jugador_config)

    pygame.display.flip()