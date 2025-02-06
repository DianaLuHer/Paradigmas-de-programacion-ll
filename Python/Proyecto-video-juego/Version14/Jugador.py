import pygame
from config import Config

class Player:
    def __init__(self, x, y, scale, sprite_size):
        self.scale = scale
        self.sprite_size = sprite_size
        self.center_x = x
        self.center_y = y
        self.last_hit_time = 0  # Tiempo del último daño recibido
        self.invulnerability_duration = 2000  # Duración de inmunidad (en milisegundos)

        self.walk_right_textures = [
            pygame.transform.scale(
                pygame.image.load(f"../Media/sp{i}.png").convert_alpha(), self.sprite_size
            )
            for i in range(1, 10)
        ]
        self.walk_left_textures = [
            pygame.transform.flip(img, True, False) for img in self.walk_right_textures
        ]
        self.jump_textures = [
            pygame.transform.scale(
                pygame.image.load("../Media/salt5.png").convert_alpha(), self.sprite_size
            )
        ]
        self.standing_image = pygame.transform.scale(
            pygame.image.load("../Media/estatica.png").convert_alpha(), self.sprite_size
        )

        self.current_texture = 0
        self.image = self.standing_image
        self.rect = self.image.get_rect(center=(self.center_x, self.center_y))
        self.direction = "right"
        self.animating = False
        self.is_jumping = False
        self.y_velocity = 0
        self.gravity = 1
        self.jump_speed = 20
        self.mask = pygame.mask.from_surface(self.image)  # Máscara para colisiones

    def update(self):
        if self.is_jumping:
            self.image = self.jump_textures[0]
        elif self.animating:
            self.current_texture += 1
            if self.current_texture >= len(self.walk_right_textures):
                self.current_texture = 0
            self.image = self.walk_right_textures[self.current_texture] if self.direction == "right" else self.walk_left_textures[self.current_texture]
        else:
            self.image = self.standing_image

    def move(self, keys):
        self.animating = False
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            self.direction = "right"
            self.animating = True
        elif keys[pygame.K_LEFT]:
            self.rect.x -= 5
            self.direction = "left"
            self.animating = True

        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.y_velocity = -self.jump_speed

    def update_jump(self):
        if self.is_jumping:
            self.rect.y += self.y_velocity
            self.y_velocity += self.gravity
            if self.rect.bottom >= Config().screen_height - 50:  # Ajuste de suelo
                self.rect.bottom = Config().screen_height - 50
                self.is_jumping = False

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Config().screen_width:
            self.rect.right = Config().screen_width

    def take_damage(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_hit_time > self.invulnerability_duration:
            self.last_hit_time = current_time
            return True  # El jugador puede recibir daño
        return False  # El jugador es inmune temporalmente