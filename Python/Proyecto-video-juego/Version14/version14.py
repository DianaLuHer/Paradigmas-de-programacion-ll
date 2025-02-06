import pygame
import sys
from config import Config
from Lagarto import Lagarto
from Fuego import Fuego
from Jugador import Player
from Game_functionalities import create_jugador, game_events, screen_refresh
from conexion import Conexion, Error


def guardar_nombre_score(nombre, score):
    try:
        cn1 = Conexion.get_connection()
        cursor = cn1.cursor()

        # Insertar en la tabla 'jugador' los valores correctos
        cursor.execute("INSERT INTO jugador (nombre, score) VALUES (%s, %s)", (nombre, score))

        # Guardar los cambios en la base de datos
        cn1.commit()
        print("Jugador guardado correctamente")

    except Error as e:
        print(f"Error al guardar la partida | {e}")

    finally:
        if cursor:
            cursor.close()
        if cn1:
            cn1.close()


# Clase para el fondo
class Background:
    def __init__(self, images, screen_width):
        self.images = [pygame.image.load(img).convert_alpha() for img in images]
        self.bg_width = self.images[0].get_width()
        self.screen_width = screen_width

    def draw(self, screen, scroll):
        for x in range(-1, int(self.screen_width / self.bg_width) + 3):
            for idx, image in enumerate(self.images):
                speed = 1 + idx * 0.2
                offset = (x * self.bg_width) - (scroll * speed)
                screen.blit(image, (offset, 0))


# Clase para el suelo
class Ground:
    def __init__(self, image_path, screen_width, screen_height):
        self.image = pygame.transform.scale(
            pygame.image.load(image_path).convert_alpha(),
            (screen_width, screen_height // 8)
        )
        self.ground_width = self.image.get_width()
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self, screen, scroll):
        for x in range(-1, int(self.screen_width / self.ground_width) + 3):
            offset = (x * self.ground_width) - (scroll * 2.5)
            screen.blit(self.image, (offset, self.screen_height - self.image.get_height()))


# Clase para la computadora al final del juego
class Computer:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# Función para mostrar la pantalla de inicio con el botón "Start"
def show_start_screen(screen, config):
    font = pygame.font.Font(None, 74)
    title_text = font.render('Bienvenido a LapRun!', True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(config.screen_width // 2, config.screen_height // 3))
    screen.blit(title_text, title_rect)

    start_button = pygame.Rect(config.screen_width // 2 - 100, config.screen_height // 2, 200, 50)
    pygame.draw.rect(screen, (0, 153, 76), start_button, border_radius=10)
    start_text = font.render('Start', True, (255, 255, 255))
    start_text_rect = start_text.get_rect(center=start_button.center)
    screen.blit(start_text, start_text_rect)

    pygame.display.flip()
    return start_button


# Función para ingresar el nombre del jugador
def get_player_name(screen, config):
    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(config.screen_width // 2 - 125, config.screen_height // 2 + 60, 250, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if text.strip():
                            return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((0, 0, 0))
        prompt_text = font.render('Nombre del jugador:', True, (255, 255, 255))
        prompt_rect = prompt_text.get_rect(center=(config.screen_width // 2, config.screen_height // 2))
        screen.blit(prompt_text, prompt_rect)

        txt_surface = font.render(text, True, color)
        input_box.w = max(250, txt_surface.get_width() + 10)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2, border_radius=10)

        pygame.display.flip()
        clock.tick(30)


# Función para mostrar una pantalla de carga
def show_loading_screen(screen, config):
    font = pygame.font.Font(None, 74)
    loading_text = font.render('', True, (255, 255, 255))
    loading_rect = loading_text.get_rect(center=(config.screen_width // 2, config.screen_height // 2))
    screen.fill((0, 0, 0))
    screen.blit(loading_text, loading_rect)
    pygame.display.flip()


# Función principal del juego
def run_game():
    pygame.init()
    config = Config()
    screen = pygame.display.set_mode((config.screen_width, config.screen_height))
    pygame.display.set_caption(config.game_title)

    show_loading_screen(screen, config)

    pygame.mixer.init()
    pygame.mixer.music.load("../Media/musica.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    background = Background([f"../Media/plx-{i}.png" for i in range(1, 6)], config.screen_width)
    ground = Ground("../Media/ground.png", config.screen_width, config.screen_height)

    while True:
        start_button = show_start_screen(screen, config)
        player_name = ""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):
                        player_name = get_player_name(screen, config)
                        print(f"Nombre del jugador: {player_name}")
                        break

            if player_name:
                break

        start_game(player_name, screen, config)


def start_game(player_name, screen, config):
    jugador = create_jugador(config, screen)
    lagarto = Lagarto(config, screen, jugador)
    fuego = Fuego(config, screen, lagarto)
    background = Background([f"../Media/plx-{i}.png" for i in range(1, 6)], config.screen_width)
    ground = Ground("../Media/ground.png", config.screen_width, config.screen_height)
    computer = Computer("../Media/computadora.png", config.screen_width - 100, config.screen_height - 200)

    player = Player(config.screen_width // 2, config.screen_height - 100, 1.0, (128, 128))
    scroll = 0
    clock = pygame.time.Clock()

    score = 0
    start_time = pygame.time.get_ticks()
    font = pygame.font.Font(None, 36)


    while True:
        clock.tick(60)
        game_events(jugador)
        keys = pygame.key.get_pressed()

        player.move(keys)
        player.update_jump()
        player.update()

        if keys[pygame.K_RIGHT]:
            scroll += 5
        elif keys[pygame.K_LEFT] and scroll > 0:
            scroll -= 5

        screen.fill((135, 206, 235))
        background.draw(screen, scroll)
        ground.draw(screen, scroll)
        screen_refresh(config, screen, jugador, lagarto, fuego)

        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        score = int(elapsed_time)

        score_text = font.render(f'Puntaje: {score}', True, (255, 255, 255))
        name_text = font.render(f'Jugador: {player_name}', True, (255, 255, 255))
        screen.blit(score_text, (10, 40))
        screen.blit(name_text, (10, 10))
        screen.blit(player.image, player.rect)

        if elapsed_time > 15:
            computer.draw(screen)
            if player.rect.colliderect(computer.rect):
                print("¡Has ganado! Felicidades, llegaste a la computadora.")
                victory_text = font.render("¡Has ganado!", True, (255, 255, 0))
                victory_rect = victory_text.get_rect(center=(config.screen_width // 2, config.screen_height // 2))
                screen.blit(victory_text, victory_rect)
                pygame.display.flip()

                pygame.time.wait(3000)
                pygame.quit()
                sys.exit()

        pygame.display.flip()


if __name__ == "__main__":
    run_game()
